#messing with lists
# Author: Enda Lynch

list = [2, 4, 6, 8]
more = list + [2, 5, 6]

for x in more:


    print ('element in list: ', x)

for key in range(0, len(more)):
    print ("more[",key,"] = ", more[key])