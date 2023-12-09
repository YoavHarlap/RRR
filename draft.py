import numpy as np
from numpy.linalg import matrix_rank, svd

def initialize_matrix(n, r, q):
    # Initialize a random matrix of rank r
    init_matrix = np.random.rand(n, r) @ np.random.rand(r, n)
    matrix = np.copy(init_matrix)
    print("Original matrix rank:", matrix_rank(matrix))

    # Set q random entries to NaN (missing entries)
    missing_entries = np.random.choice(n * n, q, replace=False)
    row_indices, col_indices = np.unravel_index(missing_entries, (n, n))
    matrix[row_indices, col_indices] = 0
    print("Matrix rank after setting entries to zero:", matrix_rank(matrix))

    # Ensure the rank is still r
    U, Sigma, Vt = svd(matrix)
    Sigma[r:] = 0  # Zero out singular values beyond rank r
    new_matrix = U @ np.diag(Sigma) @ Vt
    print("Matrix rank after preserving rank:", matrix_rank(new_matrix))

    return init_matrix,new_matrix

# Example usage
n = 5
r = 3
q = 5
result_matrix = initialize_matrix(n, r, q)
