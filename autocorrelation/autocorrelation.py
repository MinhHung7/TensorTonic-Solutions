import numpy as np

def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    # Write code here
    series = np.array(series)
    y_mean = np.mean(series)

    variance = np.sum((series - y_mean)**2)

    ans = []
    for k in range (0, max_lag + 1):
        if k == 0:
            ans.append(1.0)
        else:
            if variance == 0:
                ans.append(0.0)
            else:
                p_k = np.sum((series[k:] - y_mean) * (series[:-k] - y_mean)) / variance
                ans.append(p_k)

    return ans