import unittest

import pytest


class TestCustomHighlight(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _inject_build_site(self, build_site):
        self.build_site = build_site

    def test_default_highlight_css_is_darcula(self):
        html = self.build_site()

        self.assertIn("assets/css/darcula-highlight.min.css", html)
        self.assertNotIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/styles/",
            html,
        )

    def test_custom_highlight_css_overrides_default(self):
        html = self.build_site("highlight_css: github.min.css")

        self.assertIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/styles/github.min.css",
            html,
        )
        self.assertNotIn("assets/css/darcula-highlight.min.css", html)

    def test_highlightjs_enabled_by_default(self):
        html = self.build_site()

        self.assertIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/highlight.min.js",
            html,
        )

    def test_highlightjs_disabled_omits_script(self):
        html = self.build_site("highlightjs: false")

        self.assertNotIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/highlight.min.js",
            html,
        )

    def test_custom_highlight_js_overrides_default(self):
        html = self.build_site("highlight_js: highlight.pack.min.js")

        self.assertIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/highlight.pack.min.js",
            html,
        )

    def test_hljs_languages_are_included(self):
        html = self.build_site(
            "hljs_languages:\n                - python\n                - go"
        )

        self.assertIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/languages/python.min.js",
            html,
        )
        self.assertIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/languages/go.min.js",
            html,
        )

    def test_no_hljs_languages_by_default(self):
        html = self.build_site()

        self.assertNotIn(
            "cdnjs.cloudflare.com/ajax/libs/highlight.js/10.5.0/languages/",
            html,
        )
