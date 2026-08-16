import unittest

import mkdocs_dracula_theme


class TestPackageMetadata(unittest.TestCase):
    def test_version_is_a_non_empty_string(self):
        self.assertIsInstance(mkdocs_dracula_theme.__version__, str)
        self.assertTrue(mkdocs_dracula_theme.__version__)

    def test_author_is_set(self):
        self.assertIsInstance(mkdocs_dracula_theme.__author__, str)
        self.assertIn("Fernando Celmer", mkdocs_dracula_theme.__author__)

    def test_copyright_mentions_mit_license(self):
        self.assertIn("MIT License", mkdocs_dracula_theme.__copyright__)
