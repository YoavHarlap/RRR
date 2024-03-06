def squared_euclidean_norm(x, y):
    difference = np.subtract(y, x)
    norm_squared = np.linalg.norm(difference) ** 2
    return norm_squared


def objective_function(y):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    result1 = squared_euclidean_norm(y, PAPB_y)
    result2 = squared_euclidean_norm(y, P_Ay)
    result3 = squared_euclidean_norm(y, P_By)

    return result1 - 0.5 * (result2 + result3)


def gradient(y):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    return -2 * PAPB_y + P_Ay + P_By


def backtracking_line_search(y0, alpha=0.5, beta=0.8, max_iterations=100):
    y = y0
    iteration = 0

    while iteration < max_iterations:
        grad = gradient(y)
        learning_rate = 1.0  # Initialize learning rate to 1

        # Backtracking line search
        while objective_function(y - learning_rate * grad) > objective_function(y) - alpha * learning_rate * grad ** 2:
            learning_rate *= beta

        y = y - learning_rate * grad

        # Calculate the norm difference between PB - PA
        norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))

        # Store the norm difference for plotting
        norm_diff_list.append(norm_diff)

        # Check convergence
        if norm_diff < tolerance:
            print(f"Converged in {iteration + 1} iterations.")
            break




        print(f'Iteration: {iteration + 1}, y: {y}, f(y): {objective_function(y)}')
        iteration += 1


# Initial point and hyperparameters
initial_point = 3.0
alpha_param = 0.5
beta_param = 0.8
max_iterations_param = 10000

# Perform backtracking line search
backtracking_line_search(initial_point, alpha=alpha_param, beta=beta_param, max_iterations=max_iterations_param)
