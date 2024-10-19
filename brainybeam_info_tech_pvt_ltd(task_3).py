# -*- coding: utf-8 -*-
"""BrainyBeam Info-Tech Pvt Ltd(Task_3)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FCTtLUS0bjxaNYND7qQy6vzvLF71WjYT

**Title:Multiple Y-Axes Sharing a Common X-Axis Plot, Description:
Create a plot with multiple y-axes sharing a common x-axis.**
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.log(x + 1)
y3 = np.exp(x / 10)

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax3 = ax1.twinx()

ax3.spines['right'].set_position(('outward', 60))

ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')
ax3.plot(x, y3, 'r-')

ax1.set_xlabel('X-axis')
ax1.set_ylabel('Sin', color='g')
ax2.set_ylabel('Log', color='b')
ax3.set_ylabel('Exp', color='r')

plt.show()