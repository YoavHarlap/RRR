# # import matplotlib.pyplot as plt
# # import numpy as np
# # from mpl_toolkits.mplot3d import Axes3D
# #
# # # Define the function q = (n - r)^2
# # def q_function(n, r):
# #     return (n - r)**2
# #
# # # Generate data for n and r
# # n_values = np.linspace(10, 200, 100)
# # r_values = np.linspace(10, 200, 100)
# #
# # n_mesh, r_mesh = np.meshgrid(n_values, r_values)
# # q_values = q_function(n_mesh, r_mesh)
# #
# # # Create a 3D plot
# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection='3d')
# #
# # # Plot the surface
# # ax.plot_surface(n_mesh, r_mesh, q_values, cmap='viridis')
# #
# # # Set labels
# # ax.set_xlabel('n')
# # ax.set_ylabel('r')
# # ax.set_zlabel('q')
# #
# # # Show the plot
# # plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
# # Define the function q = (n - r)^2
# def q_function(n, r):
#     return (n - r)**2
#
# # Generate data for n and r
# n_values = np.linspace(10, 200, 100)
# r_values = np.linspace(10, 200, 100)
#
# n_mesh, r_mesh = np.meshgrid(n_values, r_values)
#
# # Filter out values where r is greater than n
# valid_indices = r_mesh <= n_mesh
# n_values = n_mesh[valid_indices]
# r_values = r_mesh[valid_indices]
#
# # Calculate q values for valid indices
# q_values = q_function(n_values, r_values)
#
# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
#
# # Scatter plot for valid points
# ax.scatter(n_values, r_values, q_values, c=q_values, cmap='viridis')
#
# # Set labels
# ax.set_xlabel('n')
# ax.set_ylabel('r')
# ax.set_zlabel('q')
#
# # Show the plot
# plt.show()
#

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Define the function q = (n - r)^2
def q_function(n, r):
    return (n - r)**2

# Generate data for n and r
n_values = np.linspace(10, 200, 100)
r_values = np.linspace(10, 200, 100)

n_mesh, r_mesh = np.meshgrid(n_values, r_values)

# Filter out values where r is greater than n
valid_indices = r_mesh <= n_mesh
n_values_valid = n_mesh[valid_indices]
r_values_valid = r_mesh[valid_indices]

# Calculate q values for valid indices
q_values_valid = q_function(n_values_valid, r_values_valid)

# Generate random points where r is less than or equal to n
num_random_points = 50
n_random = np.random.uniform(10, 200, num_random_points)
r_random = np.random.uniform(10, n_random, num_random_points)
q_random = np.random.uniform(10, n_random**2, num_random_points)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for calculated points
ax.scatter(n_values_valid, r_values_valid, q_values_valid, c=q_values_valid, cmap='viridis', label='Calculated Points')

# Scatter plot for random points
ax.scatter(n_random, r_random, q_random, c='red', marker='o', label='Random Points')
# ax.scatter(n_random, r_random, q_random, c='red', marker='x', label='Random Points')


# Set labels
ax.set_xlabel('n')
ax.set_ylabel('r')
ax.set_zlabel('q')

# Show the legend
ax.legend()

# Show the plot
plt.show()
