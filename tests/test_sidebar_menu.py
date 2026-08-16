import textwrap
import unittest

import pytest


class TestSidebarMenuActiveExpand(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _build_nested_site(self, tmp_path):
        from mkdocs.commands.build import build
        from mkdocs.config import load_config

        docs_dir = tmp_path / "docs"
        docs_dir.mkdir()
        (docs_dir / "index.md").write_text("# Home\n")

        section_a = docs_dir / "section-a"
        section_a.mkdir()
        (section_a / "page-a.md").write_text("# Page A\n")

        section_b = docs_dir / "section-b"
        section_b.mkdir()
        (section_b / "page-b.md").write_text("# Page B\n")

        site_dir = tmp_path / "site"
        config_text = textwrap.dedent(f"""
            site_name: Test Site
            docs_dir: {docs_dir}
            site_dir: {site_dir}
            theme:
              name: dracula
            nav:
              - Home: index.md
              - Section A:
                - section-a/page-a.md
              - Section B:
                - section-b/page-b.md
        """)
        cfg_path = tmp_path / "mkdocs.yml"
        cfg_path.write_text(config_text)
        cfg = load_config(str(cfg_path))
        build(cfg)

        self.active_page_html = (
            site_dir / "section-a" / "page-a" / "index.html"
        ).read_text()

    def test_active_section_collapse_has_show_class(self):
        """The section containing the current page must render `collapse show`."""
        self.assertIn(
            'class="collapse show" id="section-a-collapse"',
            self.active_page_html,
        )

    def test_active_section_toggle_is_aria_expanded(self):
        """The active section's toggle must report aria-expanded=true."""
        self.assertIn(
            'data-bs-target="#section-a-collapse" aria-expanded="true"',
            self.active_page_html,
        )

    def test_inactive_section_collapse_has_no_show_class(self):
        """An unrelated section must stay collapsed."""
        self.assertIn(
            'class="collapse" id="section-b-collapse"', self.active_page_html
        )

    def test_inactive_section_toggle_is_not_aria_expanded(self):
        """An unrelated section's toggle must report aria-expanded=false."""
        self.assertIn(
            'data-bs-target="#section-b-collapse" aria-expanded="false"',
            self.active_page_html,
        )
