import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    x = np.array(x)

    if len(x.shape) != 3 and len(x.shape) != 4:
        raise ValueError
    return np.mean(x, axis=(-2, -1))
    pass