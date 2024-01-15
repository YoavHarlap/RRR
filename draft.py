import numpy as np
import matplotlib.pyplot as plt

def create_colorbar(rgb_coordinates):
    num_colors = len(rgb_coordinates)

    # Create a colorbar with the specified RGB coordinates
    fig, ax = plt.subplots(figsize=(8, 1))  # You can adjust the figsize as needed
    ax.imshow([rgb_coordinates], aspect='auto', extent=[0, num_colors, 0, 1])

    # Hide axes ticks
    step = 1  # Change step to 1 for a tick at every color
    t = np.arange(0, num_colors + step, step)
    ax.set_xticks(t[:-1])  # Exclude the last tick to prevent overlap
    ax.set_xticklabels([str(int(i)) for i in t[:-1]])  # Convert ticks to corresponding indices
    ax.set_yticks([])

    plt.show()

# Example usage:
# Replace the following RGB values with your own coordinates
rgb_coordinates = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1)]
create_colorbar(rgb_coordinates)
