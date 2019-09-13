#!/usr/bin/env python

secretWord = 'apple' 

def hangman(secretWord):
    x=8
    mistakesMade = 0
    lettersGuessed = [0]
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."

    while x > 0:
        print "-----------"
        if isWordGuessed(secretWord, lettersGuessed) == True:
            return "Congratulations, you won!"
            break
        print "You have " + str(x) + " guesses left."
        print "Available Letters: " + getAvailableLetters(lettersGuessed)
        guess = raw_input("Please guess a letter: ")
        guesslowlet = guess.lower()
        if guesslowlet  in 'abcdefghijklmnopqrstuvwxyz':
            if guesslowlet in lettersGuessed:
                print "Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed)
            else:
                lettersGuessed.append(guesslowlet)
                if guesslowlet in secretWord:
                    print "Good guess: " + getGuessedWord(secretWord, lettersGuessed)
                else:
                    x-=1
                    print "Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed)
        else:
            print "Wrong input, use letters!"
        if x == 0:
            print "-----------"
            return "Sorry, you ran out of guesses. The word was else."  

    	
    
    
    
def isWordGuessed(secretWord, lettersGuessed):
    for l in secretWord:
        for i in lettersGuessed:
            if i == l:
                res = True
                break
        else:
            res = False
        if res == False:
            break
    return res


def getAvailableLetters(lettersGuessed):
    out = ""
    prnlist = "abcdefghijklmnopqrstuvwxyz"
    for l in lettersGuessed:
        for i in prnlist:
            if i != l:
                out = out + i
        else:
            prnlist = out
            out = ""
    return prnlist

def getGuessedWord(secretWord, lettersGuessed):
    res = ""
    for l in secretWord:
        for i in lettersGuessed:
            if i == l:
                res = res + i
                break
        else:
            res = res + "_ "
    return res

print hangman(secretWord)