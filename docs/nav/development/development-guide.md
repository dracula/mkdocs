# Development Guide

## How to test the local package?

#### Virtual environment

- Create your virtual environment.

```bash
python -m venv venv
```

#### Environment activation

- Activate the virtual environment.

```bash
source venv/bin/activate
```

#### Install Poetry

- Install Poetry for dependency management and building.

```bash
pip install poetry
```

Or using the official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Install dependencies with Poetry

- Install project dependencies using Poetry.

```bash
poetry install
```

This will install:
- `mkdocs` (>=1.6.1,<2.0.0) - Main dependency
- `build` (^1.3.0) - Development dependency for building packages

#### Development

- Make your changes as desired in the `./mkdocs_dracula_theme` folder. You can enjoy and change whatever you want, please have fun.

```bash
ls mkdocs_dracula_theme
```

The `poetry install` command installs the package in editable mode, so your changes will be reflected immediately without needing to rebuild.

#### Build package (optional)

- If you want to build the distribution package:

```bash
poetry build
```

This creates distribution files in the `dist/` directory.

#### Test

- Run the following command to start the development server.

```bash
poetry run mkdocs serve
```

Or if you're already in the Poetry environment:

```bash
mkdocs serve
```

#### View Template

- Now you can access the [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Commit Style

- ⚙️ FEATURE
- 📝 PEP8
- 📌 ISSUE
- 🪲 BUG
- 📘 DOCS
- 📦 PyPI
- ❤️️ TEST
- ⬆️ CI/CD
- ⚠️ SECURITY
