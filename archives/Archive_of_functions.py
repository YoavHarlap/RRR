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


def dft_matrix(m):
    return fft(np.eye(m))


def cyclic_shift_all_np(arr):
    result = [np.roll(arr, i) for i in range(len(arr))]
    return result

# Example usage:
my_array = np.array([1, 2, 3])

result_array = cyclic_shift_all_np(result_gd)

# for shifted_list in result_array:
#     # print(shifted_list)
#     plt.plot(b)
#     plt.plot(shifted_list)
#     plt.show()


# # Assuming b and shifted_list are your arrays
# for shifted_list in result_array:
#     # Calculate correlation coefficient
#     correlation = np.corrcoef(b, shifted_list)[0, 1]
#     print(f"Correlation coefficient: {correlation}")

#     # Plot the arrays
#     plt.plot(b, label='b')
#     plt.plot(shifted_list, label='shifted_list')
#     plt.legend()
#     plt.title(f"Correlation: {correlation}")
#     plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Assuming b and result_array are your arrays
best_correlation = 0
best_array = None

# for shifted_list in result_array:
#     # Calculate correlation coefficient
#     correlation = np.corrcoef(b, shifted_list)[0, 1]
    
#     # Update best_array if the current correlation is higher
#     if abs(correlation) > best_correlation:
#         best_correlation = abs(correlation)
#         best_array = shifted_list

#     # Plot the arrays
#     plt.plot(b, label='b')
#     plt.plot(np.abs(shifted_list), label='shifted_list')
#     plt.legend()
#     plt.title(f"Correlation: {correlation}")
#     plt.show()

# Print the overall best array
# print(f"\nOverall best array: with correlation coefficient: {best_correlation}")

plt.plot(b, label='b')
plt.plot(np.abs(PA(result_RRR, A)), label='result_RRR')
plt.legend()
# plt.title(f"best Correlation: {best_correlation}")
plt.show()
print("000:", 000)

