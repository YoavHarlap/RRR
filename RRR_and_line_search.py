import os
import sys

import matplotlib.pyplot as plt
import numpy as np

from print_to_txt_file import Tee


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


def gradient(y,A,b):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    return -2 * PAPB_y + P_Ay + P_By


def phase(y):
    # Calculate the phase of the complex vector y
    magnitudes = np.abs(y)
    phase_y = np.where(magnitudes != 0, np.divide(y, magnitudes), 0)
    return phase_y


def PB(y, b):
    # Calculate the phase of the complex vector y
    phase_y = phase(y)

    # Point-wise multiplication between b and phase_y
    result = b * phase_y

    return result


def PA(y, A):
    # Calculate the pseudo-inverse of A
    A_dagger = np.linalg.pinv(A)

    # Matrix-vector multiplication: AA†y
    result = np.dot(A, np.dot(A_dagger, y))

    return result


def step_gd(A, b, y, beta):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    y = y - beta * (-2 * PAPB_y + P_Ay + P_By)
    return y


def step_RRR(A, b, y, beta):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    y = y + beta * (2 * PAPB_y - P_Ay - P_By)
    return y


def step_AP(A, b, y):
    y_PB = PB(y, b)
    y_PA = PA(y_PB, A)
    y = y_PA
    return y


def armijo_line_search(y, grad, alpha=0.5, beta=0.5, max_iter=100):
    t = 1.0  # Initial step size
    for _ in range(max_iter):
        if objective_function(y - t * grad) <= objective_function(y) + alpha * t * np.dot(grad, -grad):
            return t
        else:
            t *= beta
    return t



def run_algorithm(A, b, y_init, algo, beta=None, max_iter=100, tolerance=1e-6,alpha=0.5):
    # Initialize y with the provided initial values
    y = y_init

    # Storage for plotting
    norm_diff_list = []

    if algo == "alternating_projections":
        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)

            y = step_AP(A, b, y)

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

    elif algo == "RRR_algorithm":

        for iteration in range(max_iter):
            # if iteration % 100 == 0:
            #     print("iteration:", iteration)

            y = step_RRR(A, b, y, beta)

            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))

            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break
    # elif algo == "line_search":

    #     lr_param = 0.8
    #     iteration = 0
    #     objective_function_array = []
    #     while iteration < max_iter:
    #         # grad = gradient(y)
    #         # learning_rate = 1.0  # Initialize learning rate to 1
    #         # Backtracking line search
    #         # while np.linalg.norm(objective_function(y - learning_rate * grad)) > np.linalg.norm(objective_function(y)):
    #         #     learning_rate *= lr_param
    #         # y = y - learning_rate * grad

        
    #         learning_rate = 0.5
    #         grad =  gradient(y,A,b)
    #         value = objective_function(y)
        
    #         while objective_function(y - learning_rate * grad) > value - alpha * learning_rate * np.dot(grad, grad):
    #             learning_rate *= lr_param
        
    #         y = y - learning_rate * grad
    
    
    #         # print("learning_rate:", learning_rate)
    #         # print("objective_function:", objective_function(y))

    #         objective_function_array.append(objective_function(y))
            
    #         plt.plot(abs(y), label='Iter_RRR_line_search')
    #         plt.plot(b, label='b')

    #         # Adding labels and legend
    #         plt.xlabel('element')
    #         plt.ylabel('value')
    #         plt.title(f'Plots learning_rate = {learning_rate}')
    #         plt.legend()

    #         # Display the plot
    #         plt.show()

            

    #         # Calculate the norm difference between PB - PA
    #         norm_diff = np.linalg.norm(abs(PB(y, b)) - abs(PA(y, A)))

    #         # Store the norm difference for plotting
    #         norm_diff_list.append(norm_diff)
    #         iteration=iteration+1
    #         # Check convergence
    #         if norm_diff < tolerance:
    #             print(f"{algo} Converged in {iteration + 1} iterations.")
    #             break


    elif algo == "line_search":
        objective_function_array = []
        learning_rate = 1.0  # Initial learning rate
        for iteration in range(max_iter):
            grad = gradient(y, A, b)
            obj_func = objective_function(y)
            
            # Perform Armijo line search
            learning_rate = armijo_line_search(y, grad)
    
            # Update solution
            y_new = y - learning_rate * grad
    
            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y_new, b) - PA(y_new, A))
    
            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)
           
            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break
    
            # Update solution for next iteration
            y = y_new
            objective_function_array.append(objective_function(y))
            # plt.plot(abs(y), label='Iter_RRR_line_search')
            
            if iteration % 300 == 0:
                print("norm_diff: ", norm_diff)
                plt.plot(abs(PA(y, A)), label=f'Iter_RRR_line_search_{iteration}')
                plt.plot(b, label='b')
    
                # Adding labels and legend
                plt.xlabel('element')
                plt.ylabel('value')
                plt.title(f'Plots learning_rate = {learning_rate}')
                plt.legend()
    
                # Display the plot
                plt.show()


        


        # Plot the objective function values
        plt.plot(objective_function_array, marker='o', linestyle='-', color='b')
        plt.xlabel('Iteration')
        plt.ylabel('Objective Function Value')
        plt.title('Objective Function Value per Iteration')
        plt.grid(True)
        plt.show()


    # Plot the norm difference over iterations
    plt.plot(norm_diff_list)
    plt.xlabel('Iteration')
    plt.ylabel('|PB - PA|')
    plt.title(f'Convergence of {algo} Algorithm')
    plt.show()


    # print("y:", y[:5])
    # print("abs y:", np.abs(y[:5]))

    return y


def line_search_RRR(A, b, y, max_iter=100, tolerance=1e-6):
    # Set the initial step size
    beta = 1.0

    for iteration in range(max_iter):
        # Calculate the gradient of the objective function
        gradient = -2 * PA(PB(y, b), A) + PA(y, A) + PB(y, b)

        # Update y with the current step size
        y_new = y + beta * gradient

        # Calculate the norm difference between PB - PA for the updated y
        norm_diff_new = np.linalg.norm(PB(y_new, b) - PA(y_new, A))

        # Check if the new step size improves the objective function
        if norm_diff_new < tolerance:
            print("Line search converged.")
            return y_new, beta

        # Reduce the step size (backtracking)
        beta *= 0.5

    print("Line search did not converge. Returning the last result.")
    return y_new, beta


def step_RRR_with_line_search(A, b, y, max_iter=100, tolerance=1e-6):
    # Perform line search to find the optimal step size
    y, beta = line_search_RRR(A, b, y, max_iter, tolerance)

    # Update y with the optimal step size
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    y = y + beta * (2 * PAPB_y - P_Ay - P_By)

    return y


# Modify run_algorithm function to use the new step function


log_file_path = os.path.join("texts", "RRR_and_GD.txt")
# Create a log file to write to
log_file = open(log_file_path, "w")

# Redirect sys.stdout to the custom Tee object
sys.stdout = Tee(sys.stdout, log_file)

beta = 0.5
max_iter = 10000
tolerance = 1e-6


array_limit = 200
m_array = np.arange(10, array_limit + 1, 10)
n_array = np.arange(10, array_limit + 1, 10)

#
m_array = [70]
n_array = [20]

# Loop over different values of m and n
for m in m_array:  # Add more values as needed
    for n in n_array:  # Add more values as needed
        np.random.seed(42)  # For reproducibility

        print(f"m = {m}, n = {n}")  # Restore the standard output after the loop

        A = np.random.randn(m, n) + 1j * np.random.randn(m, n)
        A_real = np.random.randn(m, n)
        #
        x = np.random.randn(n) + 1j * np.random.randn(n)
        x_real = np.random.randn(n)
        #
        # Calculate b = |Ax|
        b = np.abs(np.dot(A, x))
        b_real = np.abs(np.dot(A_real, x_real))

        y_true = np.dot(A, x)
        y_true_real = np.dot(A_real, x_real)

        # print("y_true:", y_true[:5])
        # print("y_true_real:", y_true_real[:5])

        # Initialize y randomly
        y_initial = np.random.randn(m) + 1j * np.random.randn(m)
        y_initial_real = np.random.randn(m)

        # print("y_initial:", y_initial[:5])
        # print("y_initial_real:", y_initial_real[:5])

        # # Epsilon value
        # epsilon = 1e-1
        # epsilon = 0.5
        # y_initial = y_true + epsilon

        A = A_real
        b = b_real
        y_initial = y_initial_real
        y_true = y_true_real

        # Call the alternating_projections function with specified variance, standard deviation, and initial y
        result_AP = run_algorithm(A, b, y_initial, algo="alternating_projections", max_iter=max_iter,
                                  tolerance=tolerance)
        print("result_AP:", np.abs(result_AP[:5]))
        print("b:        ", b[:5])

        # Call the RRR_algorithm function with specified parameters
        result_RRR = run_algorithm(A, b, y_initial, algo="RRR_algorithm", beta=beta, max_iter=max_iter,
                                   tolerance=tolerance)
        print("result_RRR:", np.abs(result_RRR[:5]))
        print("b:         ", b[:5])

        result_RRR_line_search = run_algorithm(A, b, y_initial, algo="line_search", max_iter=max_iter,
                                               tolerance=tolerance)
        print("result_RRR_line_search:", np.abs(result_RRR_line_search[:5]))
        print("b:                     ", b[:5])


        plt.plot(abs(PA(result_RRR_line_search,A)), label='result_RRR_line_search')
        plt.plot(abs(PA(result_RRR,A)), label='result_RRR')
        # plt.plot(abs(PB(result_RRR, b)))
        # plt.plot(abs(PA(result_AP,A)), label='result_AP')
        plt.plot(b, label='b')

        # Adding labels and legend
        plt.xlabel('element')
        plt.ylabel('value')
        plt.title('Plot of Terms')
        plt.legend()

        # Display the plot
        plt.show()
        
        
        # plt.plot(y_true_real, label="y_true_real")
        # plt.plot(result_RRR_line_search, label='y_result_RRR_line_search')

        # # Adding labels and legend
        # plt.xlabel('element')
        # plt.ylabel('value')
        # plt.title('Plot of Terms')
        # plt.legend()

        # # Display the plot
        # plt.show()

