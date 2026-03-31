import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y) == 0:
        return 0.0

    frequencies = np.unique(y, return_counts = True)[1]

    p_i = frequencies / len(y)
    
    return - np.sum(p_i * np.log2(p_i))
    pass