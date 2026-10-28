import subprocess
import sys
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_release.py"


@pytest.fixture
def release_project(tmp_path):
    (tmp_path / "pyproject.toml").write_text(
        '[project]\nname = "flaskteroids-turbo"\nversion = "0.1.0"\n'
    )
    (tmp_path / "uv.lock").write_text(
        '[[package]]\nname = "flaskteroids-turbo"\nversion = "0.1.0"\n'
    )
    return tmp_path


def check_release(root, tag):
    return subprocess.run(
        [sys.executable, str(SCRIPT), tag, "--root", str(root)],
        capture_output=True,
        text=True,
        check=False,
    )


def test_release_tag_matches_the_package_version(release_project):
    result = check_release(release_project, "v0.1.0")
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize("tag", ["0.1.0", "v99.0.0", "v0.1.0rc1"])
def test_release_tags_reject_mismatched_or_unstable_versions(release_project, tag):
    result = check_release(release_project, tag)
    assert result.returncode != 0
    assert "Expected stable release tag" in result.stderr


def test_release_requires_a_matching_lockfile_version(release_project):
    lock = release_project / "uv.lock"
    lock.write_text(lock.read_text().replace('version = "0.1.0"', 'version = "0.2.0"'))
    result = check_release(release_project, "v0.1.0")
    assert result.returncode != 0
    assert "Project version and lockfile differ" in result.stderr
