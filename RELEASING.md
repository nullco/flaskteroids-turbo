# Releasing

This asset-only package can be published independently of Flaskteroids.
Its Python package version is independent of the bundled JavaScript version.

## One-time setup

Create the `nullco/flaskteroids-turbo` GitHub repository and a `pypi` environment.
Configure a PyPI pending trusted publisher with:

- Project: `flaskteroids-turbo`
- Owner: `nullco`
- Repository: `flaskteroids-turbo`
- Workflow: `publish.yml`
- Environment: `pypi`

## Each release

1. Update `pyproject.toml`, `CHANGELOG.md`, and `uv.lock`.
2. For runtime updates, replace the upstream ESM asset and update its
   license/provenance. Verify upstream tarball integrity.
3. Run locked tests, lint, formatting, `uv build`, and
   `uvx twine check --strict dist/*`.
4. Publish a GitHub release tagged `vX.Y.Z`. The workflow validates metadata,
   tests and builds the package, and uploads the artifacts through trusted publishing.

No Flaskteroids checkout or release is required. Published versions are immutable.
