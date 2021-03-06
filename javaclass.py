"""
A class that contains about a single class, as read from the javadoc html

Author:  Utkarsh Dayal
"""

class JavaClass:
    def __init__(self, name, access):
        """
        Create the java class

        :param name: name of the class
        :param access: access modifier of the class
        """
        self.name = name
        self.access = access
        self.fields = {}
        self.methods = {}
        self.constructors = {}

    def getName(self):
        """
        Returns the name of the class

        :return: the name
        """
        return self.name

    def getAccessModifier(self):
        """
        Returns the access modifier of the class

        :return: the access modifier
        """
        return self.access

    def getFields(self):
        """
        Returns a dictionary containing the fields of the class, with
        name of the field as the key and a list containing a string of the modifiers
        of the field and the comments for the field as value

        :return: a dictionary containing fields
        """
        return self.fields

    def getMethods(self):
        """
        Returns a dictionary containing the methods of the class, with
        name of the method as the key and a list containing the modifiers
        and docstrings of the method as value

        :return: a dictionary containing methods
        """
        return self.methods

    def addField(self,name,info):
        """
        Takes data about a field of the class and adds it to the class

        :param name: name of the field
        :param info : list containing information about the field
        :return:
        """
        if (name in self.fields.keys()):
            print("The class already contains this field!")
            return
        self.fields[name] = info

    def addMethod(self,name,list):
        """
        Takes data about a method of the class and adds it to the class

        :param name: name of the class
        :param list: list containing information about the class
        :return:
        """
        if (name in self.methods.keys()):
            print("The class already contains this method!")
            return
        self.methods[name] = list

    def addToClass(self,information,name,list):
        """
        Takes in data about the class and stores it according to what type
        of data it is

        :param information: whether it's a method, field, or constructor
        :param name: name of the method, field, or constructor
        :param list: list containing the info
        :return:
        """
        if information == "method":
            if (name in self.methods.keys()):
                print("The class already contains this method!")
                return
            self.methods[name] = list
        elif information == "field":
            if (name in self.fields.keys()):
                print("The class already contains this method!")
                return
            self.fields[name] = list
        elif information == "constructor":
            if (name in self.constructors.keys()):
                print("The class already contains this method!")
                return
            self.constructors[name] = list