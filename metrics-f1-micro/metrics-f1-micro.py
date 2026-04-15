import numpy as np

def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    unique_classes = np.unique(y_true, return_counts = True)[0]
    
    tp = sum(yt == yp for yt, yp in zip(y_true, y_pred))
    fp = sum(yt != yp for yt, yp in zip(y_true, y_pred))
    fn = fp

    if tp == 0 or tp + fp == 0:
        return 0.0

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    f1_micro = 2 * (precision * recall) / (precision + recall)

    return f1_micro

    pass