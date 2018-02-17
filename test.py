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

    this is probably not where we want to grab constructor data from. This finds constructor summary we should look
    under constructor detail.
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
    # find the constructor and the description
    constructor = None
    description = None


def test4():
    """
    Very similar to test 3 however aiming for Constructor details instead of just
    the constructor's summary

    Since the html contains special characters, a function will be required to
    replace the '&...;' with spaces or something.
    :return:
    """
    r = requests.get("https://cs.rit.edu/~csci142/Labs/04/doc/heroes/Hero.html")
    data = r.text

    # find the contrustor detail part of the page
    constructorAreaIndex = data.find("CONSTRUCTOR DETAIL")

    #find the actual constructor
    constructorStartIndex = data.find("<pre>", constructorAreaIndex) + 5
    constructorEndIndex = data.find("</pre>", constructorStartIndex)
    constructor = data[constructorStartIndex:constructorEndIndex]

    #print the constructor for debugging
    print(constructor)

    #SECTION TO FIND THE CONSTRUCTOR'S COMMENTS INCLUDING THE PARAMETER COMMENTS

    #find the comment
    commentStartIndex = data.find("class=\"block\">", constructorEndIndex) + 14
    commentEndIndex = data.find("</div>", constructorEndIndex)
    comment = data[commentStartIndex:commentEndIndex]

    #print the comment for debugging
    print(comment)
    # print(commentStartIndex, commentEndIndex)

    #find the parameter details
    paramterArea = data.find("paramLabel", commentEndIndex)
    paramDetails = []
    movingIndex = commentEndIndex
    while True:
        result = findParam(data, movingIndex)
        if result[1] == -1:
            break
        paramDetails.append(result[0])
        movingIndex = result[1]
    print(paramDetails)



def findParam(data, index):
    """
    Given an index and some javadoc html, this function finds the next
    parameter name and parameter detail
    The function will stop itself if it reaches "=======" which usually
    means that it has found all the parameters in an area
    :param data: the html data
    :param index: the starting index to search from
    :return:
    """
    #find param name
    paramNameIndex = data.find("<code>", index) + 6
    paramNameEndIndex = data.find("</code>", paramNameIndex)
    paramName = data[paramNameIndex:paramNameEndIndex]

    #find param detail or commment
    paramCommentIndex = data.find("</code>", index) + 7
    paramCommentEndIndex = data.find("</dd>", paramCommentIndex)
    paramComment = data[paramCommentIndex:paramCommentEndIndex]

    enderIndex = data.find("=======", index)

    if paramCommentIndex == -1:
        return (None, None), -1
    elif paramCommentIndex > enderIndex:
        return (None, None), -1
    else:
        return (paramName, paramComment), paramCommentEndIndex




if __name__ == '__main__':
    test4()
