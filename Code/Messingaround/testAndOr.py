#Messing with ANDs and ORs
#Author: Enda Lynch

number = 10
if (number >=0) and (number <= 100):
    print ("valid")


if (number <= 0) or (number >= 100):
    isbad = True
    print("stop")
else:
    isbad = False
    print ("go")