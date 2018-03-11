"""
The file that writes everything to a java file. This is the main
file which is going to be run.

Author: Utkarsh Dayal
"""

from docParser import *
from javaclass import *

def getMethodStub(methodName):
    """
    Takes in a method name, and based on what the return type of
    the method is, it returns a return statement as a string

    :param methodName: name of the method
    :return: the return statement for the method stub
    """
    if " void " in methodName:
        return ""
    elif " int " in methodName or " double " in methodName:
        return " return 0; "
    elif " float " in methodName:
        return " return 0.0; "
    elif " String " in methodName:
        return " return "" "
    elif " boolean " in methodName:
        return " return false; "
    else:
        return " return null; "


def writeMethods(file,dict):
    """
    Takes a .java file and a dictionary containing the methods for
    a java class, and then stubs out the methods in the file

    :param file: the java file
    :param dict: the dictionary of methods
    """
    for name in dict.keys():
        docString = dict[name][1]
        methodName = dict[name][0]
        file.write( "\t/*\n")
        file.write("\t* " + docString + "\n")
        file.write("\t*/\n")
        file.write("\t" + methodName + "{" + getMethodStub(methodName) + "}\n")
        print()

def writeFields(file,dict):
    for name in dict.keys():
        docString = dict[name][1]
        infoName = dict[name][0]
        file.write("\t/*\n")
        file.write("\t* " + docString + "\n")
        file.write("\t*/\n")
        file.write("\t" + infoName + "\n")

def main():
    page = "https://www.cs.rit.edu/~csci142/Projects/Dendron/doc/dendron/tree/ParseTree.html"
    response = requests.get(page)
    data = response.text
    className = findBetweenTag(data, "<title>", "</title>")
    classAccess = findBetweenTag(data, "<pre>", "<span")
    java = JavaClass(className[0],classAccess[0])
    methods = findAllMethods(data)
    for method in methods.keys():
        java.addToClass("method",method,methods[method])
    file = open("ParseTree.java","w")
    file.write(java.getAccessModifier() + java.getName() + "{\n")
    writeMethods(file,java.getMethods())
    file.write("}")

if __name__ == '__main__':
    main()