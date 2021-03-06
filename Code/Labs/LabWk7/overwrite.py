#Write a function that takes in a number and overwrites a file with that number (count.txt). test it and check that the file has been changed
#Author: Enda Lynch
#REF: Labsheet for Wk07, Andrew Beatty

filename = ".\Topic07files\count.txt"

def writeNumber (number):
    with open (filename, "wt") as f:

        f.write(str(number))


#test
writeNumber("0")