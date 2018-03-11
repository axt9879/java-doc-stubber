"""
docParser.py
Author: Anthony Tamborini
Description:
    Parses a java doc html page and builds a javaclass.
"""

import requests


def findBetweenTag(data, tag1, tag2):
    """
    Takes in a html page (full or partial) and find content between two HTML Tags.
    :param tag1: string, an html tag
    :param tag2: string, an html tag
    :param data: the data from a request
    :return: a string, the string between the two tags
    """
    tag2
    beginIndex = data.find(tag1) + tag1.__len__()
    endIndex = data.find(tag2)
    returnString = data[beginIndex:endIndex]
    return returnString


def main():
    page = "https://www.cs.rit.edu/~csci142/Projects/Dendron/doc/dendron/tree/ParseTree.html"
    response = requests.get(page)
    data = response.text
    print(findBetweenTag(data, "<title>", "</title>"))


if __name__ == '__main__':
    main()
