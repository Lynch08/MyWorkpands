#Storing data (dicts) using JSON
#Enda Lynch
#REF Andrew Beatty Lab Wk7

import json
filename = '.\Topic07files\TestDict.json'

goats = dict(nfl = 'Tom Brady', soccer = 'Messi', hurling = 'DJ', basketball = ['MJ', 'LBJ'])

def writeDict(obj):
    with open (filename, 'wt') as f:
        json.dump(obj, f)

#test
writeDict(goats)