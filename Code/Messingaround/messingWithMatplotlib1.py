#Messing with matplotlib
#Enda Lynch
import numpy as np 
import matplotlib.pyplot as plt

xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = 'xsqu' )
plt.plot(xpoints, xpoints, label = 'straight', color = 'red')
plt.legend()

randomPoints = np.random.randint(1,10000,100) 
plt.scatter(xpoints, randomPoints, label = 'random', color = 'yellow')


plt.show()

