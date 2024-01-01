

import numpy as np
import matplotlib.pyplot as plt

def phase(y):
    # Calculate the phase of the complex vector y
    phase_y = np.divide(y, np.abs(y), where=y!=0)

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

        # iterative algorithm step
        P_Ay = PA(y, A)
        P_By = PB(y, b)
        PAPB_y = PA(PB(y, b), A)

        y = y + beta * (2 * PAPB_y - P_Ay - P_By)

        # Calculate the norm difference between |y| and b
        norm_diff = np.linalg.norm(np.abs(y) - np.abs(b))

        # Store the norm difference for plotting
        norm_diff_list.append(norm_diff)

        # Check convergence
        if norm_diff < tolerance:
            print(f"Converged in {iteration+1} iterations.")
            break

    # Plot the norm difference over iterations
    plt.plot(norm_diff_list)
    plt.xlabel('Iteration')
    plt.ylabel('|y| - |b|')
    plt.title('Convergence of RRR Algorithm')
    plt.show()

    return y

def alternating_projections(A, b, y_init, var_A=1.0, var_x=1.0, max_iter=100, tolerance=1e-6):
    # Initialize y with the provided initial values
    y = y_init

    # Storage for plotting
    norm_diff_list = []

    for iteration in range(max_iter):

        # Perform alternating projections
        y_PB = PB(y, b)
        y_PA = PA(y_PB, A)

        # Calculate the norm difference between |y| and b
        norm_diff = np.linalg.norm(np.abs(y_PA) - np.abs(b))

        # Store the norm difference for plotting
        norm_diff_list.append(norm_diff)

        # Check convergence
        if norm_diff < tolerance:
            print(f"Converged in {iteration+1} iterations.")
            break

        # Update y for the next iteration
        y = y_PA

    # Plot the norm difference over iterations
    plt.plot(norm_diff_list)
    plt.xlabel('Iteration')
    plt.ylabel('|y_PA| - |b|')
    plt.title('Convergence of Alternating Projections')
    plt.show()

    return y_PA

# Set dimensions
m = 200
n = 100

beta = 0.5
max_iter= 10000
tolerance = 1e-6


# Specify variance for the Gaussian matrix A and standard deviation for vector x
variance_A = 0.1  # Adjust this value as needed
std_dev_x = 0.5   # Adjust this value as needed

# Initialize A as a complex Gaussian matrix with specified variance
np.random.seed(42)  # For reproducibility
A = np.sqrt(variance_A) * (np.random.randn(m, n) + 1j * np.random.randn(m, n))
x = np.sqrt(std_dev_x) * (np.random.randn(n) + 1j * np.random.randn(n))

A = np.random.randn(m, n) + 1j * np.random.randn(m, n)
x = np.random.randn(n) + 1j * np.random.randn(n)


# Calculate b = |Ax|
b = np.abs(np.dot(A, x))


# Initialize y randomly
y_initial = np.random.randn(m) + 1j * np.random.randn(m)

# Set RRR parameter beta (adjust as needed)
# Call the alternating_projections function with specified variance, standard deviation, and initial y
result_AP = alternating_projections(A, b, y_initial,max_iter=max_iter,tolerance=tolerance)
print("result_AP:",np.abs(result_AP[-5:]))
print("b:        ",b[-5:])



# Call the RRR_algorithm function with specified parameters
result_RRR = RRR_algorithm(A, b, y_initial, beta,max_iter=max_iter,tolerance=tolerance)
print("result_RRR:",np.abs(result_RRR[-5:]))
print("b:        ",b[-5:])

