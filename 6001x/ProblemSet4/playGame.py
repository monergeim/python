def playGame(wordList):
    #HAND_SIZE = 7
    prevhand = {}
    while True:
        ans = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if ans == "r":
            if prevhand == {}:
                print "You have not played a hand yet. Please play a new hand first!\n"
            else:
                playHand(prevhand, wordList, HAND_SIZE)
        elif ans == "n":
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
            prevhand = hand.copy()
        elif ans == "e":
            break
        else:
            print "Invalid command."