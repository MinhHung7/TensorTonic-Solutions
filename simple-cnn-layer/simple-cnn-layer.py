import numpy as np

def conv2d(x, W, b):
    """
    x: (N, C_in, H, W)
    W: (C_out, C_in, kH, kW)
    b: (C_out,)
    Valid padding, stride=1.
    """
    x = np.array(x)
    W = np.array(W)
    b = np.array(b)

    N, C_in, H, W_in = x.shape
    C_out, _, kH, kW = W.shape

    H_out = H - kH + 1
    W_out = W_in - kW + 1

    out = np.zeros((N, C_out, H_out, W_out))

    for n in range(N):
        for co in range(C_out):
            for i in range(H_out):
                for j in range(W_out):
                    region = x[n, :, i:i+kH, j:j+kW]      # (C_in, kH, kW)
                    out[n, co, i, j] = np.sum(region * W[co]) + b[co]

    return out

    pass

x = [[[[1,1,1],[1,1,1],[1,1,1]]]]
W = [[[[1,1],[1,1]]]]
b = [0]

print(conv2d(x, W, b))