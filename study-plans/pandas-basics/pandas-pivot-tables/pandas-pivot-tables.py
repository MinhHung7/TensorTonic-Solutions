import pandas as pd

def create_pivot(data, index, columns, values, aggfunc):
    """
    Returns: nested dict {column_value: {index_value: agg_result}}
    """
    df = pd.DataFrame(data=data)
    df = df.pivot_table(values=values, index=index, columns=columns, aggfunc=aggfunc, fill_value=0)

    return df.to_dict()
    pass