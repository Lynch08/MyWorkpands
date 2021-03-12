# A program that makes a list, called salaries, that has 10 random numbers (20000 – 80000)
# Modify the program so that the “random” salaries are the same each time the program is run, to make the program easier to test
# Modify the program, to make another array of numbers that has the salaries plus 5000 (numpy is great for matrix operations)
# Modify the program so that it increases all the salaries by 5% (store in another array)

#Author: Enda Lynch
#Credit: Andrew Beatty - Lab Sheet Week 8
#Credit: https://www.w3schools.com/python/numpy_random.asp
#Credit: https://www.sharpsightlabs.com/blog/numpy-random-seed/
#Credit: https://stackoverflow.com/questions/20011494/plot-normal-distribution-with-matplotlib


import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

minSalary = 20000
maxSalary = 80000
numberOfEntries = 100

np.random.seed(1)  # this is so that the "random" numbers are the same each time - easier to debug.
salaries = np.random.randint(minSalary, maxSalary, numberOfEntries)
salariesPlus = salaries + 5000
salariesMult = salaries * 1.05

#plt.hist(salaries)
#plt.show()
ages = np.random.randint(low = 21, high = 65, size = numberOfEntries)

plt.scatter(ages, salaries)
#plt.show()

#adding x**2
xpoints = np.array(range(1, 101))
ypoints = xpoints**2

#For Normal Distriution Line - could not get my head around this yet
#salMean = np.mean(salaries)
#satStd = np.std(salaries)
#sns.displot(random.normal(size = 100))

plt.plot(xpoints, ypoints, color = 'red', label = 'x squared')

plt.title('Random Plot')
plt.xlabel('Salaries')
plt.ylabel('Ages')
plt.legend()

plt.show()
#plt.savefig('prettier-plot.png')
