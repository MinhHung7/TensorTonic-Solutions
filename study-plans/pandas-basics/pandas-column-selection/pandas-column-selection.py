import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)

    res = {
        'values': df[column].tolist(),
        'length': len(df[column])
    }

    return res    
    pass