import numpy as np

def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points = np.array(points)
    centroids = np.array(centroids)

    assigns = []
    for point in points:
        dists = np.sum((point - centroids) ** 2, axis=1)
        assigns.append(int(np.argmin(dists)))

    return assigns