"""Small, explicit Google Earth Engine helpers for workshop notebooks."""

from __future__ import annotations

from .config import country_settings


def initialise_earth_engine():
    """Authenticate when required and return the Earth Engine module."""
    import ee

    try:
        ee.Initialize()
    except Exception:
        ee.Authenticate()
        ee.Initialize()
    return ee


def country_boundary(ee, country: str):
    """Return the GAUL level-0 boundary for a selected workshop country."""
    country_settings(country)  # Validate before making a remote request.
    return ee.FeatureCollection("FAO/GAUL/2015/level0").filter(
        ee.Filter.eq("ADM0_NAME", country)
    )
