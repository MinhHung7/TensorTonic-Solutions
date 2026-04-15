import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data=data)

    rows_before = df.shape[0]
    new_df = df.drop_duplicates(keep='first')

    rows_after = new_df.shape[0]

    return [rows_before, rows_after, new_df.to_dict('list')]
    pass