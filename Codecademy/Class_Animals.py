import string

def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    #x=''
    lowDict = {}
    upDict = {}
    low = string.ascii_lowercase
    up = string.ascii_uppercase
    for y in up:
        if ord(y)+shift > 90:
            t = ord(y)+shift-26
            upDict[y]=chr(t)
        else:
            t = ord(y)+shift
            upDict[y]=chr(t)
    for x in low:
        if ord(x)+shift > 122:
            t = ord(x)+shift-26
            lowDict[x]=chr(t)
        else:
            t = ord(x)+shift
            lowDict[x]=chr(t)
    z = upDict.update(lowDict)
    return upDict
    
    

print buildCoder(3)