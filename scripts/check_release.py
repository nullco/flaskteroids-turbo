"""Validate a stable release tag against project and lockfile metadata."""

import argparse
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(tag, root):
    project = tomllib.loads((root / "pyproject.toml").read_text())["project"]
    expected = f"v{project['version']}"
    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag) or tag != expected:
        raise ValueError(f"Expected stable release tag {expected}, got {tag!r}")
    lock = tomllib.loads((root / "uv.lock").read_text())
    package = next(
        package for package in lock["package"] if package["name"] == project["name"]
    )
    if package["version"] != project["version"]:
        raise ValueError("Project version and lockfile differ; run uv lock")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tag")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        validate(args.tag, args.root)
    except ValueError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
