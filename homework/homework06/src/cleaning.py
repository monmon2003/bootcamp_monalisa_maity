def fill_missing_median(data, columns=None):
    
    data = data.copy()
    if columns is not None:
        data[columns] = data[columns].fillna(data[columns].median())
    else:
        data = data.fillna(data.median(numeric_only=True))
    return data


def drop_missing(data, threshold=None):

    data = data.copy()
    if threshold is not None:
        min_non_na = int(threshold * data.shape[1])
        return data.dropna(thresh=min_non_na)
    return data.dropna()


def normalize_data(data, columns=None):
    
    data = data.copy()
    cols = columns if columns is not None else data.select_dtypes(include='number').columns
    data[cols] = (data[cols] - data[cols].min()) / (data[cols].max() - data[cols].min())
    return data