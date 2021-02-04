
# Original author: Andrew Beatty
# Code used and comments by: Enda Lynch

# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case
# this program also outputs the lenght of the original string
# and the normalised one

#Requests input, strips leading space and makes all letters lower case
rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()

#gets lenght of Raw string and of normalised string(including space in between words) 
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

#prints result and tells you the lenght at which you have recuced your orig string from and to.
print("That String normalised is :{}".format(normalisedString))
print("we reduced the input string from {} to {} characters".format(
lenghtOfRawString, lenghtOfNormalised ))