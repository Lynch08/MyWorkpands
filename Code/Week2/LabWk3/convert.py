#I am writing an application at the moment, in it I take an input of an amount 
# in the form -9.44 (9 dollars and 44 cent), the issue there may or may not be a
#minus sign, and the bank takes in the amount in cent, (944). Write a program
#called convert.py that takes in a float amount of dollars, and returns that
#absolute amount in cent.

dollar = float(input('Put in $ amt ($-x.xx for deposit):'))

dollarToCent = (dollar*float(100))

print ('Your deposit in cents is:', (int(abs(dollarToCent))))