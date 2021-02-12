# This program reads in a students percentage and prints out the corresponding grade
#This also rounds the input to the nearest integer if a decimal is input
#Author : Enda Lynch

percentage = round(float(input("Enter the Percentage: ")))
if percentage <0 or percentage > 100:
    print ("Please enter a number between 1 and 100")
elif percentage < 40:
    print ("FAIL")
elif percentage < 50 :
    print ("PASS")
elif percentage < 60 :
    print ("Merit 2")
elif percentage < 70 :
    print ("Merit 1")
else:
    print ("DISTINCTION")