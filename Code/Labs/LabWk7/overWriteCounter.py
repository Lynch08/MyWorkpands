#Write a program that, uses these two functions, to count how many times the
# program has been run. Test it, check to see that the number goes up each time.
#Enda Lynch
#REF: Andrew Beatty Labnote Wk7

filename = '.\Topic07files\counter.txt'

def readNumber():                       #create function to read the number
    with open(filename) as f:           #open 'filename'
        number = int(f.read())          #read the number from the file (needs to be an integer to add 1 later)
        return number                   #return the number

def writeNumber(number):                #create function to write the number returned from readNumber
    with open (filename, 'wt') as f:    #open file so it can be overwritten
        f.write(str(number))            # write takes a string so we need to convert
        
        

num = readNumber()                      #set num as the number returned from readNumber
num += 1                                # add 1
print("we have run this programme {} times".format(num))            
writeNumber(num)                        # call function writeNumber to overwrite 'filename'