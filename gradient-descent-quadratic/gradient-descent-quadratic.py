def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(0, steps):
        x_der = 2*a*x0 + b
        x0 = x0 - lr * x_der
    return x0
    pass