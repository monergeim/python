def myLog(x, b):
    if x < b:
        return 0
    else:
        return myLog(x/b, b) + 1

print myLog(15, 3)