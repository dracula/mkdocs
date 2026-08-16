import unittest

import pytest


class TestThemeTemplates(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_theme_dir(self, theme_dir):
        self.theme_dir = theme_dir

    def test_root_templates_exist(self):
        for template in (
            "base.html",
            "main.html",
            "404.html",
            "search.html",
            "searchbox.html",
        ):
            with self.subTest(template=template):
                self.assertTrue((self.theme_dir / template).is_file())

    def test_module_templates_exist(self):
        for template in (
            "content.html",
            "dropdown-menu.html",
            "footer.html",
            "header.html",
            "menu.html",
            "preview.html",
            "sidebar.html",
            "source.html",
        ):
            with self.subTest(template=template):
                self.assertTrue(
                    (self.theme_dir / "modules" / template).is_file()
                )
