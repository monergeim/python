#!/usr/bin/env python



def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    
    a = getFrequencyDict(word)
    #print res
    if word in wordList:
        for i in word:
            if hand.get(i, 0) == 0:
                return False
            if a[i] > hand[i]:
                return False
        return True
    else:
        return False