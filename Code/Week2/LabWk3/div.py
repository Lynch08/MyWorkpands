#Author: Enda Lynch
# Division programme with remainder


#enter values using inputs to devide on integer by another

X = int(input('Enter number: '))
Y = int(input('Divided by: '))

# // gives divides the integers and % gives the remainder
B = X//Y
C = X%Y

#display work
print("{} divided by {} is equal to {} remainder {} ".format(X, Y, B, C))
