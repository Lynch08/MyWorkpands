
a = input("number to get square root of:" )
def newton_method(number, number_iters = 500):

    a = float(number) # number to get square root of
    for i in range(number_iters): # iteration number
        number = 0.5 * (number + a / number) # update
	  # x_(n+1) = 0.5 * (x_n +a / x_n)
    return (float(number))

print (newton_method(a))
# Output: 3
#print (newton_method(2))
# Output: 1.41421356237