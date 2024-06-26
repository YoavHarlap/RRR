import os
import sys
from scipy.optimize import root
from scipy.stats import multivariate_normal
import matplotlib.pyplot as plt
import numpy as np

# from print_to_txt_file import Tee
from scipy.optimize import minimize


def squared_euclidean_norm(x, y):
    difference = np.subtract(y, x)
    norm_squared = np.linalg.norm(difference) ** 2
    return norm_squared

def objective_function_power2(y):
    x = objective_function(y)
    return x ** 2

def objective_function(y):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    result1 = squared_euclidean_norm(y, PAPB_y)
    result2 = squared_euclidean_norm(y, P_Ay)
    result3 = squared_euclidean_norm(y, P_By)
    return result1 - 0.5 * (result2 + result3)

def gradient_objective_function(y, A, b):
    P_Ay = PA(y, A)
    P_By = PB(y, b)
    PAPB_y = PA(P_By, A)
    return -2 * PAPB_y + P_Ay + P_By


#################################################
# smoothing #####################################



def smoothing_gradient_objective_function(y, A, b, variance,delta):
    dim_num = len(y)
    eye_matrix = np.eye(dim_num)
    gaussian_at_0 = calc_gaussian_func_at_point(np.zeros_like(y),variance)
    smooth_grad = gradient_objective_function(y, A, b)  * gaussian_at_0
    gaussian_sum = gaussian_at_0
    for i in range(dim_num):
        gaussian_at_delta = calc_gaussian_func_at_point(delta*eye_matrix,variance)
        smooth_grad += gradient_objective_function(y+delta*eye_matrix[i], A, b) * gaussian_at_delta
        smooth_grad += gradient_objective_function(y-delta*eye_matrix[i], A, b) * gaussian_at_delta
        gaussian_sum += 2* gaussian_at_delta

    return smooth_grad/gaussian_sum

def calc_gaussian_func_at_point(point, variance):
    
    # Define the mean vector and covariance matrix
    dim_num = len(point)
    mean = np.zeros(dim_num)  # Assuming 'y' is defined elsewhere
    covariance_matrix = np.eye(dim_num)  # Assuming 'size' is defined elsewhere
    covariance_matrix *= np.sqrt(variance)
    # Define the point at which you want to evaluate the Gaussian
    
    
    # Create multivariate normal distribution
    mv_normal = multivariate_normal(mean=mean, cov=covariance_matrix)
    
    # Evaluate the PDF at the given point
    pdf_value = mv_normal.pdf(point)
    
    # print("PDF at point {}: {}".format(point, pdf_value))
    
    return pdf_value


def step_GD(A, b, y, beta):
    beta = 1
    # delta = beta/2 # make sense lion 
    delta = np.linalg.norm(gradient_objective_function(y, A, b))*beta/2
    variance = delta
    smooth_grad = smoothing_gradient_objective_function(y, A, b, variance,delta)
    result = y - beta * smooth_grad
    return result

###############################################

def gradient_objective_function_power2(y, A, b):
    gradient_objective_func1 = gradient_objective_function(y, A, b)
    objective_func1 = objective_function(y)
    return 2 * gradient_objective_func1 * objective_func1


def phase(y):
    # Calculate the phase of the complex vector y
    # magnitudes = np.abs(y)
    # phase_y = np.where(magnitudes != 0, np.divide(y, magnitudes), 0)

    y1 = np.copy(y)
    # Find indices where t is not zero
    nonzero_indices = np.nonzero(y1)
    if not len(nonzero_indices) == 0 and not len(np.nonzero(np.all(np.abs(y1[nonzero_indices])<1e-5)))==0:
        y1[nonzero_indices] /= np.abs(y1[nonzero_indices])
        
        
    for i, val in enumerate(y1):
        if np.isnan(val):
            print("NaN found at index", i)
            
    
    return y1


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


# def step_GD(A, b, y, beta):
#     result = y - beta * gradient_objective_function(y, A, b)
#     return result


# def step_GD(A, b, y, beta, delta=1e-6, num_directions=10):
#     # Initialize sum of gradients
#     sum_gradients = np.zeros_like(y)
    
#     for _ in range(num_directions):
#         # Generate random direction vector
#         direction = np.random.randn(*y.shape)
#         direction /= np.linalg.norm(direction)
        
#         # Compute gradient in the positive direction
#         grad_positive = gradient_objective_function(y + delta * direction, A, b)
        
#         # Compute gradient in the negative direction
#         grad_negative = gradient_objective_function(y - delta * direction, A, b)
        
#         # Add gradient to the sum
#         sum_gradients += (grad_positive - grad_negative) / (2 * delta * num_directions)
    
#     # Update y using the averaged gradient
#     result = y - beta * sum_gradients
    
#     return result



# def step_GD(A, b, y, beta, delta=1e-3, num_samples=10):
#     # Initialize sum of gradients
#     sum_gradients = np.zeros_like(y)
    
#     num_samples = len(y)
#     for i in range(num_samples):
#         # Initialize direction vector along axis i
#         direction = np.zeros_like(y)
#         direction[i] = 1
#         # direction[num_samples-i-1] = 1

        
#         # direction /= num_samples

#         # Compute gradient in the positive direction
#         grad_positive = gradient_objective_function(y + delta * direction, A, b)
        
#         # Compute gradient in the negative direction
#         grad_negative = gradient_objective_function(y - delta * direction, A, b)
        
#         # Add gradient to the sum
#         sum_gradients += (grad_positive + grad_negative) / (num_samples)
    
#     # Update y using the averaged gradient
#     result = y - beta * sum_gradients
    
#     return result



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

        print("learning_rate:", learning_rate)
        # # learning_rate = 0.5
        objective_func = objective_function(y)

        learning_rate = 0.5* 1/(2*objective_func)
        
        # learning_;rate = abs(0.5* 1/(2*objective_func))

        

    y_new = y - learning_rate * grad

    return y_new, learning_rate

def plot_iter_diff(iteration,y, A,b,algo,lr,th=100):
    if iteration % th == 0:
        # print("norm_diff: ", norm_diff)
        plt.plot(abs(PA(y, A)), label=f'Iter_{algo}_{iteration}')

        plt.plot(b, label='b')
        plt.xlabel('element')
        plt.ylabel('value')
        plt.title(f'Plots learning_rate = {lr}')
        plt.legend()
        plt.show()
    

def run_algorithm(A, b, y_init, algo, beta=0.5, max_iter=100, tolerance=1e-6, alpha=0.5):
    # Initialize y with the provided initial values
    y = y_init
    lr = None
    # Storage for plotting
    norm_diff_list = []
    objective_function_array = []
    converged = -1

    if algo == "alternating_projections":
        for iteration in range(max_iter):
            y = step_AP(A, b, y)
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            norm_diff_list.append(norm_diff)
            objective_function_array.append(objective_function(y))

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                converged = iteration + 1
                break

    elif algo == "RRR_algorithm":
        for iteration in range(max_iter):

            y = step_RRR(A, b, y, beta)
            
            for i, val in enumerate(y):
                if np.isinf(val):
                    print("NaN found at index", i)
    
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            norm_diff_list.append(norm_diff)
            objective_function_array.append(objective_function(y))

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.  for beta = {beta}")
                converged = iteration + 1

                break

            # plot_iter_diff(iteration,y, A,b,algo,lr,th=100)
                
                
    elif algo == "GD":
        for iteration in range(max_iter):

            y = step_GD(A, b, y, beta)
            
            for i, val in enumerate(y):
                if np.isinf(val):
                    print("NaN found at index", i)
    
            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            norm_diff_list.append(norm_diff)
            objective_function_array.append(objective_function(y))

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.  for beta = {beta}")
                converged = iteration + 1

                break

            # plot_iter_diff(iteration,y, A,b,algo,lr,th=100)

    elif algo == "line_search":
        for iteration in range(max_iter):
            y, lr = step_line_search(A, b, y)

            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            norm_diff_list.append(norm_diff)
            objective_function_array.append(objective_function(y))

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations. for beta = {beta}")
                converged = iteration + 1

                break

            # plot_iter_diff(iteration,y, A,b,algo,lr,th=100)

    elif algo == "line_search_power2":

        for iteration in range(max_iter):
            y, lr = step_line_search(A, b, y, objective="power2")

            norm_diff = np.linalg.norm(PB(y, b) - PA(y, A))
            norm_diff_list.append(norm_diff)
            obj_value = objective_function_power2(y)
            objective_function_array.append(obj_value)

            # Check convergence
            if norm_diff < tolerance:
                print(f"{algo} Converged in {iteration + 1} iterations.")
                converged = iteration + 1
                break

            # plot_iter_diff(iteration,y, A,b,algo,lr,th=100)

    # Plot the objective function values
    plt.plot(objective_function_array, marker='o', linestyle='-', color='b')
    plt.xlabel('Iteration')
    plt.ylabel('Objective Function Value')
    plt.title('Objective Function Value per Iteration line search')
    plt.grid(True)
    plt.show()

    # Plot the norm difference over iterations
    plt.plot(norm_diff_list)
    plt.xlabel('Iteration')
    plt.ylabel('|PB - PA|')
    plt.title(f'Convergence of {algo} Algorithm')
    plt.show()
    return y,converged

#
# log_file_path = os.path.join("texts", "RRR_and_GD.txt")
# log_file = open(log_file_path, "w")
# sys.stdout = Tee(sys.stdout, log_file)

beta = 0.5
max_iter = 3000
tolerance = 1e-4

array_limit = 200
m_array = np.arange(10, array_limit + 1, 10)
n_array = np.arange(10, array_limit + 1, 10)

m_array = [100]
n_array = [1,2,3]
n_array = range(20, 50, 4)
betas = np.linspace(0.3, 0.999, 10)
betas = [1]
GD_converged_list = []
RRR_converged_list = []
index_of_operation = 0
# Loop over different values of m and n
for m in m_array:  # Add more values as needed
    for n in n_array:  # Add more values as needed
        for beta in betas:  
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
            print("yoav")
    
            
            
            # result_AP = run_algorithm(A, b, y_initial, algo="alternating_projections", max_iter=max_iter, tolerance=tolerance)
            # plt.plot(abs(PA(result_AP,A)), label='result_AP')
    
            result_RRR, RRR_converged = run_algorithm(A, b, y_initial, algo="RRR_algorithm", beta=beta, max_iter=max_iter,tolerance=tolerance)
            plt.plot(abs(PA(result_RRR,A)), label='result_RRR')
            RRR_converged_list.append(RRR_converged)
            
            result_GD, GD_converged = run_algorithm(A, b, y_initial, algo="GD", beta=beta, max_iter=max_iter,tolerance=tolerance)
            plt.plot(abs(PA(result_GD,A)), label='result_GD')
            GD_converged_list.append(GD_converged)

            # result_line_search = run_algorithm(A, b, y_initial, algo="line_search", max_iter=max_iter,tolerance=tolerance)
            # plt.plot(abs(PA(result_line_search, A)), label='result_line_search')
    
            # result_line_search_power2 = run_algorithm(A, b, y_initial, algo="line_search_power2", max_iter=max_iter,tolerance=tolerance)
            # plt.plot(abs(PA(result_line_search_power2, A)), label='result_line_search_power2')
            
            index_of_operation+=1
    
            plt.plot(b, label='b')
            plt.xlabel('element')
            plt.ylabel('value')
            plt.title('Plot of Terms')
            plt.legend()
            plt.show()
            

plt.plot(range(index_of_operation),RRR_converged_list, label='RRR Converged')
plt.plot(range(index_of_operation),GD_converged_list, label='GD Converged')

# Adding labels and title
plt.xlabel('Scenario')
plt.ylabel('Convergence - num of iterations')
plt.title('Convergence Plot')

# Adding legends
plt.legend()

# Displaying the plot
plt.show()

plt.semilogy(range(index_of_operation), RRR_converged_list, label='RRR Converged')
plt.semilogy(range(index_of_operation), GD_converged_list, label='GD Converged')

# Adding labels and title
plt.xlabel('Scenario')
plt.ylabel('Convergence - num of iterations')
plt.title('Convergence Plot')
print("yoav1")
# Adding legends
plt.legend()

# Displaying the plot
plt.show()

