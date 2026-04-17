import numpy as np
from math import sqrt

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    a = np.array(a)
    b = np.array(b)
    
    if np.all(a == 0) or np.all(b == 0):
        return 0.0

    return (a @ b) / (sqrt(sum(a**2)) * sqrt(sum(b**2))) 
    pass