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
    # Calculate the point-wise product b * phase(y)
    b_phase_y = b * np.divide(y, np.abs(y), where=(y != 0))

    return b_phase_y


def Projections_iteratively(A, x, b, max_iter=10000, tolerance=1e-6):
    m, n = A.shape

    # Generate an initial random complex vector y
    y_real = np.random.normal(loc=0, scale=1, size=m)
    y_imag = np.random.normal(loc=0, scale=1, size=m)
    y = y_real + 1j * y_imag

    # Iterative projections
    for iteration in range(max_iter):
        # Project y onto the set defined by proj_B
        y = proj_B(b, y)

        # Print the result of the projection
        print("\nProjection P_B(y):")
        print(y)

        # Project y onto the set defined by proj_A
        y = proj_A(A, y)
        # Print the result of the projection
        print("\nProjection P_A(y):")
        print(y)

        # Calculate the residual (change in y)
        residual = np.linalg.norm(y - proj_B(b, y))

        # Check convergence
        if residual < tolerance:
            print(f"Converged after {iteration + 1} iterations.")
            break

    # Print the final result
    print("\nFinal Resulting Vector |y|:")
    print(abs(y))
    return y


# Define the dimensions of the sensing matrix
m = 5  # Number of rows
n = 3  # Number of columns

# Create the sensing matrix
A = create_sensing_matrix(m, n)

# Print the resulting sensing matrix
print("Sensing Matrix A:")
print(A)

# Generate a random complex vector x
x_real = np.random.normal(loc=0, scale=1, size=n)
x_imag = np.random.normal(loc=0, scale=1, size=n)
x = x_real + 1j * x_imag

# Print the random complex vector x
print("\nRandom Vector x:")
print(x)

# Perform matrix multiplication A * x
result = np.dot(A, x)

# Print the result of the matrix multiplication
print("\nResult of A * x:")
print(result)

# Take the absolute value to obtain a real non-negative vector
b = np.abs(result)

# Print the resulting vector b
print("\nResulting Vector |Ax| = b:")
print(b)

# Perform iterative projections
resulting_vector = Projections_iteratively(A, x, b)
print("\nVector b:")
print(b)