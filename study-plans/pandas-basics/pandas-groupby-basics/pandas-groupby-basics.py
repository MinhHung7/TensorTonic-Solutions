import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df = pd.DataFrame(data=data)

    sum_df = df.groupby(group_col)[value_col].sum().to_dict()
    mean_df = df.groupby(group_col)[value_col].mean().to_dict()
    count_df = df.groupby(group_col)[value_col].count().to_dict()
    
    return {
        'sum': sum_df,
        'mean': mean_df,
        'count': count_df
    } 

    pass