import numpy as np

def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    scales = np.array(scales)
    aspect_ratios = np.array(aspect_ratios)

    stride = image_size / feature_size

    # grid center
    cx = (np.arange(feature_size) + 0.5) * stride
    cy = (np.arange(feature_size) + 0.5) * stride

    cx, cy = np.meshgrid(cx, cy)   # (f, f)

    # flatten grid
    cx = cx.reshape(-1)  # (N,)
    cy = cy.reshape(-1)  # (N,)

    # compute w, h for all ratios & scales
    w = (scales[:, None] * np.sqrt(aspect_ratios)).reshape(-1)  # (K,)
    h = (scales[:, None] / np.sqrt(aspect_ratios)).reshape(-1)  # (K,)

    # expand dims for broadcasting
    cx = cx[:, None]  # (N,1)
    cy = cy[:, None]  # (N,1)

    w = w[None, :]    # (1,K)
    h = h[None, :]    # (1,K)

    # compute boxes
    x1 = cx - w / 2
    y1 = cy - h / 2
    x2 = cx + w / 2
    y2 = cy + h / 2

    # reshape to (N*K, 4)
    boxes = np.stack([x1, y1, x2, y2], axis=2).reshape(-1, 4)

    return boxes.tolist()
    # Write code here