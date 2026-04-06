import numpy as np

def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    x = np.array(x)

    return [i if i > 0 else alpha * (np.exp(i) - 1) for i in x]