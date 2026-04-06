import numpy as np
import math
from scipy import special

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.array(x)
    return 0.5 * x * (1 + special.erf(x / math.sqrt(2)))
    pass