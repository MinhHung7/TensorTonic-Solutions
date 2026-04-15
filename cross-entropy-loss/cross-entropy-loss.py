import numpy as np

def cross_entropy_loss(y_true, y_pred):
    """
    Compute average cross-entropy loss for multi-class classification.
    """
    # Write code here
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    N = len(y_true)
    p_true = y_pred[np.arange(N), y_true]

    loss_entropy = -(1.0 / N) * np.sum(np.log(p_true))

    return loss_entropy
    pass