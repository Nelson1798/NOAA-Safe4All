# SAFE4ALL Climate Risk Assessment Workshop

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Nelson1798/NOAA-Safe4All/blob/main/SAFE4ALL_Climate_Risk_Assessment_Workshop.ipynb)

Hands-on Jupyter notebook for assessing flood and drought risk in **Kenya**,
**Zimbabwe**, and **Ghana**. The exercise uses Google Earth Engine to analyse
CHIRPS/IMERG rainfall and administrative boundaries, TAHMO station
observations for ground validation, and TAMSAT for drought context.

## Run it — pick one

**Google Colab (default, no local setup):** click the badge above, or open
<https://colab.research.google.com/github/Nelson1798/NOAA-Safe4All/blob/main/SAFE4ALL_Climate_Risk_Assessment_Workshop.ipynb>,
then **Runtime -> Run all**. Section 0 of the notebook clones this repo into
the Colab runtime and installs anything missing — nothing else to configure.

**Local Jupyter or Anaconda:** clone this repo and run the notebook from its
root folder with **Run -> Run All Cells**. Section 0 detects that the
`safe4all` package is already available locally and skips the Colab-only
steps; any missing Python packages are installed automatically. A conda
environment file is provided if you prefer to pre-install everything instead:

```bash
git clone https://github.com/Nelson1798/NOAA-Safe4All.git
cd NOAA-Safe4All
conda env create -f environment.yml
conda activate safe4all-climate-risk
python -m ipykernel install --user --name safe4all-climate-risk --display-name "Python (SAFE4ALL)"
jupyter lab
```

Open `SAFE4ALL_Climate_Risk_Assessment_Workshop.ipynb` and select the
**Python (SAFE4ALL)** kernel. All three environments (Colab, Jupyter,
Anaconda) run the same notebook and produce the same screening outputs.

To verify a local installation outside the notebook, run:

```bash
python -m unittest tests/test_project.py
```

## Workshop flow

Run `SAFE4ALL_Climate_Risk_Assessment_Workshop.ipynb` from top to bottom. It is
a single, progressive notebook: environment setup, configuration, data access
and caching, TAHMO station QC, product validation, TAMSAT drought context,
flood screening, and drought screening all use the same country and dates.

## Data strategy

- **TAHMO stations:** local observations, station QC, and product validation.
- **TAMSAT:** primary Africa-focused rainfall and soil-moisture source for
  drought monitoring and long-term risk context.
- **CHIRPS:** independent long-term rainfall comparator available in Earth
  Engine.
- **IMERG:** half-hourly event-rainfall context for flood case studies.

The project caches every approved live extract. In Colab, set
`SAFE4ALL_SHARED_DRIVE` in the notebook to the exact Shared Drive name before
starting; the default is `SAFE4ALL-workshop`. If it cannot be found, the
notebook falls back to a workshop folder in the participant's MyDrive. Local
Jupyter/Anaconda use `.safe4all-cache/` inside the project folder.

## Google Earth Engine access

Earth Engine now requires every request to be attached to a Google Cloud
project. Set `EE_PROJECT` in Section 1 of the notebook to a project where the
Earth Engine API is enabled (free to create at
<https://console.cloud.google.com/>). The notebook will prompt you to
authenticate on first use; a Google account with Earth Engine access is
required to run the data-analysis cells. The project does not store
credentials or API keys — TAHMO credentials are requested privately at
runtime with `getpass` and kept only in the current session's memory.

## Interpretation note

The flood and drought maps are **screening products**, not operational
forecasts or disaster warnings. They identify relative climate hazard from
rainfall indicators and should be combined with local exposure, vulnerability,
river, topography, and impact data before making decisions.
