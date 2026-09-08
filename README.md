# SAFE4ALL Climate Risk Assessment Workshop

Hands-on Jupyter notebooks for assessing flood and drought risk in **Kenya**,
**Zimbabwe**, and **Ghana**. The exercises use Google Earth Engine to analyse
CHIRPS rainfall and administrative boundaries, and are designed for both
Google Colab and local Jupyter/Anaconda environments.

## Workshop flow

Run `SAFE4ALL_Climate_Risk_Assessment_Workshop.ipynb` from top to bottom. It is
a single, progressive notebook: configuration, data access and caching, TAHMO
station QC, product validation, TAMSAT drought context, flood screening, and
drought screening all use the same country and dates.

## Data strategy

- **TAHMO stations:** local observations, station QC, and product validation.
- **TAMSAT:** primary Africa-focused rainfall and soil-moisture source for
  drought monitoring and long-term risk context.
- **CHIRPS:** independent long-term rainfall comparator available in Earth
  Engine.
- **IMERG:** half-hourly event-rainfall context for flood case studies.

The project caches every approved live extract. In Colab, set
`SAFE4ALL_SHARED_DRIVE` to the exact Shared Drive name before starting; the
default is `SAFE4ALL-workshop`. If it cannot be found, the notebooks fall back
to a workshop folder in the participant's MyDrive. Local Jupyter uses
`.safe4all-cache/`.

## Local Jupyter / Anaconda setup

```bash
conda env create -f environment.yml
conda activate safe4all-climate-risk
python -m ipykernel install --user --name safe4all-climate-risk --display-name "Python (SAFE4ALL)"
jupyter lab
```

Open Jupyter from this project folder and select the **Python (SAFE4ALL)**
kernel. To verify the local installation, run:

```bash
python -m unittest tests/test_project.py
```

## Google Earth Engine access

The first notebook will prompt you to authenticate Earth Engine if needed. A
Google account with Earth Engine access is required to run the data-analysis
cells. The project does not store credentials or API keys.

## Interpretation note

The flood and drought maps are **screening products**, not operational
forecasts or disaster warnings. They identify relative climate hazard from
rainfall indicators and should be combined with local exposure, vulnerability,
river, topography, and impact data before making decisions.
