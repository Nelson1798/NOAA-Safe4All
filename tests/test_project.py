import os
import unittest
from unittest import mock

from safe4all.config import COUNTRIES, country_settings
from safe4all.gee import initialise_earth_engine
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

    def test_earth_engine_requires_a_project(self):
        # Earth Engine has required every request to name a Cloud project
        # since November 2024; fail fast with a clear message instead of a
        # cryptic error from the `ee` library.
        with mock.patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "EE_PROJECT"):
                initialise_earth_engine()


if __name__ == "__main__":
    unittest.main()
