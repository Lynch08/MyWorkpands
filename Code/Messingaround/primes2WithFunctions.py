#generate primes
#Author: Enda Lynch

import math

primes = []
upto = 10

def isPrime(candidate):
    #check if it is a prime
    for divisor in range(2, math.floor(math.sqrt(candidate))):
        #if divisable by and int it is not a prime number    
        if (candidate % divisor == 0):
            return False
    return True

for candidate in range(2, upto+1):
    #for divisor in range(2, candidate):
    if isPrime(candidate):
        primes.append(candidate)
print (primes)

