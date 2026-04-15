import pandas as pd

def multi_agg(data, group_col, value_col, funcs):
    """
    Returns: dict mapping function name to {group: value} dict
    """
    df = pd.DataFrame(data)

    ans = {}

    for func in funcs:
        ans[func] = df.groupby(group_col)[value_col].agg(func).to_dict()
    
    return ans
    pass