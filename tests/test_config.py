import unittest

import pytest
import yaml


class TestThemeConfig(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_theme_dir(self, theme_dir):
        self.theme_dir = theme_dir

    def setUp(self):
        config_path = self.theme_dir / "mkdocs_theme.yml"
        self.config = yaml.safe_load(config_path.read_text())

    def test_config_file_exists(self):
        self.assertTrue((self.theme_dir / "mkdocs_theme.yml").exists())

    def test_static_templates_includes_404(self):
        self.assertIn("404.html", self.config["static_templates"])

    def test_locale_is_english(self):
        self.assertEqual(self.config["locale"], "en")

    def test_search_page_is_enabled(self):
        self.assertTrue(self.config["include_search_page"])
