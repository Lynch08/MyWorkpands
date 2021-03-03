#See if file exists

import os

filename = "amIhere.txt"

if (os.path.exists(filename)):
    print("File Exists")
else:
    with open(filename, "x") as f:
        print("creating the file")