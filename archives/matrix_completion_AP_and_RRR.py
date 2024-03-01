import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import matrix_rank, svd

import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft


def phase(y):
    # Calculate the phase of the complex vector y
    magnitudes = np.abs(y)
    phase_y = np.where(magnitudes != 0, np.divide(y, magnitudes), 0)

    return phase_y


def PB(y, b):
    # Calculate the phase of the complex vector y
    phase_y = phase(y)

    # Point-wise multiplication between b and phase_y
    result = b * phase_y

    return result


def is_vector_in_image_for_real(matrix, vector):
    # Convert the vector and matrix to NumPy arrays
    vector = np.array(vector)
    matrix = np.array(matrix)

    # Check if the vector is in the column space of the matrix
    is_in_image = np.all(np.isclose(np.dot(matrix, np.linalg.lstsq(matrix, vector, rcond=None)[0]), vector))

    return is_in_image


def is_vector_in_image2(matrix, vector):
    # Convert the vector and matrix to NumPy arrays with complex data type
    vector = np.array(vector, dtype=np.complex128)
    matrix = np.array(matrix, dtype=np.complex128)

    # Check if the vector is in the column space of the matrix
    is_in_image = np.all(np.isclose(np.dot(matrix, np.linalg.lstsq(matrix, vector, rcond=None)[0]), vector))

    return is_in_image


def is_vector_in_image(matrix, vector):
    vector = np.array(vector, dtype=np.complex128)
    matrix = np.array(matrix, dtype=np.complex128)

    # Check if the vector is in the image space of the matrix
    return np.all(np.isclose(np.dot(matrix, np.linalg.lstsq(matrix, vector, rcond=None)[0]), vector))


def project_onto_image_space_for_real(matrix, vector):
    # Convert the vector and matrix to NumPy arrays
    vector = np.array(vector)
    matrix = np.array(matrix)

    # Calculate the projection matrix P_A using the pseudo-inverse
    projection_matrix = np.dot(matrix, np.dot(np.linalg.pinv(np.dot(matrix.T, matrix)), matrix.T))

    # Project the vector onto the image space of A
    projection = np.dot(projection_matrix, vector)

    return projection


def project_onto_image_space(A, y):
    # Convert the y and A to NumPy arrays
    y = np.array(y, dtype=np.complex128)
    A = np.array(A, dtype=np.complex128)

    # Calculate the projection matrix A P_A using the pseudo-inverse
    projection_matrix = np.dot(A, np.dot(np.linalg.pinv(np.dot(A.T.conj(), A)), A.T.conj()))

    # Project the y onto the image space of A
    projection = np.dot(projection_matrix, y)

    return projection


def PA(y, A):
    m = A.shape[0]
    n = A.shape[1]

    # Calculate the pseudo-inverse of A
    A_dagger = np.linalg.pinv(A)

    #     u,s,v = np.linalg.svd(A)
    #
    #     v_T = np.transpose(v)
    #     u_T = np.transpose(u)
    #
    #     # Perform element-wise division avoiding division by zero
    # #    s = np.divide(1, s, where=(s != 0), out=np.zeros_like(s))
    #
    # #    s = np.where(s != 0, np.divide(1, s), 0)
    #
    #     S = [1/x if x <= 1e-8 else 0 for x in s]

    #     S = np.where(s != 0, np.divide(1, s), 0)
    #
    #     # Create a square matrix A with s on its diagonal
    #     extra_cols = m - n  # Number of additional columns
    #
    #     # Create a matrix A with s on its diagonal and extra columns of zeros
    #     A = np.zeros((n, m))
    #     S = np.fill_diagonal(A[:, :n], s)
    #
    #     A_dagger1 = np.dot(v_T, np.dot(S, u_T))
    #
    #     is_same = np.allclose(A_dagger1, A_dagger, atol=0.02)
    #     if not is_same:
    #         print("\n--------------------------------The A_dagger1 is not same")
    #

    # Matrix-vector multiplication: AA†y
    result = np.dot(A, np.dot(A_dagger, y))
    result1 = project_onto_image_space(A, y)
    is_same = np.allclose(result, result1, atol=0.02)
    if not is_same:
        print("The projections is not same")

    u, s, v = np.linalg.svd(A)

    # Check if any eigenvalue is 0
    has_eigenvalue_zero = any(np.isclose(s, 0))

    if has_eigenvalue_zero:
        print("\n-----------------------------------Matrix A has an eigenvalue of 0.\n")

    return result


def step_RRR(A, b, y, beta):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    y = y + beta * (2 * PAPB_y - P_Ay - P_By)
    return y


def step_AP(A, b, y):
    y_PB = PB(y, b)
    y_PA = PA(y_PB, A)
    y = y_PA
    return y


def run_algorithm(A, b, y_init, algo, beta=None, max_iter=100, tolerance=1e-6):
    # Initialize y with the provided initial values
    y = y_init

    # Storage for plotting
    norm_diff_list = []
    norm_diff_min = 1000

    if algo == "alternating_projections":

        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)

            y = step_AP(A, b, y)
            # print("y:", y[:3])

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)

            if norm_diff_min >= norm_diff:
                print(iteration, norm_diff)
                norm_diff_min = norm_diff

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

    elif algo == "RRR_algorithm":
        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)
            y = step_RRR(A, b, y, beta)

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)
            if norm_diff_min >= norm_diff:
                print(iteration, norm_diff)
                norm_diff_min = norm_diff
            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

    # Plot the norm difference over iterations
    plt.plot(norm_diff_list)
    plt.xlabel('Iteration')
    plt.ylabel('PB(y, b) - PA(y, A)')
    plt.title(f'Convergence of {algo} Algorithm')
    plt.show()

    print("y:", y[:5])
    print("abs y:", np.abs(y[:5]))
    print("norm_diff_list:", norm_diff_list[-5:])

    return y


def dft_matrix(m):
    return fft(np.eye(m))


def reduce_dft_matrix(A, n, symmetric=False):
    m = A.shape[0]

    # Randomly select n columns to keep
    selected_cols = sorted(np.random.choice(m, n, replace=False))

    # Create the reduced DFT matrix
    reduced_matrix = A[:, selected_cols]

    return reduced_matrix


def dft_matrix_not_square(m, n, symmetric=False):
    A = dft_matrix(m)
    # Create the reduced DFT matrix
    reduced_matrix = reduce_dft_matrix(A, n, symmetric=False)
    return reduced_matrix



def initialize_matrix(n, r, q):
    # Initialize a random matrix of rank r
    init_matrix = np.random.rand(n, r) @ np.random.rand(r, n)
    hints_matrix = init_matrix.copy()
    print("Original matrix rank:", matrix_rank(hints_matrix))

    # Set q random entries to NaN (missing entries)
    missing_entries = np.random.choice(n * n, q, replace=False)
    row_indices, col_indices = np.unravel_index(missing_entries, (n, n))
    hints_matrix[row_indices, col_indices] = 0
    print("Matrix rank after setting entries to zero:", matrix_rank(hints_matrix))

    hints_indices = np.ones_like(init_matrix, dtype=bool)
    hints_indices[row_indices, col_indices] = False

    # # Ensure the rank is still r
    # U, Sigma, Vt = svd(matrix)
    # Sigma[r:] = 0  # Zero out singular values beyond rank r
    # new_matrix = U @ np.diag(Sigma) @ Vt
    # print("Matrix rank after preserving rank:", matrix_rank(new_matrix))

    return [init_matrix, hints_matrix, hints_indices]


def proj_1(matrix, r):
    # Perform SVD and truncate to rank r
    u, s, v = np.linalg.svd(matrix, full_matrices=False)
    matrix_proj_1 = u[:, :r] @ np.diag(s[:r]) @ v[:r, :]

    # # Ensure the rank is still r
    # U, Sigma, Vt = svd(matrix)
    # Sigma[r:] = 0  # Zero out singular values beyond rank r
    # new_matrix = U @ np.diag(Sigma) @ Vt

    return matrix_proj_1


def proj_2(matrix, hints_matrix, hints_indices):
    # Set non-missing entries to the corresponding values in the initialization matrix
    matrix[hints_indices] = hints_matrix[hints_indices]
    return matrix

def plot_sudoku(matrix,colors ,ax, title, missing_elements_indices):
    n = matrix.shape[0]

    # Hide the axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Add a grid
    for i in range(n + 1):
        lw = 2 if i % 3 == 0 else 0.5
        ax.axhline(i, color='black', lw=lw)
        ax.axvline(i, color='black', lw=lw)

    # Calculate text size based on n
    text_size = -5/11 * n + 155/11

    # Fill the cells with the matrix values and color based on differences
    for i in range(n):
        for j in range(n):
            value = matrix[i, j]
            color = colors[i, j]
            if missing_elements_indices[i,j]:
                # Highlight specific cells with blue background
                ax.add_patch(plt.Rectangle((j, n - i - 1), 1, 1, fill=True, color='blue', alpha=0.3))
            if value != 0:
                ax.text(j + 0.5, n - i - 0.5, f'{value:.2f}', ha='center', va='center', color=color, fontsize=text_size)

    ax.set_title(title)
def plot_2_metrix(matrix1, matrix2,missing_elements_indices,iteration_number):
    # Set a threshold for coloring based on absolute differences
    threshold = 0.004
    # Calculate absolute differences between matrix1 and matrix2
    diff_matrix = np.abs(matrix2 - matrix1)
    colors = np.where(diff_matrix > threshold, 'red', 'green')
    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the initial matrix with the specified threshold
    plot_sudoku(matrix1, colors, axs[0], "Init_matrix",missing_elements_indices)

    # Plot the matrix after setting entries to zero with the specified threshold
    plot_sudoku(matrix2, colors, axs[1], "iteration_number: "+ str(iteration_number),missing_elements_indices)

    plt.show()

def matrix_completion(n, r, q, max_iterations=100000, tolerance=1e-6):
    tolerance = 0.001
    # Initialize the matrix with rank r and missing entries
    init_matrix, hints_matrix, hints_indices = initialize_matrix(n, r, q)
    missing_elements_indices = ~hints_indices

    matrix = hints_matrix.copy()

    # Lists to store the objective function value and iteration number for plotting
    obj_values = []
    iterations = []

    for i in range(max_iterations):
        #plot_2_metrix(init_matrix, matrix, missing_elements_indices,i)
        print(i)
        # Alternate between proj_1 and proj_2
        matrix = proj_1(matrix, r)

        matrix = proj_2(matrix, hints_matrix, hints_indices)

        # Calculate the Frobenius norm of the difference between consecutive iterations
        obj_value = np.linalg.norm(matrix - init_matrix, 'fro')

        obj_values.append(obj_value)
        iterations.append(i + 1)

        residual = np.linalg.norm(matrix - proj_1(matrix, r))
        # Check convergence
        if residual < tolerance:
            print(f"Algorithm Converged after {i + 1} iterations.")
            break
    plot_2_metrix(init_matrix, matrix, missing_elements_indices,"END")

    # Plot the convergence curve
    plt.plot(iterations, obj_values, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Objective Function Value')
    plt.title('Convergence of Matrix Completion(relative to the correct matrix)')
    plt.show()

    return matrix




beta = 0.5
max_iter = 100000
tolerance = 1e-6
np.random.seed(42)  # For reproducibility


# Example usage
n = 9  # Size of the matrix (nxn)
r = 5  # Rank constraint
q = 4  # Number of missing entries to complete

completed_matrix = matrix_completion(n, r, q)

# print("Completed Matrix:")
# print(completed_matrix)
