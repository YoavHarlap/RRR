import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import matrix_rank, svd


def initialize_matrix(n, r, q,seed = None):
    if seed is not None:
        np.random.seed(seed)  # Set seed for reproducibility

    # Initialize a random matrix of rank r
    init_matrix = np.random.rand(n, r) @ np.random.rand(r, n)
    hints_matrix = init_matrix.copy()
    # print("Original matrix rank:", matrix_rank(hints_matrix))

    # Set q random entries to NaN (missing entries)
    missing_entries = np.random.choice(n * n, q, replace=False)
    row_indices, col_indices = np.unravel_index(missing_entries, (n, n))
    # print(row_indices,col_indices)
    hints_matrix[row_indices, col_indices] = 0
    # print("Matrix rank after setting entries to zero:", matrix_rank(hints_matrix))

    hints_indices = np.ones_like(init_matrix, dtype=bool)
    hints_indices[row_indices, col_indices] = False

    # # Ensure the rank is still r
    # U, Sigma, Vt = svd(matrix)
    # Sigma[r:] = 0  # Zero out singular values beyond rank r
    # new_matrix = U @ np.diag(Sigma) @ Vt
    # print("Matrix rank after preserving rank:", matrix_rank(new_matrix))

    return [init_matrix, hints_matrix, hints_indices]


def proj_1(matrix, r):
    # Perform SVD and truncate to rank r
    u, s, v = np.linalg.svd(matrix, full_matrices=False)
    matrix_proj_1 = u[:, :r] @ np.diag(s[:r]) @ v[:r, :]

    # # Ensure the rank is still r
    # U, Sigma, Vt = svd(matrix)
    # Sigma[r:] = 0  # Zero out singular values beyond rank r
    # new_matrix = U @ np.diag(Sigma) @ Vt

    return matrix_proj_1


def proj_2(matrix, hints_matrix, hints_indices):
    # Set non-missing entries to the corresponding values in the initialization matrix
    matrix[hints_indices] = hints_matrix[hints_indices]
    return matrix

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
def plot_2_metrix(matrix1, matrix2,missing_elements_indices,iteration_number):
    # Set a threshold for coloring based on absolute differences
    threshold = 0.004
    # Calculate absolute differences between matrix1 and matrix2
    diff_matrix = np.abs(matrix2 - matrix1)
    colors = np.where(diff_matrix > threshold, 'red', 'green')
    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))

    # Plot the initial matrix with the specified threshold
    plot_sudoku(matrix1, colors, axs[0], "Init_matrix",missing_elements_indices)

    # Plot the matrix after setting entries to zero with the specified threshold
    plot_sudoku(matrix2, colors, axs[1], "iteration_number: "+ str(iteration_number),missing_elements_indices)

    plt.show()

def matrix_completion(n, r, q, max_iterations=1000, tolerance=1e-6,seed = None):
    # Initialize the matrix with rank r and missing entries
    init_matrix, hints_matrix, hints_indices = initialize_matrix(n, r, q,seed)
    # print(hints_indices)
    missing_elements_indices = ~hints_indices

    matrix = hints_matrix.copy()

    # Lists to store the objective function value and iteration number for plotting
    obj_values = []
    iterations = []

    for i in range(max_iterations):
        #plot_2_metrix(init_matrix, matrix, missing_elements_indices,i)
        # print(i)
        # Alternate between proj_1 and proj_2
        matrix = proj_1(matrix, r)

        matrix = proj_2(matrix, hints_matrix, hints_indices)

        # Calculate the Frobenius norm of the difference between consecutive iterations
        obj_value = np.linalg.norm(matrix - init_matrix, 'fro')

        obj_values.append(obj_value)
        iterations.append(i + 1)

        residual = np.linalg.norm(matrix - proj_1(matrix, r))
        # Check convergence
        if residual < tolerance:
            print(f"Algorithm Converged after {i + 1} iterations.")
            break
    #plot_2_metrix(init_matrix, matrix, missing_elements_indices,"END")

    # # Plot the convergence curve
    # plt.plot(iterations, obj_values, marker='o')
    # plt.xlabel('Iteration')
    # plt.ylabel('Objective Function Value')
    # plt.title('Convergence of Matrix Completion(relative to the correct matrix)')
    # plt.show()

    return [i,obj_values,matrix]



def plot_convergence_over_q(n, r, max_iterations=1000, tolerance=1e-6):
    #q_values = range(15, 2*n-1, 30)
    a=15
    b=n*n-1
    q_values = np.arange(a, b, (b-a)//9)
    print("q_values:",q_values)
    # q_values = [15,20]
    convergence_data = []
    # seed = 42
    seed = np.random.randint(1, 1000)
    seed = 42
    # Create a colormap based on the number of different q values
    cmap = plt.get_cmap('viridis', len(q_values))
    cmap = plt.get_cmap('tab10')


    for i, q in enumerate(q_values):
        print(f"Processing for q = {q}")
        iteration_number, obj_values, completed_matrix = matrix_completion(n, r, q, max_iterations, tolerance, seed)
        convergence_data.append((q, iteration_number, obj_values, cmap(i)))

    # Plot convergence over q
    for q, iteration_number, obj_values, color in convergence_data:
        plt.plot(obj_values, label=f'q = {q}, after {iteration_number} iter', color=color)


    plt.xlabel('Iteration')
    plt.ylabel('Objective Function Value')
    plt.title(f'Convergence of Matrix Completion (relative to the correct matrix) for different q values\n with n={n} and rank ={r}')
    plt.legend()
    plt.show()

# Example usage
n = 200  # Size of the matrix (nxn)
r = 20  # Rank constraint
plot_convergence_over_q(n, r,max_iterations=10000)
print("yoav")


