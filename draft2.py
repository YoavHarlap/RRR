import matplotlib.pyplot as plt

def plot_rgb_coordinates(rgb_coordinates,ax):
    num_colors = len(rgb_coordinates)
    fig, ax = plt.subplots(1, 1, figsize=(num_colors, 1))

    # Create a colorbar with the specified RGB coordinates
    ax.imshow([rgb_coordinates], aspect='auto', extent=[0, num_colors, 0, 1])

    # Hide axes
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

# Example usage:
rgb_coordinates = [
    [0.8, 0.2, 0.3],  # RGB values for the first color
    [0.4, 0.6, 0.1],  # RGB values for the second color
    [0.2, 0.5, 0.8],  # RGB values for the third color
    # Add more RGB coordinates as needed
]

plot_rgb_coordinates(rgb_coordinates)
