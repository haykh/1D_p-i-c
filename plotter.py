import matplotlib
matplotlib.use('TKAgg')

from parameters import *

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'

fig = plt.figure()
fig.set_size_inches(12, 10)
ax = plt.axes(xlim=(0, SIZE), ylim=(-6, 6))

scat = ax.scatter([], [], c = '0.2', lw = 0, s = 10)

def init():
    scat.set_offsets([])
    return scat,

def animate(i):
    filename = 'dats/' + NAME + '/step_' + str(i) + ".dat"
    x, y = np.loadtxt(filename, unpack = True)
    data = np.hstack((x[:len(x),np.newaxis],y[:len(x),np.newaxis]))
    scat.set_offsets(data)
    return scat,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=STEPS, interval=1, blit=False)

writer = animation.writers['ffmpeg'](fps=60)
anim.save('results/' + NAME + '.mp4', writer = writer, dpi = 150)

# plt.show()
