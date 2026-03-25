import textwrap
import pytest
from pathlib import Path


THEME_DIR = Path(__file__).parent.parent / "mkdocs_dracula_theme"
CSS_SOURCE = Path(__file__).parent.parent / "template" / "assets" / "css" / "mkdocs.css"
CSS_MIN = THEME_DIR / "assets" / "css" / "mkdocs.min.css"


@pytest.fixture()
def docs_dir(tmp_path):
    d = tmp_path / "docs"
    d.mkdir()
    (d / "index.md").write_text("# Home\nHello world.\n")
    return d


@pytest.fixture()
def build_site(tmp_path, docs_dir):
    """Factory: build a minimal MkDocs site and return the index.html content."""
    from mkdocs.config import load_config
    from mkdocs.commands.build import build

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
