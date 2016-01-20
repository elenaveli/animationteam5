import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

ph = os.path.expanduser('~/public_html')


# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()

ax = plt.axes(xlim=(0, 5), ylim=(-5, 5))

ax.set_axis_bgcolor('deepskyblue')

line, = ax.plot((), [], lw=7, color='white')

circle, =ax.plot(0,0, 'o', markerfacecolor='w', markeredgecolor='w',
markersize=80, markeredgewidth = 10)

diamond_point, = ax.plot((),[], markerfacecolor='y',
              markeredgecolor='yellow', markersize=100,
              markeredgewidth = 100)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    circle.set_data([],[])
    return line,circle,diamond_point

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 10, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    circle.set_data(x,y)
    return line,circle,diamond_point

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=400, interval=20, blit=True)
                               
anim.save(ph+"/basic_animation.mp4", fps=30, extra_args=['-vcodec', 'libx264'])