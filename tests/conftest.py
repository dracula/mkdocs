from pathlib import Path

import pytest

import mkdocs_dracula_theme


@pytest.fixture(scope="session")
def theme_dir():
    return Path(mkdocs_dracula_theme.__file__).parent
