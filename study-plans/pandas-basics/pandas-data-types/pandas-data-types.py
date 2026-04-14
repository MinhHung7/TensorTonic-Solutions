import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """

    df = pd.DataFrame(data)

    d_types = {}

    d_types =  df.dtypes.astype(str).to_dict()
    
    ans = {
        'dtypes': d_types,
        'type_counts': df.dtypes.astype(str).value_counts().to_dict(),
        'num_columns': len(df.columns)
    }

    return ans
    pass