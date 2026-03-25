from pathlib import Path

THEME_DIR = Path(__file__).parent.parent / "mkdocs_dracula_theme"
CSS_SOURCE = Path(__file__).parent.parent / "template" / "assets" / "css" / "mkdocs.css"
CSS_MIN = THEME_DIR / "assets" / "css" / "mkdocs.min.css"
