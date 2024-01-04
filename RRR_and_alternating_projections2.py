import numpy as np
import matplotlib.pyplot as plt


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


def RRR_algorithm(A, b, y_init, beta, max_iter=100, tolerance=1e-6):
    # Initialize y with the provided initial values
    y = y_init

    # Storage for plotting
    norm_diff_list = []

    for iteration in range(max_iter):
        # if iteration % 100 == 0:
        #     print(iteration)

        # iterative algorithm step
        P_Ay = PA(y, A)
        P_By = PB(y, b)
        PAPB_y = PA(P_By, A)

        y = y + beta * (2 * PAPB_y - P_Ay - P_By)

        # Calculate the norm difference between |y| and b
        norm_diff = np.linalg.norm(np.abs(y) - np.abs(b))

        # Store the norm difference for plotting
        norm_diff_list.append(norm_diff)

        # Check convergence
        if norm_diff < tolerance:
            print(f"RRR Converged in {iteration + 1} iterations.")
            break

    # # Plot the norm difference over iterations
    # plt.plot(norm_diff_list)
    # plt.xlabel('Iteration')
    # plt.ylabel('|y| - |b|')
    # plt.title('Convergence of RRR Algorithm')
    # plt.show()

    return y


def alternating_projections(A, b, y_init, var_A=1.0, var_x=1.0, max_iter=100, tolerance=1e-6):
    # Initialize y with the provided initial values
    y = y_init

    # Storage for plotting
    norm_diff_list = []

    for iteration in range(max_iter):
        # if iteration % 100 == 0:
        #     print(iteration)

        # Perform alternating projections
        y_PB = PB(y, b)
        y_PA = PA(y_PB, A)
        y = y_PA

        # Calculate the norm difference between |y| and b
        norm_diff = np.linalg.norm(np.abs(y) - np.abs(b))

        # Store the norm difference for plotting
        norm_diff_list.append(norm_diff)

        # Check convergence
        if norm_diff < tolerance:
            print(f"AP Converged in {iteration + 1} iterations.")
            break

    # # Plot the norm difference over iterations
    # plt.plot(norm_diff_list)
    # plt.xlabel('Iteration')
    # plt.ylabel('|y_PA| - |b|')
    # plt.title('Convergence of Alternating Projections')
    # plt.show()

    return y


np.random.seed(42)  # For reproducibility

beta = 1
max_iter = 10000
tolerance = 1e-6
array_limit = 200
m_array = np.arange(10, array_limit + 1, 10)
n_array = np.arange(10, array_limit + 1, 10)

# Loop over different values of m and n
for m in m_array:  # Add more values as needed
    for n in n_array:  # Add more values as needed
        print("m =", m,",","n =", n)

        A = np.random.randn(m, n) + 1j * np.random.randn(m, n)
        x = np.random.randn(n) + 1j * np.random.randn(n)

        # Calculate b = |Ax|
        b = np.abs(np.dot(A, x))
        y_true = np.dot(A, x)
        # Initialize y randomly
        y_initial = np.random.randn(m) + 1j * np.random.randn(m)

        # Call the alternating_projections function with specified variance, standard deviation, and initial y
        result_AP = alternating_projections(A, b, y_initial, max_iter=max_iter, tolerance=tolerance)
        # print("result_AP:", np.abs(result_AP[-5:]))
        # print("b:        ", b[-5:])

        # Call the RRR_algorithm function with specified parameters
        result_RRR = RRR_algorithm(A, b, y_initial, beta, max_iter=max_iter, tolerance=tolerance)
        # print("result_RRR:", np.abs(result_RRR[-5:]))
        # print("b:         ", b[-5:])
        print("\n")