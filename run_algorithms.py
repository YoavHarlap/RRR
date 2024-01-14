import matplotlib.pyplot as plt
import numpy as np


def init_random_complex_vector(size):
    # Generate an initial random complex vector y
    y_real = np.random.normal(loc=0, scale=1, size=size)
    y_imag = np.random.normal(loc=0, scale=1, size=size)
    y = y_real + 1j * y_imag

    return y


def create_sensing_matrix(m, n):
    # Generate a complex normal distribution with mean 0 and standard deviation 1
    real_part = np.random.normal(loc=0, scale=1, size=(m, n))
    imag_part = np.random.normal(loc=0, scale=1, size=(m, n))

    # Combine real and imaginary parts to create a complex matrix
    sensing_matrix = real_part + 1j * imag_part
    return sensing_matrix


def pseudoinverse(A):
    # Calculate the pseudoinverse of A
    A_pseudoinv = np.linalg.pinv(A)

    return A_pseudoinv


def proj_A(A, y):
    A_pseudoinv = pseudoinverse(A)
    # Calculate the projection PA(y) = AA†y
    projection = np.dot(A, np.dot(A_pseudoinv, y))

    return projection


def proj_B(b, y):
    # Calculate the point-wise product b * phase(y), where phase(y)[i] := y[i]/|y[i]|
    b_phase_y = b * np.divide(y, np.abs(y), where=(y != 0))

    return b_phase_y


def Alternative_Projections(y, A, b, max_iter=1000, tolerance=1e-9):
    # Calculate the Frobenius norm of the difference between consecutive iterations
    obj_values = []
    # Iterative projections
    for iteration in range(max_iter):
        # Print iteration progress
        # print(f"Iteration {iteration + 1}/{max_iter}")

        # Project y onto the set defined by proj_B
        y = proj_B(b, y)

        # Project y onto the set defined by proj_A
        y = proj_A(A, y)

        obj_values.append(np.linalg.norm(b - np.abs(y)))
        # obj_values.append(np.linalg.norm(y))


        # Calculate the residual (change in y)
        # if proj_A~proj_B stop
        residual = np.linalg.norm(y - proj_B(b, y))

        # Check convergence
        if residual < tolerance:
            print(f"Algorithm 1 Converged after {iteration + 1} iterations.")
            print("obj_values:",obj_values[-5:])
            break

    return [iteration + 1, y, obj_values]


def RRR(y, A, b, beta=1, max_iter=100000, tolerance=1e-9):
    obj_values = []
    print
    # Iterative projections
    for iteration in range(max_iter):
        # Print iteration progress
        # print(f"Iteration {iteration + 1}/{max_iter}")

        # Algorithm 2: Update y using a different formula
        # y = y + beta * (proj_A(A, 2 * proj_B(b, y) - y) - proj_B(b, y))

        y = y + beta * (2 * proj_A(A, proj_B(b, y)) - proj_A(A, y) - proj_B(b, y))
        obj_values.append(np.linalg.norm(b - np.abs(y)))
        # obj_values.append(np.linalg.norm(y))

        # Calculate the residual (change in y)
        # if proj_A~proj_B stop
        residual = np.linalg.norm(proj_A(A, y) - proj_B(b, y))
        # Check convergence
        if residual < tolerance:
            print(f"Algorithm 2 Converged after {iteration + 1} iterations.")
            print("obj_values:",obj_values[-5:])
            print(b[:5] , np.abs(y)[:5])

            break

    return [iteration + 1, y, obj_values]


# Function to run both algorithms for a given m/n ratio
def run_algorithms_for_n(m, n, beta=1, max_iter=1000, tolerance=1e-6):
    # Create the sensing matrix
    A = create_sensing_matrix(m, n)
    # print("A:", A)
    # Generate a random complex vector x
    x = init_random_complex_vector(n)

    # Perform matrix multiplication A * x
    result = np.dot(A, x)

    # Take the absolute value to obtain a real non-negative vector,  |Ax| = b
    b = np.abs(result)

    y = init_random_complex_vector(m)

    # Perform iterative projections for Algorithm 1
    Algo_1_iteration,_,obj_values_1 = Alternative_Projections(y, A, b, max_iter=max_iter, tolerance=tolerance)

    # Perform iterative projections for Algorithm 2
    Algo_2_iteration,_,obj_values_2 = RRR(y, A, b, beta=beta, max_iter=max_iter, tolerance=tolerance)

    return [Algo_1_iteration, Algo_2_iteration,obj_values_1,obj_values_2]


# Fix m at 200 and vary n from 20 to 400
m_fixed = 200
# n_values = np.arange(20, 199, 60)
# n_values = np.arange(20, 199, 30)
n_values = [20,23]

algo_1_iterations = []
algo_2_iterations = []
obj_values_1_array = []
obj_values_2_array = []

for n_value in n_values:

    print(n_value, ":")
    Algo_1_iteration, Algo_2_iteration,obj_values_1,obj_values_2 = run_algorithms_for_n(m_fixed, n_value)
    algo_1_iterations.append(Algo_1_iteration)
    algo_2_iterations.append(Algo_2_iteration)
    obj_values_1_array.append(obj_values_1)
    obj_values_2_array.append(obj_values_2)


# Plot the convergence behavior
plt.plot(n_values, algo_1_iterations, label='Alternative_Projections')
plt.plot(n_values, algo_2_iterations, label='RRR (beta =1)')
plt.xlabel('n (Number of Columns)')
plt.ylabel('Iterations to Converge')
plt.title(f'Convergence Behavior for m={m_fixed} and Varying n')
plt.legend()
plt.show()

#------------------------------------
# # Plot convergence over n_values
# for n_value in n_values:
#     plt.plot(obj_values_1_array, label=f'n_value = {n_value}, after {algo_1_iterations} iter')
#
# plt.xlabel('Iteration')
# plt.ylabel('Objective Function Value')
# plt.title(f'Alternative_Projections\nlosses(x-y_iter) per iter for different n values with m={m_fixed}')
# plt.legend()
# plt.show()
#
# for n_value in n_values:
#     plt.plot(obj_values_2_array, label=f'n_value = {n_value}, after {algo_2_iterations} iter')
#
# plt.xlabel('Iteration')
# plt.ylabel('Objective Function Value')
# plt.title(f'RRR (beta =1)\nlosses(x-y_iter) per iter for different n values with m={m_fixed}')
# plt.legend()
# plt.show()
#

# Create a figure with subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot convergence over n_values for Alternative_Projections
for index,n_value in enumerate(n_values):
    axs[0].plot(obj_values_1_array[index], label=f'n_value = {n_value}, after {algo_1_iterations[index]} iter')

axs[0].set_ylabel('Objective Function Value')
axs[0].set_title(f'Alternative_Projections\nlosses(|b-y_iter|) per iter for different n values with m={m_fixed}')
axs[0].legend()

# Plot convergence over n_values for RRR (beta = 1)
for index,n_value in enumerate(n_values):
    axs[1].plot(obj_values_2_array[index], label=f'n_value = {n_value}, after {algo_2_iterations[index]} iter')

axs[1].set_xlabel('Iteration')
axs[1].set_ylabel('Objective Function Value')
axs[1].set_title(f'RRR (beta = 1)\nlosses(|b-y_iter|) per iter for different n values with m={m_fixed}')
axs[1].legend()

plt.tight_layout()
plt.show()