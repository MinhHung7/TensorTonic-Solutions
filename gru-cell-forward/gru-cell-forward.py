import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    # Write code here
    x = np.array(x)
    h_prev = np.array(h_prev)

    for key in list(params.keys()):
        params[key] = np.array(params[key])

    D = params["Wz"].shape[0]
    H = params["Wz"].shape[1]
    x, x_was_1d = _as2d(x, D)
    h_prev, h_was_1d = _as2d(h_prev, H)
    
    # Compute the update gate
    update_gate_params = x @ params["Wz"] + h_prev @ params["Uz"] + params["bz"]
    z_t = _sigmoid(update_gate_params)

    # Compute the reset gate
    reset_gate_params = x @ params["Wr"] + h_prev @ params["Ur"] + params["br"]
    r_t = _sigmoid(reset_gate_params)

    # Compute the candidate hidden state
    reset_gate_filter = r_t * h_prev
    candidate_params = x @ params["Wh"] + reset_gate_filter @ params["Uh"] + params["bh"]
    h_t_hat = np.tanh(candidate_params)

    # Compute the final hidden state
    h_t = (1 - z_t) * h_prev + z_t * h_t_hat

    if x_was_1d:
        return h_t.reshape(-1)
    return h_t
    pass