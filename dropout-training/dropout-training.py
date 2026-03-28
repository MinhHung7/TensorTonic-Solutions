import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x)
    rand = rng.random(x.shape) if rng is not None else np.random.random(x.shape)
    mask = (rand < (1 - p)).astype(float)
    pattern = mask / (1 - p)
    return x * pattern, pattern
    pass