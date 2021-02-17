#messing with dictionaries
# Author: Enda Lynch

car = {
    "make": "ford",
    "price": 123,
    "owner": {
        "firstName" : "Fred",
        "age" : 12
    }
}
for x in car:
    print(car[x])

for x, y in car.items():
    print(x,y)

print (type(car))
print (car)

car ["model"] = "focus"
print (car)


#make = car["make"]
#notMake = car.get("kjgasgd")
#print (notMake)
#print (make)
print (car["owner"]["age"])