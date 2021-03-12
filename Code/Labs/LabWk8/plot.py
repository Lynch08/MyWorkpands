#A program that plots the function y = x**2

#Author: Enda Lynch
#Credit: Andrew Beatty - Lab Sheet Week 8

import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints)
plt.show()
