# Homework 05 — Data Storage

## Overview

This homework implements format-aware read/write utilities (`write_df` / `read_df`) that route automatically between CSV and Parquet based on file suffix, and demonstrates saving, reloading, and validating sample data in both formats.

## Folder Structure

```
homework05/
├── data/
│   ├── raw/          # source data saved as CSV
│   │   ├── sample_<timestamp>.csv
│   │   └── util_<timestamp>.csv
│   └── processed/    # cleaned/typed data saved as Parquet
│       ├── sample_<timestamp>.parquet
│       └── util_<timestamp>.parquet
├── .env               # local environment variables (gitignored, not committed)
├── .env.example        # template showing required variable names
└── stage05_data-....ipynb   # notebook with the write_df/read_df implementation and demo
```

Filenames are timestamped (via a `ts()` helper) so repeated runs of the notebook don't overwrite previous outputs — each save produces a new, uniquely named file in both `raw/` and `processed/`.

## Formats Used and Why

- **`data/raw/` → CSV.** Raw data is stored as CSV: plain-text, human-readable, and a safe source-of-truth format. The tradeoff is that CSV has no dtype metadata — columns like `date` come back as strings on reload and must be re-parsed manually (e.g. `pd.read_csv(path, parse_dates=['date'])`).

- **`data/processed/` → Parquet.** Cleaned data is stored as Parquet, which preserves column dtypes natively on reload (no manual re-parsing needed), is more storage-efficient, and loads faster for repeated analysis. Parquet requires an engine (`pyarrow` or `fastparquet`) to be installed — the write/read utilities raise a clear `RuntimeError` with an install hint if neither is available, rather than a raw traceback.


## Environment Variables

`.env` (gitignored, not committed) holds local config — e.g. data directory paths — and `.env.example` is committed as a template showing which variables are required, without real values.

## Validation

After saving, both files are reloaded and checked against the original DataFrame for:
- Matching shape
- Preserved dtypes on critical columns (especially `date`, which requires manual parsing on CSV reload but comes back correctly typed automatically from Parquet)