#Write a function that reads in a number from a file that already exists
#(count.txt). test the program by calling the function and outputting the number.
#Author: Enda Lynch
#REF: Labsheet for Wk07, Andrew Beatty

#import os


filename = ".\Topic07files\count.txt"           #file loc and name

def readNumber():                               #create function to read file
    with open (filename) as f:                  # open file
        number = int(f.read())                  #read file
        return number                           #retuen values in file

#test
num = readNumber()                              
print (num)



