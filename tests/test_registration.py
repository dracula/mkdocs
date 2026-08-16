import importlib.metadata
import unittest


class TestThemeRegistration(unittest.TestCase):
    def test_dracula_theme_is_registered_as_mkdocs_theme(self):
        entry_points = importlib.metadata.entry_points(group="mkdocs.themes")
        names = [ep.name for ep in entry_points]

        self.assertIn("dracula", names)

    def test_dracula_entry_point_resolves_to_theme_package(self):
        entry_points = importlib.metadata.entry_points(
            group="mkdocs.themes", name="dracula"
        )
        (entry_point,) = entry_points

        self.assertEqual(entry_point.value, "mkdocs_dracula_theme")
