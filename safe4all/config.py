"""Country settings shared by the SAFE4ALL workshop notebooks."""

COUNTRIES = {
    "Kenya": {"iso3": "KEN", "center": (0.2, 37.9), "zoom": 6, "bbox": (33.5, -4.8, 42.1, 5.5)},
    "Zimbabwe": {"iso3": "ZWE", "center": (-19.0, 29.2), "zoom": 6, "bbox": (25.0, -22.5, 33.0, -15.0)},
    "Ghana": {"iso3": "GHA", "center": (7.9, -1.0), "zoom": 6, "bbox": (-3.5, 4.5, 1.5, 11.5)},
}


def country_settings(country: str) -> dict:
    """Return workshop settings for a supported country."""
    try:
        return COUNTRIES[country].copy()
    except KeyError as error:
        supported = ", ".join(COUNTRIES)
        raise ValueError(f"Unsupported country: {country}. Choose one of: {supported}.") from error
