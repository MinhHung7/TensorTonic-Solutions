import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)
    df_no_index = df.drop(columns=index_col)
    record_col = [index_col]
    record_col.extend(df_no_index.columns.tolist())

    return [df_no_index.columns.tolist(), record_col]
    pass