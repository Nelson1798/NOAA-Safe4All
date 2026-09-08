import unittest

from safe4all.config import COUNTRIES, country_settings
from safe4all.validation import rainfall_metrics


class ProjectTests(unittest.TestCase):
    def test_supported_countries_have_map_settings(self):
        self.assertEqual(set(COUNTRIES), {"Kenya", "Zimbabwe", "Ghana"})
        for country in COUNTRIES:
            settings = country_settings(country)
            self.assertIn("iso3", settings)
            self.assertIn("center", settings)

    def test_unsupported_country_has_clear_error(self):
        with self.assertRaisesRegex(ValueError, "Unsupported country"):
            country_settings("Uganda")

    def test_rainfall_metrics(self):
        metrics = rainfall_metrics(observed=[1.0, 2.0, 3.0], estimated=[1.0, 3.0, 5.0])
        self.assertEqual(metrics['n'], 3.0)
        self.assertGreater(metrics['rmse_mm'], 0)


if __name__ == "__main__":
    unittest.main()
