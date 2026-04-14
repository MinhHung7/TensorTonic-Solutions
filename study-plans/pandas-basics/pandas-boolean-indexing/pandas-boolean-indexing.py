import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)

    ans = {
        'filtered_data': df[df[column] > threshold].to_dict("list"),
        'count': len(df[df[column] > threshold])
    }
    return ans
    pass