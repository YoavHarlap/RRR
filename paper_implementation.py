import numpy as np

def create_sensing_matrix(m, n):
    # Generate a complex normal distribution with mean 0 and standard deviation 1
    real_part = np.random.normal(loc=0, scale=1, size=(m, n))
    imag_part = np.random.normal(loc=0, scale=1, size=(m, n))

    # Combine real and imaginary parts to create a complex matrix
    sensing_matrix = real_part + 1j * imag_part

    return sensing_matrix


def proj_A(A, y):
    # Calculate the conjugate transpose (Hermitian transpose) of A
    A_dagger = np.conjugate(A.T)

    # Calculate the projection PA(y) = AA†y
    projection = np.dot(A, np.dot(A_dagger, y))

    return projection


def proj_B(b, y):
    # Calculate the point-wise product b * phase(y), where phase(y)[i] := y[i]/|y[i]|
    b_phase_y = b * np.divide(y, np.abs(y), where=(y != 0))

    return b_phase_y


def Projections_iteratively(A, b, max_iter=10000, tolerance=1e-6):
    m, n = A.shape

    # Generate an initial random complex vector y
    y_real = np.random.normal(loc=0, scale=1, size=m)
    y_imag = np.random.normal(loc=0, scale=1, size=m)
    y = y_real + 1j * y_imag

    residuals = []

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
            print(f"Converged after {iteration + 1} iterations.")
            break

    return y


# Define the dimensions of the sensing matrix
m = 5  # Number of rows
n = 3  # Number of columns

# Create the sensing matrix
A = create_sensing_matrix(m, n)

# Generate a random complex vector x
x_real = np.random.normal(loc=0, scale=1, size=n)
x_imag = np.random.normal(loc=0, scale=1, size=n)
x = x_real + 1j * x_imag

# Perform matrix multiplication A * x
result = np.dot(A, x)

# Take the absolute value to obtain a real non-negative vector,  |Ax| = b
b = np.abs(result)

# Perform iterative projections
resulting_vector = Projections_iteratively(A, b)
print("\nresulting_vector |y|:")
print(abs(resulting_vector))
print("\nVector b:")
print(b)
