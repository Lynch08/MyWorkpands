# Prompts user to guess a number
# Author: Enda Lynch

numberToGuess = 30

guess = int(input("Please guess the number:"))

while guess != numberToGuess:
    if guess < numberToGuess:
        print ("Too Low")
    else:
        print ("Too High")
    guess = int(input("Please guess again:"))
    
print ("Well done! Yes the number was ", numberToGuess)