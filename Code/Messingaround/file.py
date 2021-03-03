#Messing with Files
#From video 7.1
#Enda Lynch

#with open (".\week07files.txt", "w") as f:
    #print ('create a file')

with open("TestData.txt", "rt") as f:
    #data = f.read(6)
    #print(data)
    for line in f:
        print("we got line:", line.strip())


with open (".\week07files.txt", "wt") as f:
    f.write("Hello Enda again \n TEST")
    print("my data", file = f)
