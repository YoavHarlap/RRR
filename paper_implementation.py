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


def Alternative_Projections(y,A, b, max_iter=100000, tolerance=1e-9):
    # Iterative projections
    for iteration in range(max_iter):
        # Print iteration progress
        print(f"Iteration {iteration + 1}/{max_iter}")

        # Project y onto the set defined by proj_B
        y = proj_B(b, y)

        # Project y onto the set defined by proj_A
        y = proj_A(A, y)

        # Calculate the residual (change in y)
        # if proj_A~proj_B stop
        residual = np.linalg.norm(y - proj_B(b, y))
        # Check convergence
        if residual < tolerance:
            print(f"Algorithm 1 Converged after {iteration + 1} iterations.")
            break

    return iteration + 1,y


def RRR(y,A, b,beta = 1, max_iter=100000, tolerance=1e-9):
    # Iterative projections
    for iteration in range(max_iter):
        # Print iteration progress
        print(f"Iteration {iteration + 1}/{max_iter}")


        # Algorithm 2: Update y using a different formula
        y = y + beta * (proj_A(A, 2 * proj_B(b, y) - y) - proj_B(b, y))


        # Calculate the residual (change in y)
        # if proj_A~proj_B stop
        residual = np.linalg.norm(proj_A(A, y) - proj_B(b, y))
        # Check convergence
        if residual < tolerance:
            print(f"Algorithm 2 Converged after {iteration + 1} iterations.")
            break

    return iteration + 1,y


# Define the dimensions of the sensing matrix
m = 200  # Number of rows
n = 199# Number of columns

# Create the sensing matrix
A = create_sensing_matrix(m, n)

# Generate a random complex vector x
x = init_random_complex_vector(n)

# Perform matrix multiplication A * x
result = np.dot(A, x)

# Take the absolute value to obtain a real non-negative vector,  |Ax| = b
b = np.abs(result)

m, n = A.shape

y = init_random_complex_vector(m)

# Perform iterative projections
max_iter = 10000
tolerance = 1e-6
Algo_1_iteration,Algo_1_resulting_vector = Alternative_Projections(y,A, b,max_iter=max_iter,tolerance=tolerance)
Algo_2_iteration,Algo_2_resulting_vector = RRR(y,A, b,beta = 1,max_iter=max_iter,tolerance=tolerance)
print("\nAlgo_1_resulting_vector |y|:\n",abs(Algo_1_resulting_vector))
print("\nVector b:\n",b)


print("\nAlgo_2_resulting_vector |y|:\n",abs(Algo_2_resulting_vector))
print("\nVector b:\n",b)

print(f"Algorithm 1(Alternative_Projections) Converged after {Algo_1_iteration} iterations.")
print(f"Algorithm 2(RRR) Converged after {Algo_2_iteration} iterations. with beta = 1")


