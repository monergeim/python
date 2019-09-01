#!/usr/bin/env python

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def isWordGuessed(secretWord, lettersGuessed):
    res = ""
    for l in secretWord:
        for i in lettersGuessed:
            print i
            if i == l:
                res = res + i
                break
        else:
            res = res + "_ "
    return res



print isWordGuessed(secretWord, lettersGuessed)