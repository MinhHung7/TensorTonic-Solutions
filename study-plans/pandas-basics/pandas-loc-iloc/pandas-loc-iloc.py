import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)

    res = [
        df.iloc[row, col],
        df.iloc[row, :].tolist(),
        df.iloc[:, col].tolist()
    ]

    return res
    pass