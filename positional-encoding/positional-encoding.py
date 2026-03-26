import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pos = np.arange(seq_len)[:, None]

    div_term = base ** ((2 * (np.arange(d_model) // 2)) / d_model)
    angles = pos / div_term

    ans = np.zeros((seq_len, d_model))
    ans[:, 0::2] = np.sin(angles[:, 0::2])
    ans[:, 1::2] = np.cos(angles[:, 1::2])

    return ans
    pass