"""Small, explicit Google Earth Engine helpers for workshop notebooks."""

from __future__ import annotations

import os

from .config import country_settings


def initialise_earth_engine(project: str | None = None):
    """Authenticate when required and return the Earth Engine module.

    Since November 2024, Earth Engine requires every request to be attached
    to a Google Cloud project. Pass ``project`` explicitly or set the
    ``EE_PROJECT`` environment variable (the notebook's Section 1 does this).
    """
    project = project or os.environ.get("EE_PROJECT")
    if not project:
        raise RuntimeError(
            "Earth Engine needs a Cloud project. Set EE_PROJECT in Section 1 "
            "of the notebook to a project where you have enabled the Earth "
            "Engine API (see https://console.cloud.google.com/)."
        )
    import ee

    try:
        ee.Initialize(project=project)
    except Exception:
        ee.Authenticate()
        ee.Initialize(project=project)
    return ee


def country_boundary(ee, country: str):
    """Return the GAUL level-0 boundary for a selected workshop country."""
    country_settings(country)  # Validate before making a remote request.
    return ee.FeatureCollection("FAO/GAUL/2015/level0").filter(
        ee.Filter.eq("ADM0_NAME", country)
    )
