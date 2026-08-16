import unittest

import pytest


class TestThemeAssets(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_theme_dir(self, theme_dir):
        self.theme_dir = theme_dir

    def test_css_assets_exist(self):
        css_dir = self.theme_dir / "assets" / "css"
        for asset in (
            "bootstrap.min.css",
            "dracula-ui.min.css",
            "mkdocs.min.css",
        ):
            with self.subTest(asset=asset):
                self.assertTrue((css_dir / asset).is_file())

    def test_js_assets_exist(self):
        js_dir = self.theme_dir / "assets" / "js"
        for asset in ("bootstrap.bundle.min.js", "mkdocs.js"):
            with self.subTest(asset=asset):
                self.assertTrue((js_dir / asset).is_file())

    def test_image_assets_exist(self):
        img_dir = self.theme_dir / "assets" / "img"
        for asset in ("dracula.png", "dracula.svg", "favicon.ico"):
            with self.subTest(asset=asset):
                self.assertTrue((img_dir / asset).is_file())
