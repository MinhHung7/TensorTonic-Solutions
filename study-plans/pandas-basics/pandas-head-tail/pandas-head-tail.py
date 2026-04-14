import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    df = pd.DataFrame(data)

    df_head = {}
    df_tail = {}

    for col in df.head(n).columns:
        df_head[col] = df.head(n)[col].tolist()
    
    for col in df.tail(n).columns:
        df_tail[col] = df.tail(n)[col].tolist()

    return { 
        'head': df_head,
        'tail': df_tail
    }
    pass