def lessThan4(aList):
    bList = []
    for o in aList:
        if len(o) <4:
            bList.append(o)
    return bList
aList = ["apple", "cat", "dog", "banana"]
print lessThan4(aList)