#!/usr/bin/env python

def FancyDivide(numbers,index):
    print len(numbers)
    try:
        denom = numbers[index]
        for i in range(len(numbers)):
            numbers[i] /= denom
    except IndexError, e:
        print "-1"
    else:
        print "1"
        print numbers
    finally:
        print "0"
        print numbers
        
print FancyDivide([0, 2, 4], 1)
