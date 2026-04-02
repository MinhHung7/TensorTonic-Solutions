import numpy as np

def impute_missing(X, strategy='mean'):
    """
    Fill NaN values in each feature column using column mean or median.
    """
    # Write code here
    X = np.array(X)
    X_copy = np.array(X)

    if np.ndim(X_copy) == 1 or X_copy.shape[1] == 1:
        X_copy = X_copy.reshape(1, -1)
    else:
        X_copy = X_copy.T

    X_copy = X_copy.astype(float)
    
    for row in range(X_copy.shape[0]):
        if strategy == 'mean':
            if np.isnan(X_copy[row]).all():
                mean_value = 0.0
            else:
                mean_value = np.nanmean(X_copy[row])
            X_copy[row] = np.where(np.isnan(X_copy[row]), mean_value, X_copy[row]).astype(float)
        elif strategy == 'median':
            if np.isnan(X_copy[row]).all():
                median_value = 0.0
            else:
                median_value = np.nanmedian(X_copy[row])
            X_copy[row] = np.where(np.isnan(X_copy[row]), median_value, X_copy[row]).astype(float)
    
    if np.ndim(X) == 1:
        return X_copy.flatten()
    else:
        return X_copy.T
    pass