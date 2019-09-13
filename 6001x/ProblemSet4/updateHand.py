#!/usr/bin/env python
import copy
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = "quail"

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    res = copy.deepcopy(hand)
    #print res
    for i in word:
        if hand.get(i, 0) == 0:
            return "Incorrect letter"
        res[i] = res[i] - 1
    return res
        


def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


print updateHand({'a': 2, 'c': 2, 'l': 2, 'p': 3, 'r': 2, 't': 2}, "claptrap")
