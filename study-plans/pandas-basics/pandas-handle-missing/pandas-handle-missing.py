import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    df = pd.DataFrame(data)

    null_counts = df.isnull().sum().to_dict()

    cleaned_data = df.fillna(fill_value).to_dict('list')
    ans = {
        'null_counts': null_counts,
        'cleaned_data': cleaned_data
    }

    return ans
    pass