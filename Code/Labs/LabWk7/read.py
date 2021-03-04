#Write a function that reads in a number from a file that already exists
#(count.txt). test the program by calling the function and outputting the number.
#Author: Enda Lynch
#REF: Labsheet for Wk07, Andrew Beatty
import os
os.chdir('/Topic07files/count.txt')
f = open('count.txt', 'r')

filename = ".\count.txt"

def readNumber():
    with open (filename) as f:
        number = int(f.read())
        return number

#test
num = readNumber()
print (num)



