#Write some code to check if the file exists. To do this we will need to import
#os.path and use the isfile() function
#Enda Lynch
#REF Andrew Beatty Lab Wk7

import os
filename = ".\Topic07files\count.txt"

def writeNumber(num):                #create function to write the number returned from readNumber
    with open (filename, 'wt') as f:    # create and open file so it can be overwritten
        f.write(str(num))            #need to write as str

if not os.path.isfile(filename):        #check to see if file is not there
    print ("File does not exist - but i have now created it")   
 #initialise file here
    writeNumber(30)
else:
    print("yes file is there already")