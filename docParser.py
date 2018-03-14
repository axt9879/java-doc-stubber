"""
docParser.py
Author: Anthony Tamborini
Description:
    Parses a java doc html page and builds a javaclass.
"""

import javaclass
import requests


def findBetweenTag(data, tag1, tag2, start=0):
    """
    Takes in a html page (full or partial) and find content between two HTML Tags.
    :param start: where to start searching for tags in the html text data
    :param tag1: string, an html tag
    :param tag2: string, an html tag
    :param data: the data from a request
    :return: a tuple, (the string between the two tags, the index of the second tag)
        the index of the second tag is useful for a start point for the next findBetweenTag
    """

    beginIndex = data.find(tag1, start) + tag1.__len__()
    endIndex = data.find(tag2, beginIndex)
    returnString = data[beginIndex:endIndex]
    returnString = removeOddStuff(returnString)
    return returnString, endIndex


def findAllMethods(data):
    """
    Parses through the specific string of html data that contains only the methods details
    :param data: the html data
    :return: a dictionary of
            key         :   value
            methodName  :   (method signature, method description, dict of params, returnDetails(String or None))
    """
    methods = {}
    data = data[data.find("<!-- ============ METHOD DETAIL ========== -->"):data.find("<!-- ========= END OF CLASS "
                                                                                      "DATA ========= -->")]
    index = 0
    while data.find("name=", index) != -1:
        methodName = findBetweenTag(data, "name=\"", "\">", index)
        index = methodName[1]
        if methodName[0].__contains__("method.detail"):
            continue

        # get method signature
        method = findBetweenTag(data, "<pre>", "</pre>", index)

        # get method description
        methodDescription = findBetweenTag(data, "\"block\">", "</div>", index)

        # get parameters
        params = {}
        j = 0
        if data.find("paramLabel", index) != -1:
            index = data.find("paramLabel", index)
            while data.find("<dd><code>", index) != -1 and data.find("<dd><code>", index) < data.find("<a name=", index):
                if j > 10:
                    break
                paramName = findBetweenTag(data, "<dd><code>", "</code>", index)
                paramDetails = findBetweenTag(data, "</code> - ", "</dd>", paramName[1])
                params[paramName[0]] = paramDetails[0]
                index = paramDetails[1]
                j += 1

        # get return
        returnDetails = None
        if (data.find("returnLabel", index) != -1 and data.find("returnLabel", index) < data.find("<a name=", index)) or\
                (data.find("returnLabel", index) != -1 and data.find("<a name=", index) == -1):
            index = data.find("returnLabel", index)
            returnDetails = findBetweenTag(data, "<dd>", "</dd>", index)[0]

        methods[methodName[0]] = (method[0], methodDescription[0], params, returnDetails)
    return methods


def findAllFields(data):
    methods = {}
    data = data[data.find("<!-- ============ FIELD DETAIL =========== -->"):data.find("<!-- ========= CONSTRUCTOR ")]
    index = 0
    while data.find("name=", index) != -1:
        methodName = findBetweenTag(data, "name=\"", "\">", index)
        index = methodName[1]
        if methodName[0].__contains__("field.detail"):
            continue

        # get method signature
        method = findBetweenTag(data, "<pre>", "</pre>", index)

        # get method description
        methodDescription = findBetweenTag(data, "\"block\">", "</div>", index)

        methods[methodName[0]] = (method[0], methodDescription[0])
    return methods

def removeOddStuff(string):
    """Takes a string and removes '<', '>' and everything between them
    also removes weird html characters that don't translate to plain text
    :param string: the string to clean
    :return: the cleaned string
    """
    # remove html first
    i = 0
    while string.find("<") != -1:
        if i > 5:
            break
        start = string.find("<")
        end = string.find(">")
        if start != -1 and end != -1:
            string = string[:start] + string[end + 1:]
        i += 1

    # remove - amd -- and replace the single dashes with < then >
    i = 0
    while string.find("-") != -1:
        if i > 5:
            break
        i += 1
        start = string.find("-")

        next1 = -1
        if string.find("-", start) != -1:
            next1 = string.find("-", start + 1)
            isAnother = True
        else:
            isAnother = False

        # if start + 1 < string.__len__() - 1:
        if start < string.__len__() -1:
            if string[start] == string[start + 1] == "-":
                string = string[:start] + string[start + 2:]
        if start < string.__len__() -2:
            if string[start] != string[start + 1] and isAnother:
                string = string[:start] + " <" + string[start+1:next1] + "> " + string[next1 + 1:]

    # remove symbols
    symbols = {"&nbsp;": " ", "&#8203;": "", "&lt": "<", "&gt": ">", "\n": "", ";": ""}
    for i in symbols.keys():
        string = string.replace(i, symbols[i])

    return string

def WHITESPACE():
    return "    "

def main():
    page = "https://www.cs.rit.edu/~csci142/Projects/Dendron/doc/dendron/tree/BinaryOperation.html"
    response = requests.get(page)
    data = response.text
    className = findBetweenTag(data, "<title>", "</title>")
    classAccess = findBetweenTag(data, "<pre>", "<span")
    classExtends = findBetweenTag(data, "</span>", "</pre>", start=classAccess[1])
    startConstructors = data.find("<!-- ========= CONSTRUCTOR DETAIL ======== -->")
    classConstructor = findBetweenTag(data, "<pre>", "</pre>", start=startConstructors)
    classConstructorParams = findBetweenTag(data, "<code>", "</dl>", classConstructor[1])

    # print found information
    print("Class Name:", className)
    print("Class Access", classAccess)
    print("Class Extends", classExtends)
    print("Class Constructor", classConstructor)
    print("Class Constructor Params", classConstructorParams, "\n")
    methods = findAllMethods(data)
    fields = findAllFields(data)
    print("\nMethods")
    print("=======")
    for method in methods:
        print(method, "\n\t", methods[method])
    print("\nFields")
    print("======")
    for field in fields:
        print(field, "\n\t",  fields[field])
    print("\n", fields)


    #make the javaclass

    java = javaclass.JavaClass(className[0],classAccess[0])
    for method in methods.keys():
        java.addToClass("method",method,methods[method])

    print()
    print("Testing JavaClass...")
    print(java.getAccessModifier()=="public class ")
    print(java.getName()=="ParseTree")
    jMethods = java.getMethods()
    for name in jMethods.keys():
        print(jMethods[name] == methods[name])
    print("Test complete!")



    print()
    print("Attempting to write to file...")
    file = open("ParseTree.java","w")
    file.write(java.getAccessModifier() + java.getName() + "{ \n")
    for name in jMethods.keys():
        if name == "compile":
            continue
        file.write(WHITESPACE() + jMethods[name][0] + "{} \n")
    file.write("}")
    print("Writing completed without any errors!")

if __name__ == '__main__':
    main()


