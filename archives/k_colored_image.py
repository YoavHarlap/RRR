import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def color_by_number(image_path, num_colors=10):
    # Read the image
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB

    # Reshape the image to be a list of pixels
    pixels = image.reshape(-1, 3)

    # Apply KMeans clustering to identify dominant colors
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)

    # Assign each pixel to its corresponding cluster center
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_

    # Create a new image where each pixel is replaced by its corresponding cluster center color
    segmented_image = centers[labels].reshape(image.shape)

    # Display the segmented image
    plt.imshow(segmented_image.astype(np.uint8))
    plt.axis('off')
    # plt.title('Segmented Image')
    plt.show()



# Path to the image
image_path = r"C:\Users\ASUS\Downloads\yoav4.jpg"

# Number of colors
num_colors = 8

# Apply color by number
color_by_number(image_path, num_colors)
