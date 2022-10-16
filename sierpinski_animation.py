
# Dependencies
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter, FFMpegWriter
from os import getcwd

# Global Parameters for the GIF
FPS_RATE = 10
TIME_LENGTH = 10
POINTS_PER_FRAME = 1_000


# Corners of the triangle
p0, p1, p2 = np.array([0,0]), np.array([1,0]), np.array([.5, np.sqrt(3) / 2])

# Getting the starting point from a uniform sampling in the triangle
def get_random_start(): 
    w0 = 1 - np.random.random() ** .5
    w1 = (1 - w0) * np.random.random()
    w2 = 1 - w0 - w1
    return p0 * w0 + p1 * w1 + p2 * w2

# Getting the next point by chosing a random corner and getting halfway to it
def get_new_point(start_point):
    obj = np.random.choice([0,1,2])
    if obj == 0: 
        obj = p0
    elif obj == 1: 
        obj = p1
    else:
        obj = p2
    return (start_point + obj) / 2


# Initializing plot
point = get_random_start()
fig, ax = plt.subplots(figsize = (8,8))
ax.set_axis_off()
xdata, ydata = [point[0]], [point[1]]
ln, = plt.plot([], [], 'bo', markersize = .1)

# Initializer function
def init():
    ax.set_xlim(0, 1)
    ax.set_ylim(0, np.sqrt(3) / 2)
    return ln,

# Function to get the next frames
def update(frame):
    global point
    for _ in range(POINTS_PER_FRAME):
        point = get_new_point(point)
        xdata.append(point[0])
        ydata.append(point[1])
    ln.set_data(xdata, ydata)
    return ln,

# Creating the animation
ani = FuncAnimation(fig, update, frames = TIME_LENGTH * FPS_RATE, 
                    init_func = init, blit = True)

# Saving
filepath = getcwd() + "/sierpinski.gif" 
writervideo = PillowWriter(fps = FPS_RATE) 
ani.save(filepath, writer = writervideo)


 
