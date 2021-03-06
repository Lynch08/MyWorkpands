#A programme to input student names and modules and the grades recieved  - using json to store and load the data input
#Author Enda Lynch
#REF - Andrew Beatty, Lab Sheet and Video 6.1
#REF - https://www.w3schools.com/python/python_functions.asp

import json

students  = []
filename = "students.json"

def writeDict(obj):
    with open(filename, 'wt') as fstudents:
        json.dump(obj, fstudents)

def readDict():
    with open (filename) as fstudents:
        return json.load(fstudents)

# This is the initial input - asking the user which function to call
def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(l) Load students")
    print("\t(s) Save Students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q):").strip()
    return choice

#function to add students info that has been inputted
def doAdd():
    currentStudent = {}
    currentStudent ["Name"] = input ("Enter Students Name:")
    currentStudent ["Modules"] = readModules()
    students.append(currentStudent)

#function to  input module information
def readModules():
    modules = []
    moduleName = input("Enter the first module name (blank to quit) :").strip()

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        #no error handeling
        module["grade"] = int(input("\t\tEnter Grade:"))
        modules.append(module)
        #reading in next module
        moduleName = input("Enter next module name (blank to quit):").strip()
        
    return modules
def displayModules(modules):
    print("\tName   \tGrade")
    for module in modules:
        print("\t{}   \t{}".format(module["name"], module["grade"]))

def doView():
    for currentStudent in students: 
        print(currentStudent["Name"])
        displayModules(currentStudent["Modules"])

def doSave():
    writeDict(students)
    print('Students saved')

def doLoad():
    global students             #changeing global variable to students
    students = readDict()
    print ('Students loaded')

choice = displayMenu()
while (choice != 'q'):

    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice == 's':
        doSave()
    elif choice == 'l':
        doLoad()
    elif choice != "q":
        print ("\n\n please select either 'a'/'v'/'q'")
    choice = displayMenu()

