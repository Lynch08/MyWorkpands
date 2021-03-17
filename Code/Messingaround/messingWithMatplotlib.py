#Messing with matplotlib
#Enda Lynch
import csv
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

filename = 'MTS 2021 Burndown example py.csv'

data = np.genfromtxt(filename, delimiter=",", names=["x", "y"])
plt.plot(data['x'], data['y'])
plt.show()
#with open(filename) as mtsf:
    #mts = csv.reader(mtsf, delimiter = ',')
    #for row in mts:
        #print('  '.join(row))
    #print (mts)
        #xpoints = mts[1]
        #print(xpoints)


