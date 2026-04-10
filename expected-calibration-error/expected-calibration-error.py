import numpy as np
from math import ceil

def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    bins = [[] for _ in range(n_bins)]
    range_value = (1 - 0) / n_bins

    for true_value, pred_value in zip(y_true, y_pred):
        index = int(pred_value // range_value)
        if pred_value == 1.0:
            index = -1

        bins[index].append((true_value, pred_value))
    
    ece = 0

    for m in range(n_bins):
        if not bins[m]:
            continue
        
        true_average = sum(true_value for true_value, pred_value in bins[m]) / len(bins[m])
        pred_average = sum(pred_value for true_value, pred_value in bins[m]) / len(bins[m])
    
        ece += (len(bins[m]) / len(y_true)) * abs(true_average - pred_average)
    return ece

    pass