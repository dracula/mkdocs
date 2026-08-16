import unittest

import pytest


class TestMinifiedCSSFormat(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_css(self, css_min):
        self.css_min = css_min

    def _admonition_section(self):
        content = self.css_min.read_text()
        start = content.find(".admonition{")

        self.assertNotEqual(
            start, -1, "Admonition CSS not found in minified file"
        )

        return content[start:]

    def test_admonition_section_has_no_comments(self):
        """The admonition block in mkdocs.min.css must not contain CSS comments."""
        self.assertNotIn("/*", self._admonition_section())

    def test_admonition_section_has_no_indentation(self):
        """The admonition block in mkdocs.min.css must not contain indented lines."""
        self.assertNotIn("\n    ", self._admonition_section())

    def test_admonition_uses_shorthand_values(self):
        """Minified CSS should use shorthand values (e.g. .5rem not 0.5rem)."""
        admonition_section = self._admonition_section()

        self.assertNotIn("0.5rem", admonition_section)
        self.assertNotIn("0.75rem", admonition_section)
