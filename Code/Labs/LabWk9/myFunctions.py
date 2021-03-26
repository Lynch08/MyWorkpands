#In this lab we are going to make a function called Fibonacci in a module called myFunctions to show error handeling
#Author: Enda Lynch
#Credit: Andrew Beatty (LabWk 9)

def fibonacci (number):
    return[] 

return7 = [0,1,1,2,3,5,8]
return11 = [0,1,1,2,3,5,8,13,21,34,55]
assert fibonacci(7) == return7, 'incorrect return for 7'
assert fibonacci(11) == return11, 'incorrect return for 11'
assert fibonacci(0) == [], 'incorrect return value for 0'
assert fibonacci(1) == [0], 'incorrect return value for 1'

if __name__ == '__main__':
# tests will go here
    print("all good")