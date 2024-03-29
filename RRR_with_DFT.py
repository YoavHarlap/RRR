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
        
    
    u,s,v = np.linalg.svd(A)
        
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

            if norm_diff_min>=norm_diff:
                print(iteration,norm_diff)
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
            if norm_diff_min>=norm_diff:
                print(iteration,norm_diff)
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
    
        
    last_element =  100
    norm_diff_list = norm_diff_list[-100:]
    # Calculate the changes |y_i+1 - y_i|
    changes = [abs(y - x) for x, y in zip(norm_diff_list, norm_diff_list[1:])]
    
    # Plot circles at each point
    plt.scatter(range(1, len(norm_diff_list)), changes, marker='o')
    plt.title(f"Changes in last {last_element} elements of norm_diff_list for {algo}")
    plt.xlabel('Index')
    plt.ylabel('|y_i+1 - y_i|')
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


beta = 0.5
max_iter = 100000
tolerance = 1e-6
np.random.seed(42)  # For reproducibility

# Set dimensions
m = 40
n = 20

print("m =", m)
print("n =", n)

A = dft_matrix_not_square(m, n)
# A = np.random.randn(m, n) + 1j * np.random.randn(m, n)
# A_real = np.random.randn(m, n)

x = np.random.randn(n) + 1j * np.random.randn(n)
# x_real = np.random.randn(n)

# Calculate b = |Ax|
b = np.abs(np.dot(A, x))
# b_real = np.abs(np.dot(A_real, x_real))
print("b:", b[:5])
# print("b_real:", b_real[:5])


y_true = np.dot(A, x)
# y_true_real = np.dot(A_real, x_real)

print("y_true:", y_true[:5])
# print("y_true_real:", y_true_real[:5])

# Initialize y randomly
y_initial = np.random.randn(m) + 1j * np.random.randn(m)
# y_initial_real = np.random.randn(m)

print("y_initial:", y_initial[:5])
# print("y_initial_real:", y_initial_real[:5])

# # Epsilon value
# epsilon = 1e-1
# # epsilon = 1
# y_initial = y_true + epsilon


# Call the alternating_projections function with specified variance, standard deviation, and initial y
result_AP = run_algorithm(A, b, y_initial, algo="alternating_projections", max_iter=max_iter,
                          tolerance=tolerance)
# print("result_AP:", np.abs(result_AP[:5]))
# print("b:        ", b[:5])

# Call the RRR_algorithm function with specified parameters
result_RRR = run_algorithm(A, b, y_initial, algo="RRR_algorithm", beta=beta, max_iter=max_iter,
                           tolerance=tolerance)
# print("result_RRR:", np.abs(result_RRR[:5]))
# print("b:         ", b[:5])
