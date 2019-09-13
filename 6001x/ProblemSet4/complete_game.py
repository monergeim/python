#!/usr/bin/env python

def playGame(wordList):
    prevh = {}
    
    while True:
        i = raw_input("\nEnter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if i == "n":
            hand = dealHand(HAND_SIZE)
            prevh = hand
            uorc(hand, wordList, HAND_SIZE)#find vars  
        elif i == "r":
            if prevh == {}:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                uorc(prevh, wordList, HAND_SIZE)#check
        elif i == "e":
            break
        else:
            print "Invalid command."
        
def uorc(hand,wl,n):
    inp = ""
    while inp != "u" or inp != "c":
        inp = raw_input("\nEnter u to have yourself play, c to have the computer play: ")
        if inp == "u":
            playHand(hand, wl, n)#find vars
            break
        elif inp == "c":
            compPlayHand(hand, wl, n)#find vars
            break
        else:
            print "Invalid command."
    
