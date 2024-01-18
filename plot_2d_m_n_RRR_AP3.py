import re

import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import matplotlib.colors as mcolors
import seaborn as sns





def plot_rgb_coordinates(rgb_coordinates, ax,step):
    num_colors = len(rgb_coordinates)

    # Create a colorbar with the specified RGB coordinates
    ax.imshow([rgb_coordinates], aspect='auto', extent=[0, num_colors, 0, 1])

    # Hide axes ticks
    ax.set_yticks([])

    # Add title
    # ax.set_title('RGB Color Palette')

    # Add x-axis legend
    ax.set_xlabel(f"Colors * {step}")


# Your data
data_text = """
m = 10 , n = 10
AP Converged in 1 iterations.
RRR Converged in 1 iterations.

"""
import os

filename = "savesAnormal.txt"

folder_path = r"C:\Users\ASUS\PycharmProjects\RRR"
file_path = os.path.join(folder_path, filename)

try:
    with open(filename, "r") as file:
        data_text = file.read()
except FileNotFoundError:
    # Handle file not found error by trying another location
    folder_path = r"//home//yoavharlap//PycharmProjects//RRR"

    new_file_path = os.path.join(folder_path, filename)

    try:
        with open(new_file_path, "r") as file:
            data_text = file.read()
    except FileNotFoundError:
        print("File not found in both locations.")

print(data_text)
# Ignore lines containing "The projections is not same" before processing
data_text = '\n'.join(line for line in data_text.split('\n') if "The projections is not same" not in line)


# Extract relevant information using regular expressions
pattern = re.compile(
    r"m = (\d+), n = (\d+)\n(?:alternating_projections Converged in (\d+) iterations\.)?(?:\n?RRR_algorithm Converged in (\d+) iterations\.)?")
matches = pattern.findall(data_text)


# Convert matches to dictionary
data = []
for match in matches:
    m, n, ap_iterations, rrr_iterations = map(lambda x: int(x) if x else None, match)
    data.append({'m': m, 'n': n, 'AP_iterations': ap_iterations, 'RRR_iterations': rrr_iterations})

# Plotting
colors = []
for entry in data:
    if entry['AP_iterations'] is not None and entry['RRR_iterations'] is not None:
        colors.append('green')
    elif entry['AP_iterations'] is None and entry['RRR_iterations'] is None:
        colors.append('red')
    elif entry['AP_iterations'] is not None and entry['RRR_iterations'] is None:
        colors.append('blue')  # Choose your color for AP Converged only
    elif entry['AP_iterations'] is None and entry['RRR_iterations'] is not None:
        colors.append('orange')  # Choose your color for RRR Converged only


# Extract RRR values and handle None values
rrr_values = [entry['RRR_iterations'] for entry in data]
valid_rrr_values = [rrr for rrr in rrr_values if rrr is not None]


# Check if there are valid RRR values
if not valid_rrr_values:
    print("No valid RRR values found.")



color_len = 15
step = 200
# step = 700

colormap  = sns.color_palette("viridis", n_colors=color_len)
colormap = np.flip(colormap)

import matplotlib.pyplot as plt
import numpy as np

# Assuming you have defined colormap and colors somewhere in your code

# Create a figure with two subplots (1 row, 2 columns)
# fig, axes = plt.subplots(2, 1, figsize=(8, 10))  # You can adjust the figsize as needed
fig, axes = plt.subplots(2, 1, figsize=(8, 10), gridspec_kw={'height_ratios': [8, 1]})

# Plot on the first subplot (upper one)
ax1 = axes[0]
for i, entry in enumerate(data):
    rrr = entry['RRR_iterations']
    p = np.floor((-1 + np.sqrt(1 + 8 * i)) / 2)
    if colors[i] == "red":
        ax1.scatter(entry['m'], entry['n'], color='gray', marker='x')
    elif rrr is not None:
        color_index = rrr // step
        if color_index >= color_len:
            color = colormap[-1]
        else:
            color = colormap[color_index]
        ax1.scatter(entry['m'], entry['n'], color=colors[i])
        ax1.text(entry['m'], entry['n'] + 1.6 + 1.6 * (-1) ** p,
                 f"AP: {entry['AP_iterations']}, RRR: {rrr}",
                 fontsize=6, color=color)
    else:
        ax1.scatter(entry['m'], entry['n'], color=colors[i])
        ax1.text(entry['m'], entry['n'] + 1.6 + 1.6 * (-1) ** p,
                 f"AP: {entry['AP_iterations']}, RRR: {entry['RRR_iterations']}", fontsize=6)

# Set title and labels for the first subplot
ax1.set_title('Convergence Plot with A normal matrix(mxn)\n max iterations = 10000 ')
ax1.set_xlabel('m')
ax1.set_ylabel('n')

# Plot the colors on the second subplot (lower one)
ax2 = axes[1]
plot_rgb_coordinates(colormap,ax2,step)
# Show the plot
plt.show()

