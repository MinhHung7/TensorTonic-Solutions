from numpy.lib._shape_base_impl import apply_along_axis
import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    if x.ndim == 1:
        max_x = np.max(x)
        return np.exp(x - max_x) / np.sum(np.exp(x - max_x))
    elif x.ndim == 2:
        max_x = np.max(x, axis=1, keepdims=True)
        return np.exp(x - max_x) / np.sum(np.exp(x - max_x), axis=1, keepdims=True)
    else:
        raise ValueError("Input must be a 1D or 2D NumPy array")
    
    pass