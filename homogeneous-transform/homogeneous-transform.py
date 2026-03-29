import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    T = np.array(T)
    points = np.array(points)

    if points.ndim == 1:
        points = points.reshape(1, -1)

    one_row = np.ones((points.shape[0], 1))
    p_h = np.hstack([points, one_row]).T

    p_h_comma = T @ p_h
        
    p_h_comma = p_h_comma[:3, :].T

    if p_h_comma.shape[0] == 1:
        return p_h_comma.flatten()
    
    return p_h_comma
    pass