import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, ifft



def sparse_projection_on_x(y, S):
    n = len(y)  # Infer the size of the DFT matrix from the length of y

    # Perform inverse FFT to get the sparse x
    x_sparse = ifft(y)

    # Find indices of S largest elements in absolute values
    indices = np.argsort(np.abs(x_sparse))[-S:]

    # Create a sparse vector by zeroing out elements not in indices
    x_sparse_sparse = np.zeros(n, dtype='complex_')
    x_sparse_sparse[indices] = np.array(x_sparse)[indices.astype(int)]

    # Reconstruct y using DFT matrix and the sparse x
    y_reconstructed = fft(x_sparse_sparse)

    return y_reconstructed


def sparse_projection_on_y(y, S):
    n = len(y)  # Infer the size of the DFT matrix from the length of y

    # Perform inverse FFT to get the sparse x
    x_sparse = ifft(y)

    # Find indices of S largest elements in absolute values
    indices = np.argsort(np.abs(y))[-S:]

    # Create a sparse vector by zeroing out elements not in indices
    y_sparse = np.zeros(n, dtype='complex_')
    y_sparse[indices] = np.array(y)[indices.astype(int)]

    return y_sparse