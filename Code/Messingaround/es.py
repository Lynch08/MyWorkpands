#reading all the e's from a text file
#Author Enda Lynch

import sys
filename = sys.argv[1]

def readLetter(filename, letter):               #create function to read file
    with open (filename) as f:                  # open file
        text = f.read()                         #read file
        count = 0                               #count begins at:0
        for char in text:                       #loop for char
            if char == letter:
                count += 1                      #+1 every time char is found
        return count                            #return number of characters

print(readLetter(filename, 'e'))       