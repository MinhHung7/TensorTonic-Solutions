import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions
    """
    T = scores.shape[-1]

    # Create a causal mask: 1 for allowed positions, 0 for masked (future)
    causal_mask = np.tril(np.ones((T, T), dtype=bool))

    # Broadcast mask to match scores shape
    masked_scores = np.where(causal_mask, scores, mask_value)

    return masked_scores
    pass