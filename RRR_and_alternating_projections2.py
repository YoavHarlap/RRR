import os
import sys

import numpy as np
import matplotlib.pyplot as plt
from print_to_txt_file import Tee


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


def PA(y, A):
    # Calculate the pseudo-inverse of A
    A_dagger = np.linalg.pinv(A)

    # Matrix-vector multiplication: AA†y
    result = np.dot(A, np.dot(A_dagger, y))

    return result

def step_gd(A, b, y, beta):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    y = y - beta * (-2 * PAPB_y + P_Ay + P_By)
    return y
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

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)

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

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break
    elif algo == "GD":
        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)
            y = step_gd(A, b, y, beta)

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

    # Plot the norm difference over iterations
    plt.plot(norm_diff_list)
    plt.xlabel('Iteration')
    plt.ylabel('|PB - PA|')
    plt.title(f'Convergence of {algo} Algorithm')
    plt.show()

    # print("y:", y[:5])
    # print("abs y:", np.abs(y[:5]))

    return y


log_file_path = os.path.join("texts", "RRR_and_GD.txt")
# Create a log file to write to
log_file = open(log_file_path, "w")

# Redirect sys.stdout to the custom Tee object
sys.stdout = Tee(sys.stdout, log_file)

beta = 0.5
max_iter = 10000
tolerance = 1e-6

array_limit = 200
m_array = np.arange(10, array_limit + 1, 10)
n_array = np.arange(10, array_limit + 1, 10)

#
m_array = [21]
n_array = [11]


# Loop over different values of m and n
for m in m_array:  # Add more values as needed
    for n in n_array:  # Add more values as needed
        np.random.seed(42)  # For reproducibility

        print(f"m = {m}, n = {n}")  # Restore the standard output after the loop

        A = np.random.randn(m, n) + 1j * np.random.randn(m, n)
        A_real = np.random.randn(m, n)
        #
        x = np.random.randn(n) + 1j * np.random.randn(n)
        x_real = np.random.randn(n)
        #
        # Calculate b = |Ax|
        b = np.abs(np.dot(A, x))
        b_real = np.abs(np.dot(A_real, x_real))

        y_true = np.dot(A, x)
        y_true_real = np.dot(A_real, x_real)

        # print("y_true:", y_true[:5])
        # print("y_true_real:", y_true_real[:5])

        # Initialize y randomly
        y_initial = np.random.randn(m) + 1j * np.random.randn(m)
        y_initial_real = np.random.randn(m)

        # print("y_initial:", y_initial[:5])
        # print("y_initial_real:", y_initial_real[:5])

        # # Epsilon value
        # epsilon = 1e-1
        # epsilon = 0.5
        # y_initial = y_true + epsilon

        A = A_real
        b = b_real
        y_initial = y_initial_real


        # Call the alternating_projections function with specified variance, standard deviation, and initial y
        result_AP = run_algorithm(A, b, y_initial, algo="alternating_projections", max_iter=max_iter,
                                  tolerance=tolerance)
        print("result_AP:", np.abs(result_AP[:5]))
        print("b:        ", b[:5])

        # Call the RRR_algorithm function with specified parameters
        result_RRR = run_algorithm(A, b, y_initial, algo="RRR_algorithm", beta=beta, max_iter=max_iter,
                                   tolerance=tolerance)
        print("result_RRR:", np.abs(result_RRR[:5]))
        print("b:         ", b[:5])
        # result_gd = run_algorithm(A, b, y_initial, algo="GD", beta=beta, max_iter=max_iter,
        #                           tolerance=tolerance)
        # print("result_GD:", np.abs(result_gd[:5]))
        # print("b:         ", b[:5])


plt.plot(b, label='b')
plt.plot(np.abs(PA(result_RRR, A)), label='result_RRR')
plt.legend()
plt.title("result_RRR and original b")
plt.show()
print("000:", 000)
