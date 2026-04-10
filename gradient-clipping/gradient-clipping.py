import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.array(g)
    gradient_norm = np.sqrt(np.sum(g**2))
    
    return g if max_norm <= 0.0 or gradient_norm == 0.0 or gradient_norm <= max_norm else g * max_norm / gradient_norm
    pass