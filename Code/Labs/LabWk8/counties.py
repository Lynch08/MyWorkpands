# A program that has a list of counties, make it a long list (pick from five counties). Make some counties appear more than others. Generate pie chart of the counties
# I am demonstrating more than just how to do pie plots in this.

#Author: Enda Lynch
#Credit: Andrew Beatty - Lab Sheet Week 8

import numpy as np
import matplotlib.pyplot as plt

possCounties = [ 'Cork', 'Kerry', 'Galway', 'Killkenny', 'Offaly']
counties = np.random.choice(
    possCounties, 
    p = [0.31, 0.2, 0.23, 0.17, 0.09],                          
    size = 100
)
print (counties)

# need the number of occurences of each county
#this returns a tuple of the unique values and how many times they appear

unique, counts = np.unique(counties, return_counts=True)

#plt.pie(counts, labels = unique)
plt.bar(unique, counts)
plt.show()