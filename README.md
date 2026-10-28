# Flaskteroids Turbo

The upstream Turbo **8.0.23** ESM runtime, packaged for Python applications with
its license and provenance. This package has **no runtime dependencies**.
All server-side integration remains in Flaskteroids.

New browser applications include this package. To add it to an existing app:

```sh
uv add 'flaskteroids-turbo>=0.1.0,<0.2'
bin/flask turbo:install
```

To upgrade:

```sh
uv lock --upgrade-package flaskteroids-turbo
uv sync --locked
bin/flask assets:precompile
```

The package exposes `turbo.js` to the asset pipeline. Applications load it through
import maps without copying or downloading it at generation or startup.

## Development

```sh
uv sync --locked --dev
uv run pytest
uv run ruff check .
uv run ruff format --check .
```

See [RELEASING.md](RELEASING.md) for publishing and
[asset provenance](flaskteroids_turbo/assets/README.md) for upstream details.
