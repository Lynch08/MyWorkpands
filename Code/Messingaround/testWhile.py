#Messing with WHILE statments
#Author: Enda Lynch

#While Condition
#Counter controlled loop
count = 10
while count >= 0: 
    print (count)
    count -=1
print ("Blast Off")


val = input ("type some (q to quit): ")
while val != 'q':
    print ("you said: " + val)
    val = input ("(q to quit):")