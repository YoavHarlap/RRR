learning_rate = 1.0 
for iteration in range(max_iter):
    grad = gradient(y, A, b)
    obj_func = objective_function(y)
    
    learning_rate = armijo_line_search(y, grad)

    y_new = y - learning_rate * grad



def armijo_line_search(y, grad, alpha=0.5, beta=0.5, max_iter=100):
    t = 1.0  # Initial step size
    for _ in range(max_iter):
        if objective_function(y - t * grad) <= objective_function(y) + alpha * t * np.dot(grad, -grad):
            return t
        else:
            t *= beta
    return t





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






    