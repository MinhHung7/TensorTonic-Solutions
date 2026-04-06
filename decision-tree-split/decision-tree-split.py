import numpy as np

def decision_tree_split(X, y):
    """
    Find the best feature and threshold to split the data.
    """
    # Write code here
    X = np.array(X)
    y = np.array(y)

    n_samples, n_features = X.shape

    unique_label_counts = np.unique(y, return_counts = True)[1]

    sum_proportion = np.sum((unique_label_counts / n_samples) ** 2)
    gini_S = 1 - sum_proportion

    ans = []
    max_gain_information = 0

    for j in range(n_features):
        feature_values = np.array(sorted(X[:, j]))
        thresholds = (feature_values[:-1] + feature_values[1:]) / 2
        
        for t in thresholds:
            left_idx = np.where(X[:, j] < t)[0]
            right_idx = np.where(X[:, j] >= t)[0]
            
            data_left = X[left_idx]
            data_right = X[right_idx]

            S_L = len(data_left)
            S_R = len(data_right)
            S = S_L + S_R

            left_unique_label_counts = np.unique(y[left_idx], return_counts = True)[1]
            right_unique_label_counts = np.unique(y[right_idx], return_counts = True)[1]

            left_sum_proportion = np.sum((left_unique_label_counts / len(y[left_idx])) ** 2)
            right_sum_proportion = np.sum((right_unique_label_counts / len(y[right_idx])) ** 2)

            gini_left = 1 - left_sum_proportion
            gini_right = 1 - right_sum_proportion

            gini_split = (S_L / S) * gini_left + (S_R / S) * gini_right

            information_gain = gini_S - gini_split

            if max_gain_information < information_gain:
                ans = [j, t]
                max_gain_information = information_gain
            elif max_gain_information == information_gain:
                if ans != [] and ans[0] > j:
                    ans[0] = j
                elif ans != [] and ans[1] > t:
                    ans[1] = t
            
    return ans
