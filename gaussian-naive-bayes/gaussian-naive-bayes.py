import numpy as np
from math import pi
def gaussian_naive_bayes(X_train, y_train, X_test):
    """
    Predict class labels for test samples using Gaussian Naive Bayes.
    """
    # Write code here
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    X_test = np.array(X_test)

    unique_class = np.unique(y_train)
    p = {}
    mean = {}
    variance = {}

    eps = 1e-9

    n_samples, n_features = X_train.shape

    for c in unique_class:
        samples_with_class_c = np.array([X_train[i] for i in range(len(X_train)) if y_train[i] == c ])

        p[c] = len(samples_with_class_c) / n_samples

        mean[c] = np.mean(samples_with_class_c, axis=0)
        variance[c] = np.var(samples_with_class_c, axis=0) + eps

    y_preds = []

    for t in X_test:
        max_log_c_x = -np.inf
        c_predict = unique_class[0]

        for c in unique_class:
            t = np.array(t)
            log_c_x = np.log(p[c]) + sum(-0.5 * np.log(2*pi*variance[c]) - ((t - mean[c])**2) / (2 * variance[c]))
            if log_c_x > max_log_c_x:
                c_predict = c
                max_log_c_x = log_c_x

        y_preds.append(c_predict)        
    return y_preds