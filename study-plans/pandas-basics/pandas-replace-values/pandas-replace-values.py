import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """ 
    df = pd.DataFrame(data=data)

    counts = int((df[column] == old_val).sum())
    df[column] = df[column].replace(to_replace=old_val, value=new_val)

    return {
        'data': df.to_dict('list'),
        'count': counts
    }
    pass