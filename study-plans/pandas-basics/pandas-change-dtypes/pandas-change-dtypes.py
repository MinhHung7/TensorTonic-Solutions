import pandas as pd

def change_dtype(data, column, target_type):
    """
    Returns: list [dtypes_before, dtypes_after] (both dicts)
    """

    df = pd.DataFrame(data=data)

    dtypes_before = {}
    for col, d_type in df.dtypes.items():
        dtypes_before[col] = str(d_type)
    
    df[column] = df[column].astype(target_type)
    dtypes_after = {}

    for col, d_type in df.dtypes.items():
        dtypes_after[col] = str(d_type)
    
    return [dtypes_before, dtypes_after]

    pass