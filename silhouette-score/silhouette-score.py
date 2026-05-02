import numpy as np
from math import sqrt

def distance(X, Y):
    X = np.array(X)
    Y = np.array(Y)

    return sqrt(np.sum((X - Y)**2))

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    X = np.array(X)
    distance_map = {}

    intra_cluster_distance = {}
    inter_cluster_distance = {}
    silhouette_score = {}

    for i, point in enumerate(X):
        # Xet A(0, 0) with label 0
        # Calculate the intra-cluster distance
        intra_points_list = []
        for j, other_point in enumerate(X):
            if np.all(point == other_point) or labels[i] != labels[j]:
                continue
            
            if (tuple(point), tuple(other_point)) not in distance_map:
                distance_map[(tuple(point), tuple(other_point))] = distance(point, other_point)
                distance_map[(tuple(other_point), tuple(point))] = distance_map[(tuple(point), tuple(other_point))]
            
            intra_points_list.append(distance_map[(tuple(point), tuple(other_point))])
        intra_cluster_distance[(tuple(point))] = np.mean(intra_points_list)

        # Calculate the inter-cluster distance
        inter_points_list = []
        for label in labels:
            # Xet label = 1
            if label == labels[i]:
                continue
            
            inter_distance = []
            for j, other_point in enumerate(X):
                if label != labels[j]:
                    continue
                
                if (tuple(point), tuple(other_point)) not in distance_map:
                    distance_map[(tuple(point), tuple(other_point))] = distance(point, other_point)
                    distance_map[(tuple(other_point), tuple(point))] = distance_map[(tuple(point), tuple(other_point))]
                
                inter_distance.append(distance_map[(tuple(point), tuple(other_point))])
            
            if (tuple(point)) not in inter_cluster_distance:
                inter_cluster_distance[(tuple(point))] = np.mean(inter_distance)
            else:
                inter_cluster_distance[(tuple(point))] = min(inter_cluster_distance[(tuple(point))], np.mean(inter_distance))

        silhouette_score[(tuple(point))] = (inter_cluster_distance[(tuple(point))] - intra_cluster_distance[(tuple(point))]) / max(inter_cluster_distance[(tuple(point))], intra_cluster_distance[(tuple(point))])
    
    return np.mean(list(silhouette_score.values()))