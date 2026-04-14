import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    df = pd.DataFrame(data)

    df_no_index = df.drop(columns=index_col)

    index_values = df[index_col].tolist()
    columns = df_no_index.columns.tolist()
    data = df[columns].to_dict("list")

    return {
        'index_values': index_values,
        'columns': columns,
        'data': data
    }
    pass