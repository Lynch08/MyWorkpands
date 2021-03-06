#reading data (dicts) using JSON
#Enda Lynch
#REF Andrew Beatty Lab Wk7


import json
filename = '.\Topic07files\TestDict.json'


def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty dict
    with open (filename) as f:
        return json.load(f)

#test
goats = readDict()
print(goats)


