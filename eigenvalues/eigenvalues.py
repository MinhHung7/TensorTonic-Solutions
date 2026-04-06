import numpy as np

def is_valid_matrix(matrix):
    if not isinstance(matrix, (list, tuple)):
        return False
    
    if len(matrix) == 0:
        return False
    
    if not all(isinstance(row, (list, tuple)) for row in matrix):
        return False
    
    row_length = len(matrix[0])
    return all(len(row) == row_length for row in matrix)

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here

    if is_valid_matrix(matrix) and len(matrix) == len(matrix[0]):
        matrix = np.array(matrix)
        
        eigenvalues = np.linalg.eigvals(matrix) 
    
        # Sort by real part, then imaginary part
        idx = np.lexsort((eigenvalues.imag, eigenvalues.real))
        eigenvalues = eigenvalues[idx]

        return eigenvalues
    else:
        return 
    pass 
