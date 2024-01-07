import matplotlib.pyplot as plt
import numpy as np


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

    # Calculate the pseudo-inverse of A
    A_dagger = np.linalg.pinv(A)

    # Matrix-vector multiplication: AA†y
    result = np.dot(A, np.dot(A_dagger, y))
    result1 = project_onto_image_space(A, y)
    is_same = np.allclose(result, result1, atol=0.02)
    
    
    if not is_same:
        print("The projections is not same")
        
        
    # is_in_image_space = is_vector_in_image(A, y)
    #
    # if is_in_image_space:
    #     print("The vector is in the image of the matrix.")
    # else:
    #     print("The vector is not in the image of the matrix.")
    #

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

    if algo == "alternating_projections":
        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)

            y = step_AP(A, b, y)

            # Calculate the norm difference between
            norm_diff = np.linalg.norm(np.abs(y) - b)

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)

            # Check convergence
            if norm_diff < tolerance:
                print(f"Converged in {iteration + 1} iterations.")
                break

    elif algo == "RRR_algorithm":
        y = step_RRR(A, b, y, beta)

        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)
            y = step_AP(A, b, y)

            # Calculate the norm difference between |y| and b
            norm_diff = np.linalg.norm(np.abs(y) - b)

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)

            # Check convergence
            if norm_diff < tolerance:
                print(f"Converged in {iteration + 1} iterations.")
                break

    # Plot the norm difference over iterations
    plt.plot(norm_diff_list)
    plt.xlabel('Iteration')
    plt.ylabel('|y| - b')
    plt.title(f'Convergence of {algo} Algorithm')
    plt.show()

    print("y:", y[:5])
    print("abs y:", np.abs(y[:5]))

    return y


beta = 1
max_iter = 10000
tolerance = 1e-6
np.random.seed(42)  # For reproducibility


# Set dimensions
m = 20
n = 20

print("m =", m)
print("n =", n)


# A = np.random.randn(m, n) + 1j * np.random.randn(m, n)
A_real = np.random.randn(m, n)

# x = np.random.randn(n) + 1j * np.random.randn(n)
x_real = np.random.randn(n)

# Calculate b = |Ax|
# b = np.abs(np.dot(A, x))
b_real = np.abs(np.dot(A_real, x_real))
# print("b:", b[:5])
print("b_real:", b_real[:5])


# y_true = np.dot(A, x)
y_true_real = np.dot(A_real, x_real)

# print("y_true:", y_true[:5])
print("y_true_real:", y_true_real[:5])

# Initialize y randomly
# y_initial = np.random.randn(m) + 1j * np.random.randn(m)
y_initial_real = np.random.randn(m)

# print("y_initial:", y_initial[:5])
print("y_initial_real:", y_initial_real[:5])

# # Epsilon value
# epsilon = 1e-1
# # epsilon = 1
# y_initial = y_true + epsilon


# Call the alternating_projections function with specified variance, standard deviation, and initial y
result_AP = run_algorithm(A_real, b_real, y_initial_real, algo="alternating_projections", max_iter=max_iter,
                          tolerance=tolerance)
# print("result_AP:", np.abs(result_AP[:5]))
# print("b:        ", b[:5])

# Call the RRR_algorithm function with specified parameters
result_RRR = run_algorithm(A_real, b_real, y_initial_real, algo="RRR_algorithm", beta=beta, max_iter=max_iter,
                           tolerance=tolerance)
# print("result_RRR:", np.abs(result_RRR[:5]))
# print("b:         ", b[:5])

