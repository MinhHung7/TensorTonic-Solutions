import numpy as np

def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here

    values = np.array(values)
    w = (np.max(values) - np.min(values)) / num_bins

    if w == 0:
        return [0] * len(values)

    bin = (values - np.min(values)) // w

    return np.minimum(bin, num_bins - 1).tolist()