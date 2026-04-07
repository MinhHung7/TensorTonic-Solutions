import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    y_left = np.array(y_left)
    y_right = np.array(y_right)

    left_frequent_label = np.unique(y_left, return_counts=True)[1]
    right_frequent_label = np.unique(y_right, return_counts=True)[1]
    
    gini_left = 1 - np.sum((left_frequent_label / np.sum(left_frequent_label)) ** 2)
    gini_right = 1 - np.sum((right_frequent_label / np.sum(right_frequent_label)) ** 2)

    N_L = len(y_left)
    N_R = len(y_right)
    
    N = N_L + N_R

    if N:
        return (N_L / N) * gini_left + (N_R / N) * gini_right
    return 0.0
    pass