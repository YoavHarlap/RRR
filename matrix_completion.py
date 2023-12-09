import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import matrix_rank,svd


def initialize_matrix(n, r, q):
    # Initialize a random matrix of rank r
    matrix = np.random.rand(n, r) @ np.random.rand(r, n)
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

    return new_matrix

def proj_1(matrix, r):
    # Perform SVD and truncate to rank r
    u, s, v = np.linalg.svd(matrix, full_matrices=False)
    matrix_proj_1 = u[:, :r] @ np.diag(s[:r]) @ v[:r, :]
    return matrix_proj_1


def proj_2(matrix, init_matrix):
    # Set non-missing entries to the corresponding values in the initialization matrix
    matrix_proj_2 = np.where(~np.isnan(init_matrix), init_matrix, matrix)
    return matrix_proj_2


def matrix_completion(n, r, q, max_iterations=1000, tolerance=1e-6):
    # Initialize the matrix with rank r and missing entries
    matrix = initialize_matrix(n, r, q)

    # Save the initial matrix for proj_2
    init_matrix = matrix.copy()

    # Lists to store the objective function value and iteration number for plotting
    obj_values = []
    iterations = []

    for i in range(max_iterations):
        # Alternate between proj_1 and proj_2
        matrix = proj_1(matrix, r)
        matrix = proj_2(matrix, init_matrix)

        # Calculate the Frobenius norm of the difference between consecutive iterations
        obj_value = np.linalg.norm(matrix - init_matrix, 'fro')

        obj_values.append(obj_value)
        iterations.append(i + 1)

        # Check for convergence
        if i > 0 and abs(obj_values[i] - obj_values[i - 1]) < tolerance:
            break

    # Plot the convergence curve
    plt.plot(iterations, obj_values, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Objective Function Value')
    plt.title('Convergence of Matrix Completion')
    plt.show()

    return matrix


# Example usage
n = 200  # Size of the matrix (nxn)
r = 10  # Rank constraint
q = 50  # Number of missing entries to complete

completed_matrix = matrix_completion(n, r, q)
print("Completed Matrix:")
print(completed_matrix)
