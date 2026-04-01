import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    predictions = np.array(predictions)
    predictions = predictions.T

    ans = []

    for sample in predictions:
        frequencies = np.unique(sample, return_counts = True)
        ans.append(frequencies[0][np.argmax(frequencies[1])])
        
    return ans