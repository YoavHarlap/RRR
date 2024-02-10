import re

filename = r"n_r_q_n_iter.txt"
try:
    with open(filename, "r") as file:
        data_text = file.read()
except FileNotFoundError:
    # Handle file not found error by trying another location
    print(f"filename{filename} not found")


lines = data_text.strip().split('\n')
n_r_q_n_iter = []

i = 0
while i < len(lines):
    offset = 0
    n_line = re.search(r'n = (\d+), r = (\d+), q = (\d+)', lines[i])
    ap_line = re.search(r'alternating_projections Converged in (\d+) iterations', lines[i + 1]) if i + 1 < len(
        lines) else 0
    if ap_line:
        offset = 1
    rrr_line = re.search(r'RRR_algorithm Converged in (\d+) iterations', lines[i + 1 + offset]) if i + 1 + offset < len(
        lines) else 0

    if not n_line:
        i += 1
        continue  # Skip lines without the 'n' line

    n = int(n_line.group(1))
    r = int(n_line.group(2))
    q = int(n_line.group(3))
    ap_n_iter = int(ap_line.group(1)) if ap_line else -1
    rrr_n_iter = int(rrr_line.group(1)) if rrr_line else -1

    n_r_q_n_iter.append([n, r, q, ap_n_iter, rrr_n_iter])

    # Move to the next set of lines
    i += 3 if ap_line and rrr_line else 1

print(n_r_q_n_iter)

import matplotlib.pyplot as plt
import numpy as np


# Define the function q = (n - r)^2
def q_function(n, r):
    return (n - r) ** 2


# Generate data for n and r
n_values = np.linspace(1, 20, 300)
r_values = np.linspace(1, 20, 300)

n_mesh, r_mesh = np.meshgrid(n_values, r_values)

# Filter out values where r is greater than n
valid_indices = r_mesh <= n_mesh
n_values_valid = n_mesh[valid_indices]
r_values_valid = r_mesh[valid_indices]

# Calculate q values for valid indices
q_values_valid = q_function(n_values_valid, r_values_valid)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for calculated points
ax.scatter(n_values_valid, r_values_valid, q_values_valid, c=q_values_valid, cmap='viridis', label='Calculated Points')

# Scatter plot for random points
# ax.scatter(n_random, r_random, q_random, c='red', marker='o', label='Random Points')
# ax.scatter(n_random, r_random, q_random, c='red', marker='x', label='Random Points')


# Set labels
ax.set_xlabel('n')
ax.set_ylabel('r')
ax.set_zlabel('q')

for element in n_r_q_n_iter:
    n, r, q = element[:3]
    if (n == 120 and r == 30 and q == 5):
        print("item:", element)

    AP_iter, RRR_iter = element[3:5]
    if AP_iter == -1 and RRR_iter == -1:
        ax.scatter(n, r, q, c='black', marker='x')
    elif AP_iter == -1:
        ax.scatter(n, r, q, c='orange', marker='o')
    elif RRR_iter == -1:
        ax.scatter(n, r, q, c='blue', marker='o')
    else:
        ax.scatter(n, r, q, c='green', marker='o')

# Show the legend
ax.legend()

# Show the plot
plt.show()
