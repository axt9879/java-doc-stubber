"""
Messing around with the requests module to see how it works

Author: Anthony Tamborini
"""

import requests

def test():
    """
    Gets a javadoc, slices the text in the html document from the start of the
    class data till the end
    """
    r = requests.get("https://cs.rit.edu/~csci142/Labs/04/doc/game/HeroStorm.html")
    info = r.text
    start = info.find("START OF CLASS DATA")
    end = info.find("END OF CLASS DATA")
    info = info[start:end]
    print(info)
    test2(r)


def test2(r):
    """
    Takes the requested data, finds the indexes of the html where the string "========" is
    and puts all those indexes in a list and prints the list

    :param r: the requested data
    """
    indexAdjust = 5
    info = r.text
    lst = [0]
    i = 0
    while True:
        addThis = info.find("========", lst[i]+5)
        if addThis == -1:
            break
        lst.append(addThis)
        i += 1
    print(lst)
    # print(info[1669-indexAdjust:3898+indexAdjust])


def test3():
    """
    I am testing on getting data for the constructor for a class
    :return:
    """
    r = requests.get("https://cs.rit.edu/~csci142/Labs/04/doc/heroes/Hero.html")
    data = r.text
    # find the constructor table
    constructorIndex = data.find("Constructor</th>")
    # find the index of the first table column with the <code> tag. this is usually the constructor modifier
    modifierIndex = data.find("colFirst\"><code>", constructorIndex)
    modifierEndIndex = data.find("</code>", modifierIndex)
    # save the slice of data between the two indexes to get the modifier
    constructorModifier = data[modifierIndex + len("colFirst\"><code>"):modifierEndIndex]
    print(constructorIndex, modifierIndex, modifierEndIndex)
    print(constructorModifier)


if __name__ == '__main__':
    test3()
