# Creates a list of random numbers
#removes numbers one at a time until list is empty

import random

#set parameters

queue = []             
numberOfNumbers=10
rangeTo=1000000


for num in range(0,numberOfNumbers):                
    queue.append(random.randint(0,rangeTo))         #add random integers to queue

print ("queue is {}".format(queue))                 #print 10 random numbers       

while len(queue) != (0):                            # when the lenght of the queue is not equal to 0
    currentNumber = queue.pop(0)                    # pop out the first element(0)

    #print the number being popped out and remaining numbers in the queue
    print ('currentNumber is: {} and queue is: {}' .format (currentNumber, queue) )
print ('The queue is now empty')                    #inform user the queue has no elements remaining
