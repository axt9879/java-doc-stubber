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


if __name__ == '__main__':
    test()