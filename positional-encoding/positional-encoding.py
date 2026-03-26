import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    ans = np.zeros((seq_len, d_model))
    for j in range(0, seq_len):
        for i in range(0, d_model//2):
            ans[j][2*i] = np.sin(j/base**(2*i/d_model))
            ans[j][2*i+1] = np.cos(j/base**(2*i/d_model))
        if d_model % 2 == 1:
            ans[j][d_model - 1] = np.sin(j/base**((d_model-1)/d_model))

    return ans
    pass