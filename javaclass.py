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
        name of the field as the key and a string of the modifiers
        of the field as value

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

    def addField(self,name,modifiers):
        """
        Takes data about a field of the class and adds it to the class

        :param name: name of the field
        :param modifiers: string of modifiers of the field
        :return:
        """
        if (name in self.fields.keys()):
            print("The class already contains this field!")
            return
        self.fields[name] = modifiers

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
