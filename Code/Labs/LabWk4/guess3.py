# generates random number for user to guess
# Author: Enda Lynch

# import random module and set limit between 1 and 100
import random
numberToGuess = random.randint(0,100)

#string for user
guess = int(input("Please guess the number between 1 and 100:"))

##'while' sets loop and 'if' and 'else' give prompts 
while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too Low")
    else:
        print ("Too High")
    guess = int(input("Please guess again:"))

 #display when number is correct   
print ("Well done! Yes the number was ", numberToGuess)