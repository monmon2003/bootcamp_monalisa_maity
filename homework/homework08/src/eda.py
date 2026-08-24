import pandas as pd
import numpy as np
from scipy.stats import skew, kurtosis

def eda_summary(df: pd.DataFrame, numeric_cols=None):
    """Return a dict with quick profiling stats and basic missingness.
    numeric_cols: optional list to limit numeric profiling.
    """
    if numeric_cols is None:
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    out = {}
    out['shape'] = df.shape
    out['dtypes'] = df.dtypes.to_dict()
    out['missing'] = df.isna().sum().to_dict()
    profile = df[numeric_cols].describe().T
    profile['skew'] = [skew(df[c].dropna()) for c in profile.index]
    profile['kurtosis'] = [kurtosis(df[c].dropna()) for c in profile.index]
    out['numeric_profile'] = profile
    return out

def flag_columns(df, missing_threshold=0.5, variance_threshold=0.01, dominance_threshold=0.9):
    flagged_columns = []
    
    for col in df.columns:
        # Check for missingness
        missing_ratio = df[col].isna().mean()
        if missing_ratio > missing_threshold:
            flagged_columns.append((col, 'High Missingness', missing_ratio))
            continue
        
        # Check for near-zero variance (only for numeric columns)
        if pd.api.types.is_numeric_dtype(df[col]):
            variance = df[col].var()
            if variance < variance_threshold:
                flagged_columns.append((col, 'Near-Zero Variance', variance))
                continue
        
        # Check for dominance (only for categorical columns)
        if pd.api.types.is_categorical_dtype(df[col]) or pd.api.types.is_object_dtype(df[col]):
            top_category_ratio = df[col].value_counts(normalize=True).iloc[0]
            if top_category_ratio > dominance_threshold:
                flagged_columns.append((col, 'Dominant Category', top_category_ratio))
    
    return flagged_columns