import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import matrix_rank, svd

def initialize_matrix(n, r, q):
    # Initialize a random matrix of rank r
    init_matrix = np.random.rand(n, r) @ np.random.rand(r, n)
    hints_matrix = init_matrix.copy()
    print("Original matrix rank:", matrix_rank(hints_matrix))

    # Set q random entries to NaN (missing entries)
    missing_entries = np.random.choice(n * n, q, replace=False)
    row_indices, col_indices = np.unravel_index(missing_entries, (n, n))
    hints_matrix[row_indices, col_indices] = 0
    print("Matrix rank after setting entries to zero:", matrix_rank(hints_matrix))

    hints_indices = np.ones_like(init_matrix, dtype=bool)
    hints_indices[row_indices, col_indices] = False

    # # Ensure the rank is still r
    # U, Sigma, Vt = svd(matrix)
    # Sigma[r:] = 0  # Zero out singular values beyond rank r
    # new_matrix = U @ np.diag(Sigma) @ Vt
    # print("Matrix rank after preserving rank:", matrix_rank(new_matrix))

    return [init_matrix, hints_matrix, hints_indices]

def plot_sudoku(matrix,colors ,ax, title, missing_elements_indices):
    n = matrix.shape[0]

    # Hide the axes
    ax.set_xticks([])
    ax.set_yticks([])

    # Add a grid
    for i in range(n + 1):
        lw = 2 if i % 3 == 0 else 0.5
        ax.axhline(i, color='black', lw=lw)
        ax.axvline(i, color='black', lw=lw)

    # Calculate text size based on n
    text_size = -5/11 * n + 155/11

    # Fill the cells with the matrix values and color based on differences
    for i in range(n):
        for j in range(n):
            value = matrix[i, j]
            color = colors[i, j]
            if missing_elements_indices[i,j]:
                # Highlight specific cells with blue background
                ax.add_patch(plt.Rectangle((j, n - i - 1), 1, 1, fill=True, color='blue', alpha=0.3))
            if value != 0:
                ax.text(j + 0.5, n - i - 0.5, f'{value:.2f}', ha='center', va='center', color=color, fontsize=text_size)

    ax.set_title(title)
def plot_2_metrix(matrix1, matrix2,missing_elements_indices):
    # Set a threshold for coloring based on absolute differences
    threshold = 0.2
    # Calculate absolute differences between matrix1 and matrix2
    diff_matrix = np.abs(matrix2 - matrix1)
    colors = np.where(diff_matrix > threshold, 'red', 'green')
    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the initial matrix with the specified threshold
    plot_sudoku(matrix1, colors, axs[0], "Matrix 1",missing_elements_indices)

    # Plot the matrix after setting entries to zero with the specified threshold
    plot_sudoku(matrix2, colors, axs[1], "Matrix 2",missing_elements_indices)

    plt.show()


# Example usage
n = 9
r = 5
q = 20
# matrix1, matrix2 = initialize_matrix(n, r, q)
init_matrix, hints_matrix, hints_indices = initialize_matrix(n, r, q)
missing_elements_indices = ~hints_indices


plot_2_metrix(init_matrix, hints_matrix,missing_elements_indices)