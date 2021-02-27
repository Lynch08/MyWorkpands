#generate primes
#Author: Enda Lynch

primes = []
upto = 1000

for candidate in range(2, upto):
    #print (candidate) 
    isPrime = True
    #for divisor in range(2, candidate):
    for divisor in primes:
        #if divisable by and int it is not a prime number    
        if (candidate % divisor == 0):
            isPrime = False
            break

    if isPrime:
        primes.append(candidate)

print (primes)