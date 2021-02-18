#Author: Enda Lynch
# Programme  to generate a random number (range defined by user)

import random
print ('Pick a range to generate a random number, eg between 10 and 20')
X = int(input('First number: '))
Y = int(input('Second Number: '))

R = random.randint(X,Y)

print('{} is in the range of {} to {}'.format(R,X,Y))