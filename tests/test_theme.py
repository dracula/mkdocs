from pathlib import Path

import mkdocs_dracula_theme

THEME_DIR = Path(mkdocs_dracula_theme.__file__).parent


def test_version_is_set():
    assert mkdocs_dracula_theme.__version__


def test_theme_config_exists():
    assert (THEME_DIR / "mkdocs_theme.yml").exists()


def test_theme_templates_exist():
    for template in ("main.html", "base.html", "404.html"):
        assert (THEME_DIR / template).exists()
