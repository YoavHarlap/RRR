import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, ifft


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


def sparse_projection(y, S):
    n = len(y)  # Infer the size of the DFT matrix from the length of y

    # Perform inverse FFT to get the sparse x
    x_sparse = ifft(y)

    # Find indices of S largest elements in absolute values
    indices = np.argsort(np.abs(x_sparse))[-S:]

    # Create a sparse vector by zeroing out elements not in indices
    x_sparse_sparse = np.zeros(n)
    x_sparse_sparse[indices] =np.array(x_sparse)[indices.astype(int)]


    # Reconstruct y using DFT matrix and the sparse x
    y_reconstructed = fft(x_sparse_sparse)

    return y_reconstructed


def step_RRR(S, b, p, beta):
    P_1 = sparse_projection(p, S)
    P_2 = PB(2*P_1-p, b)
    p = p + beta * (P_2 - P_1)
    return p

def pow_p2_S(p,S):
    P_1 = sparse_projection(p, S)
    P_2 = PB(2 * P_1 - p, b)
    return ____



def step_AP(S, b, y):
    y_PB = PB(y, b)
    y_PA = sparse_projection(y_PB, S)
    y = y_PA
    return y


def run_algorithm(S, b, y_init, algo, beta=None, max_iter=100, tolerance=1e-6):
    # Initialize y with the provided initial values
    y = y_init

    # Storage for plotting
    norm_diff_list = []
    norm_diff_min = 1000

    if algo == "alternating_projections":

        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)

            y = step_AP(S, b, y)
            # print("y:", y[:3])

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - sparse_projection(y, S))

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
            y = step_RRR(S, b, y, beta)

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - sparse_projection(y, S))
            norm_diff = np.linalg.norm(pow_p2_S(y,S))

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)
            if norm_diff_min>=norm_diff:
                print(iteration,norm_diff)
                norm_diff_min = norm_diff
            # Check convergence
            if norm_diff > tolerance:
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


beta = 0.5
max_iter = 100000
tolerance = 0.95
np.random.seed(42)  # For reproducibility

# Set dimensions
m = 10
n = 10
S = 1
print("m =", m)
print("n =", n)

A = dft_matrix(m)
# A = dft_matrix_not_square(m, n)
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
# result_AP = run_algorithm(S, b, y_initial, algo="alternating_projections", max_iter=max_iter,
#                           tolerance=tolerance)
# print("result_AP:", np.abs(result_AP[:5]))
# print("b:        ", b[:5])

# Call the RRR_algorithm function with specified parameters
result_RRR = run_algorithm(S, b, y_initial, algo="RRR_algorithm", beta=beta, max_iter=max_iter,
                           tolerance=tolerance)
# print("result_RRR:", np.abs(result_RRR[:5]))
# print("b:         ", b[:5])
