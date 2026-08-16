import textwrap
from pathlib import Path

import pytest

import mkdocs_dracula_theme


@pytest.fixture(scope="session")
def theme_dir():
    return Path(mkdocs_dracula_theme.__file__).parent


@pytest.fixture(scope="session")
def css_source():
    return (
        Path(__file__).parent.parent
        / "template"
        / "assets"
        / "css"
        / "mkdocs.css"
    )


@pytest.fixture(scope="session")
def css_min(theme_dir):
    return theme_dir / "assets" / "css" / "mkdocs.min.css"


@pytest.fixture()
def docs_dir(tmp_path):
    d = tmp_path / "docs"
    d.mkdir()
    (d / "index.md").write_text("# Home\nHello world.\n")
    return d


@pytest.fixture()
def build_site(tmp_path, docs_dir):
    """Factory: build a minimal MkDocs site and return the index.html content."""
    from mkdocs.commands.build import build
    from mkdocs.config import load_config

    def _build(extra_theme_config: str = "") -> str:
        config_text = textwrap.dedent(f"""
            site_name: Test Site
            docs_dir: {docs_dir}
            site_dir: {tmp_path / "site"}
            theme:
              name: dracula
              {extra_theme_config}
        """)
        cfg_path = tmp_path / "mkdocs.yml"
        cfg_path.write_text(config_text)
        cfg = load_config(str(cfg_path))
        build(cfg)
        return (tmp_path / "site" / "index.html").read_text()

    return _build
