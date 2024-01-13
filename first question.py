import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.animation import FFMpegWriter

# Circle equation: x^2 + y^2 + 2x + 2y - 1 = 0
# Line equation: x + y = 1

# Define the line equation
x_line = np.linspace(-5, 5, 100)
y_line = 1 - x_line

# Define the circle equation
theta = np.linspace(0, 2 * np.pi, 100)
x_circle = -1 + np.cos(theta)
y_circle = -1 + np.sin(theta)

# Initialize the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Initialize the line and circle plots
line, = ax.plot([], [], 'b', linewidth=1.5, label='Line: x + y = 1')
circle, = ax.plot([], [], 'r', linewidth=1.5, label='Circle: x^2 + y^2 + 2x + 2y - 1 = 0')
intersection, = ax.plot([], [], 'ro', label='Intersection')

# Set axis labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()

# Set plot title and grid
ax.set_title('Intersection of Line and Circle')
ax.grid(True)

# Function to update the plot in each animation frame
def update(frame):
    # Plot the line and the circle
    line.set_data(x_line, y_line)
    circle.set_data(x_circle, y_circle)

    # Calculate the intersection points
    intersections_x = []
    intersections_y = []
    for i in range(len(x_circle)):
        for j in range(len(x_line)):
            if np.isclose(x_circle[i], x_line[j]) and np.isclose(y_circle[i], y_line[j]):
                intersections_x.append(x_circle[i])
                intersections_y.append(y_circle[i])

    # Plot the intersection points
    intersection.set_data(intersections_x, intersections_y)

    return line, circle, intersection

# Create the animation
animation = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=200, blit=True)

# Save the animation as an MP4 file using FFMpegWriter
animation.save('out.mp4', writer=FFMpegWriter(fps=5))

plt.show()
