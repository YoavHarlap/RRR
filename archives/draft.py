import numpy as np
import matplotlib.pyplot as plt

def gaussian(x, mu, sigma):
    return np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

def smooth_objective_function(x_values, y_values, sigma=1.0):
    smoothed_y = np.convolve(y_values, gaussian(x_values, 0, sigma), mode='same') / np.sum(gaussian(x_values, 0, sigma))
    return smoothed_y

# Example objective function
x = np.linspace(-10, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, size=len(x))  # Adding some noise to sine function

# Smooth the objective function
smoothed_y = smooth_objective_function(x, y, sigma=1.0)

# Plot the original and smoothed functions
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Original Function')
plt.plot(x, smoothed_y, label='Smoothed Function')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Smoothing Objective Function with Gaussian Kernel')
plt.legend()
plt.grid(True)
plt.show()
