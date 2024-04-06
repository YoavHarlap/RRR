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


def objective_function_power2(y):
    x = objective_function(y)
    return x ** 2


def gradient_objective_function(y, A, b):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    return -2 * PAPB_y + P_Ay + P_By


def gradient_objective_function_power2(y, A, b):
    gradient_objective_func = gradient_objective_function(y, A, b)
    objective_func = objective_function(y)
    return 2 * objective_func * gradient_objective_func


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


def step_RRR(A, b, y, beta):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    result = y + beta * (2 * PAPB_y - P_Ay - P_By)
    return result


def step_AP(A, b, y):
    y_PB = PB(y, b)
    y_PA = PA(y_PB, A)
    resulr = y_PA
    return resulr


def armijo_line_search(y, grad, objective_func=objective_function, alpha=0.5, beta=0.5, max_iter=100):
    t = 1.0  # Initial step size
    for _ in range(max_iter):
        if objective_func(y - t * grad) <= objective_func(y) + alpha * t * np.dot(grad, -grad):
            print("step is:", t)
            return t
        else:
            t *= beta
    return t


def step_line_search(A, b, y, objective="objective"):
    if objective == "objective":
        grad = gradient_objective_function(y, A, b)
        learning_rate = armijo_line_search(y, grad)
    if objective == "power2":
        grad = gradient_objective_function_power2(y, A, b)
        learning_rate = armijo_line_search(y, grad, objective_function_power2)

    y_new = y - learning_rate * grad
    return y_new, learning_rate


def step_previous_iterations(A, b, y, beta, prev_y, rrr_weight=1,y_initial = 0):
    rrr_step = step_RRR(A, b, y, beta)
    prev_step = y - prev_y
    prev_step = y - y_initial

    if np.all(prev_step == 0):
        return rrr_step
    
    return  rrr_weight * rrr_step + (1 - rrr_weight) * prev_step

    # return (rrr_weight * rrr_step - (1 - rrr_weight) * prev_step)*1/np.linalg.norm(prev_step)


# ##############

def step_prevs_iterations(A, b, y, beta, prev_y, rrr_weight, num_prev_points):
    rrr_weight = 0.9995
    num_prev_points = 20
    rrr_step =step_RRR(A, b, y, beta)
    # Calculate the average of the previous points
    prev_step = np.mean([prev_y[i] for i in range(min(num_prev_points, len(prev_y)))], axis=0)

    if np.linalg.norm(prev_step) != 0:
        return rrr_weight * rrr_step + (1 - rrr_weight) * prev_step #* (1 / np.linalg.norm(prev_step))
    else:
        return rrr_step


# ##############


def run_algorithm(A, b, y_init, algo, beta=0.5, max_iter=100, tolerance=1e-6, alpha=0.5):
    # Initialize y with the provided initial values
    y = y_init
    lr = None
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
            
            
            if iteration % 10 == 0:
                print("norm_diff: ", norm_diff)
                plt.plot(abs(PA(y, A)), label=f'Iter_RRR_algorithm_{iteration}')
                plt.plot(b, label='b')

                # Adding labels and legend
                plt.xlabel('element')
                plt.ylabel('value')
                plt.title(f'Plots learning_rate = {lr}')
                plt.legend()

                # Display the plot
                plt.show()
                

    elif algo == "line_search":

        objective_function_array = []
        learning_rate = 1  # Initial learning rate
        for iteration in range(max_iter):
            y, lr = step_line_search(A, b, y)
            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)
            objective_function_array.append(objective_function(y))

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

            if iteration % 100 == 0:
                print("norm_diff: ", norm_diff)
                plt.plot(abs(PA(y, A)), label=f'Iter_line_search_{iteration}')
                plt.plot(b, label='b')

                # Adding labels and legend
                plt.xlabel('element')
                plt.ylabel('value')
                plt.title(f'Plots learning_rate = {lr}')
                plt.legend()

                # Display the plot
                plt.show()

        # Plot the objective function values
        plt.plot(objective_function_array, marker='o', linestyle='-', color='b')
        plt.xlabel('Iteration')
        plt.ylabel('Objective Function Value')
        plt.title('Objective Function Value per Iteration line search')
        plt.grid(True)
        plt.show()


    elif algo == "line_search_power2":

        objective_function_array = []
        learning_rate = 1  # Initial learning rate
        for iteration in range(max_iter):
            y, lr = step_line_search(A, b, y, objective="power2")
            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)
            obj_value = objective_function_power2(y)
            objective_function_array.append(obj_value)

            # Check convergence
            if norm_diff < tolerance or obj_value < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

            if iteration % 100 == 0:
                print("norm_diff: ", norm_diff)
                plt.plot(abs(PA(y, A)), label=f'Iter_line_search_power2_{iteration}')
                plt.plot(b, label='b')

                # Adding labels and legend
                plt.xlabel('element')
                plt.ylabel('value')
                plt.title(f'Plots learning_rate = {lr}')
                plt.legend()

                # Display the plot
                plt.show()


    elif algo == "smart_weighting":
        lr = None
        objective_function_array = []
        learning_rate = 1  # Initial learning rate
        prev_y = y_initial.copy()
        for iteration in range(max_iter):
            y = step_previous_iterations(A, b, y, beta, prev_y, rrr_weight=0.5,y_initial = y_initial.copy())
            # Calculate the norm difference between PB - PA
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)
            obj_value = objective_function(y)
            objective_function_array.append(obj_value)

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

            if iteration % 100 == 0:
                print("norm_diff: ", norm_diff)
                plt.plot(abs(PA(y, A)), label=f'Iter_smart_w{iteration}')
                plt.plot(b, label='b')

                # Adding labels and legend
                plt.xlabel('element')
                plt.ylabel('value')
                plt.title(f'Plots learning_rate = {lr}')
                plt.legend()

                # Display the plot
                plt.show()
                
                
                
                
    elif algo == "prevs_smart_weighting":
        lr = None
        objective_function_array = []
        norm_diff_list = []
        num_prev_points = 20
        rrr_weight = 0.5
        learning_rate = 1  # Initial learning rate        
        prev_y = [y_initial.copy()] * num_prev_points
        max_iter = 100000
        for iteration in range(max_iter):
            y1 = step_RRR(A, b, y, beta)
            y = step_prevs_iterations(A, b, y, beta, prev_y, rrr_weight, num_prev_points)
            # print("",y[0:3],'\n',y1[0:3])
            # print("8--------------8")
            prev_y.pop(0)
            prev_y.append(y)

            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            # Store the norm difference for plotting
            norm_diff_list.append(norm_diff)
            obj_value = objective_function(y)
            objective_function_array.append(obj_value)

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                break

            if iteration % 10 == 0:
                print("norm_diff: ", norm_diff)
                plt.plot(abs(PA(y, A)), label=f'prevs_Iter_smart_w{iteration}')
                plt.plot(b, label='b')

                # Adding labels and legend
                plt.xlabel('element')
                plt.ylabel('value')
                plt.title(f'Plots learning_rate = {lr}')
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

    return y


log_file_path = os.path.join("texts", "RRR_and_GD.txt")
# Create a log file to write to
log_file = open(log_file_path, "w")

# Redirect sys.stdout to the custom Tee object
sys.stdout = Tee(sys.stdout, log_file)

beta = 0.5
max_iter = 1000
tolerance = 1e-6

array_limit = 200
m_array = np.arange(10, array_limit + 1, 10)
n_array = np.arange(10, array_limit + 1, 10)

#
m_array = [20]
n_array = [11]

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

        # Initialize y randomly
        y_initial = np.random.randn(m) + 1j * np.random.randn(m)
        y_initial_real = np.random.randn(m)

        A = A_real
        b = b_real
        y_initial = y_initial_real
        y_true = y_true_real

        # result_AP = run_algorithm(A, b, y_initial, algo="alternating_projections", max_iter=max_iter,
        #                           tolerance=tolerance)
        # print("result_AP:", np.abs(result_AP[:5]))
        # print("b:        ", b[:5])

        # result_RRR = run_algorithm(A, b, y_initial, algo="RRR_algorithm", beta=beta, max_iter=max_iter,
        #                             tolerance=tolerance)
        # print("result_RRR:", np.abs(result_RRR[:5]))
        # print("b:         ", b[:5])

        # result_line_search = run_algorithm(A, b, y_initial, algo="line_search", max_iter=max_iter,
        #                                     tolerance=tolerance)
        # print("result_line_search:", np.abs(PA(result_line_search, A)[:5]))
        # print("b:                     ", b[:5])

        # result_line_search_power2 = run_algorithm(A, b, y_initial, algo="line_search_power2", max_iter=max_iter,
        #                                     tolerance=tolerance)
        # print("result_line_search_power2:", np.abs(PA(result_line_search_power2, A)[:5]))
        # print("b:                     ", b[:5])

        # result_smart_weighting = run_algorithm(A, b, y_initial, algo="smart_weighting", max_iter=max_iter,
        #                                        tolerance=tolerance)
        # print("result_smart_weighting:", np.abs(PA(result_smart_weighting, A)[:5]))
        # print("b:                     ", b[:5])
        
        result_prevs_smart_weighting = run_algorithm(A, b, y_initial, algo="prevs_smart_weighting", max_iter=max_iter,
                                               tolerance=tolerance)
        print("result_smart_weighting:", np.abs(PA(result_prevs_smart_weighting, A)[:5]))
        print("b:                     ", b[:5])
        

        # plt.plot(abs(PA(result_line_search, A)), label='result_line_search')
        # plt.plot(abs(PA(result_line_search_power2, A)), label='result_line_search_power2')
        # plt.plot(abs(PA(result_smart_weighting, A)), label='result_smart_weighting')
        plt.plot(abs(PA(result_prevs_smart_weighting, A)), label='result_prevs_smart_weighting')


        # plt.plot(abs(PA(result_RRR,A)), label='result_RRR')
        # plt.plot(abs(PA(result_AP,A)), label='result_AP')
        plt.plot(b, label='b')

        # Adding labels and legend
        plt.xlabel('element')
        plt.ylabel('value')
        plt.title('Plot of Terms')
        plt.legend()

        # Display the plot
        plt.show()
