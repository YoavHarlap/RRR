import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Function to generate random data
def generate_data():
    return np.random.rand(100)

# Function to update the plot
def update(frame):
    data = generate_data()
    line.set_ydata(data)
    return line,

# Create a figure and axis
fig, ax = plt.subplots()
x = np.arange(0, 100)
y = generate_data()

# Create a line plot
line, = ax.plot(x, y)

# Set the axes labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Real-time Plot')

# Set up the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=200)

# Show the plot
plt.show()
