# Project Scaffold — Practice

## Description

In this exercise, I practiced setting up a standardized project folder structure — `data/raw/`, `data/processed/`, `notebooks/`, `src/`, `docs/`, `reports/`, and `model/` — to reflect a typical data/finance project layout that separates raw inputs, processed data, exploratory work, source code, documentation, and reporting outputs. Since Git does not track empty folders, I added a `.gitkeep` placeholder file inside each directory so the structure would still be committed and visible in version control even before any real content is added. This scaffold is a dry run for the structure I'll build for real in `project/`, where each folder will actually be populated with data, code, and deliverables tied to my stock price tracker project.

## Structure

```
homework02/
├── data/
│   ├── raw/          # unprocessed source data
│   └── processed/    # cleaned/transformed data
├── notebooks/         # exploratory analysis notebooks
├── src/                # reusable source code / modules
├── docs/               # documentation
├── reports/            # generated reports/summaries
└── model/              # trained models / model artifacts
```