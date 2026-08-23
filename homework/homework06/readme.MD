# cleaning.py

Utility functions for basic DataFrame cleaning: filling missing values, dropping incomplete rows, and normalizing numeric columns. All functions return a **new** DataFrame rather than modifying the input in place, so you always reassign the result (e.g. `df = cleaning.fill_missing_median(df, ...)`).

## Functions

### `fill_missing_median(data, columns=None)`

Fills missing values with the median of each column.

- **`data`** — the input DataFrame.
- **`columns`** *(optional)* — list of column names to fill. If omitted, all numeric columns are filled.
- **Returns** — a new DataFrame with missing values replaced.

```python
df = cleaning.fill_missing_median(df, ['col1', 'col2'])
```

### `drop_missing(data, threshold=None)`

Drops rows with missing values.

- **`data`** — the input DataFrame.
- **`threshold`** *(optional)* — a value between 0 and 1. A row is kept only if at least that fraction of its columns are non-null (e.g. `threshold=0.5` keeps rows that are at least half filled in). If omitted, any row with even one missing value is dropped.
- **Returns** — a new DataFrame with qualifying rows removed.

```python
df = cleaning.drop_missing(df, threshold=0.5)
```

### `normalize_data(data, columns=None)`

Normalizes columns using Min-Max scaling, rescaling values into a `[0, 1]` range: `(x - min) / (max - min)`.

- **`data`** — the input DataFrame.
- **`columns`** *(optional)* — list of column names to normalize. If omitted, all numeric columns are normalized.
- **Returns** — a new DataFrame with the specified columns rescaled.
