import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

def initialize_matrix(n, r, q):
    # Initialize a random matrix of rank r
    init_matrix = np.random.rand(n, r) @ np.random.rand(r, n)
    matrix = np.copy(init_matrix)
    print("Original matrix rank:", np.linalg.matrix_rank(matrix))

    # Set q random entries to NaN (missing entries)
    missing_entries = np.random.choice(n * n, q, replace=False)
    row_indices, col_indices = np.unravel_index(missing_entries, (n, n))
    matrix[row_indices, col_indices] = 0
    print("Matrix rank after setting entries to zero:", np.linalg.matrix_rank(matrix))

    # Ensure the rank is still r
    U, Sigma, Vt = np.linalg.svd(matrix)
    Sigma[r:] = 0  # Zero out singular values beyond rank r
    new_matrix = U @ np.diag(Sigma) @ Vt
    print("Matrix rank after preserving rank:", np.linalg.matrix_rank(new_matrix))

    return init_matrix, new_matrix

def plot_sudoku(matrix, ax, title):
    n = matrix.shape[0]

    # Hide the axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Add a grid
    for i in range(n + 1):
        lw = 2 if i % 3 == 0 else 0.5
        ax.axhline(i, color='black', lw=lw)
        ax.axvline(i, color='black', lw=lw)

    # Calculate differences between matrix1 and matrix2
    diff_matrix = matrix2 - matrix1

    # Create a colormap with red for negative differences and green for positive differences
    cmap = ListedColormap(['red', 'green'])
    norm = plt.Normalize(np.min(diff_matrix), np.max(diff_matrix))

    # Calculate text size based on n
    text_size = -5/11*n +155/11
    print(text_size)

    # Fill the cells with the matrix values and color based on differences
    for i in range(n):
        for j in range(n):
            value = matrix[i, j]
            color = cmap(norm(diff_matrix[i, j]))
            if value != 0:
                ax.text(j + 0.5, n - i - 0.5, f'{value:.2f}', ha='center', va='center', color=color, fontsize=text_size)

    ax.set_title(title)

# Example usage
n = 9
r = 5
q = 20
matrix1, matrix2 = initialize_matrix(n, r, q)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the initial matrix
plot_sudoku(matrix1, axs[0], "Matrix 1")

# Plot the matrix after setting entries to zero
plot_sudoku(matrix2, axs[1], "Matrix 2")
print(matrix2)
plt.show()
