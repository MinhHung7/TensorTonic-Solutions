import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)

    d_types = {}

    for col, dtype in df.dtypes.items():
        d_types[col] = str(dtype)

    ans = {
        'rows': df.shape[0],
        'cols': df.shape[1],
        'columns': df.columns.tolist(),
        'dtypes': d_types,
        'total_values': df.shape[0] * df.shape[1]
    }

    return ans

    pass