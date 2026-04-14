import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    df = pd.DataFrame(data)

    res = {
        "data": data,
        "shape": list(df.shape),
        "columns": df.columns.tolist()
    }

    return res
    pass