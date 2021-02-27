#A programme to input student names and modules and the grades recieved
#Author Enda Lynch
#REF - Andrew Beatty Lab Sheet and Video 6.1
#REF - https://www.w3schools.com/python/python_functions.asp

students = []
def readModules():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent ["Name"] = input ("Enter Students Name:")
    currentStudent ["Modules"] = readModules()

    students.append(currentStudent)

#test
doAdd(students)

print(students)