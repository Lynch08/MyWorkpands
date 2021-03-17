#Messing with matplotlib
#Enda Lynch
import csv
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

filename = pd.read_csv('MTS 2021 Burndown example py.csv')
#xpoints = filename[2]
print(filename.iloc[:,[0]])

xpoints = (filename.iloc[:,[1]])
ypoints = (filename.iloc[:,[2]])

plt.plot(xpoints, ypoints, label = 'xsqu' )
plt.plot(ypoints, xpoints, label = 'straight', color = 'red')
plt.legend()
plt.show()