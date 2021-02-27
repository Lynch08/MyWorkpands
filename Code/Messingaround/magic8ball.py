#random generator with functions
#From Python:Automate the Boring Stuff
#Enda Lynch

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is Certain'
    elif answerNumber == 2:
        return 'it may be so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'mmmm dunno'
    elif answerNumber == 5:
        return 'im tired - ask later'
    elif answerNumber == 6:
        return 'not looking good'
    elif answerNumber == 7:
        return 'forget about it - no way'

print(getAnswer(random.randint(1, 7)))