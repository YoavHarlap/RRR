# import numpy as np
#
#
# def dft_matrix(N):
#     # Create a 1D array of complex numbers representing the roots of unity
#     omega = np.exp(-2j * np.pi / N)
#
#     # Create row and column indices using meshgrid
#     i, j = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
#
#     # Compute the DFT matrix using vectorized operations
#     DFT_matrix = omega ** (i * j)
#
#     return DFT_matrix
#
#
# # Set the size of the DFT matrix (N)
# N = 4
#
# # Create the DFT matrix of size N
# DFT_matrix = dft_matrix(N)
#
# # Print the result
# print("DFT Matrix:")
# print(DFT_matrix)
#
#
#
#
#
#
# import numpy as np
# from scipy.fft import fftfreq, fft
#
#
# def dft_matrix1(N):
#     # Create the frequency values using fftfreq
#     freq = fftfreq(N)
#
#     # Initialize the DFT matrix
#     DFT_matrix = np.zeros((N, N), dtype=np.complex128)
#
#     # Fill in the DFT matrix using fft function
#     for i in range(N):
#         DFT_matrix[:, i] = fft(np.eye(N)[i])
#
#     return DFT_matrix
#
#
# # Set the size of the DFT matrix (N)
# N = 4
#
# # Create the DFT matrix of size N
# DFT_matrix1 = dft_matrix1(N)
#
# # Print the result
# print("DFT Matrix1:")
# print(DFT_matrix1)
#
#



# DFT_matrix2 = fft(np.eye(N))
# print("DFT Matrix2:")
# print(DFT_matrix2)
# print(np.allclose(DFT_matrix1,dft_matrix(N)))




# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# matrix_3x3 = x.reshape(3, 3)
#
# import numpy as np


import numpy as np
from scipy.fft import fft

def dft_matrix(m):
    return fft(np.eye(m))

def reduce_dft_matrix(A, n, symmetric=False):
    m = A.shape[0]

    # Randomly select n columns to keep
    selected_cols = sorted(np.random.choice(m, n, replace=False))

    # Create the reduced DFT matrix
    reduced_matrix = A[:, selected_cols]

    return reduced_matrix

def dft_matrix_not_square(m,n,symmetric=False):
    A = dft_matrix(m)
    # Create the reduced DFT matrix
    reduced_matrix = reduce_dft_matrix(A, n, symmetric=False)
    return reduced_matrix



# Set the size of the original DFT matrix (m x m)
m = 5

# Set the desired size of the reduced matrix (m x n)
n = 3

# Create the original DFT matrix



def generate_matrix(m, n):
    matrix = [[j for j in range(n)] for i in range(m)]
    return matrix

# Example: Generate a 3x4 matrix
original_dft_matrix = np.array(generate_matrix(m, m))


# Create the reduced DFT matrix
reduced_dft_matrix = reduce_dft_matrix(original_dft_matrix, n, symmetric=True)

# Print the results
print("Original DFT Matrix:")
print(original_dft_matrix)

print("\nReduced DFT Matrix:")
print(reduced_dft_matrix)
