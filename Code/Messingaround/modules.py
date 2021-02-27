

def readModules():
    modules = []
    moduleName = input("Enter the first module name (blank to quit):").strip

    while moduleName != "":
        module = {}
        module["name"] = moduleName
        #no error handeling
        module["grade"] = int(input("Enter Grade:"))
        modules.append(module)
        #reading in next module
        moduleName = input("Enter next module name (blank to quit):").strip

        return modules
    