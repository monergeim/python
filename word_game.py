def playHand(hand, wordList, n):
    tscore = 0
    updhand = hand.copy()
    while calculateHandlen(updhand) > 0:
        print "Current Hand: ",
        for key in updhand:
            if updhand[key] > 0:
                for c in range(updhand[key]):
                    print key,
        i = raw_input("\nEnter word, or a \".\" to indicate that you are finished: ")
        if i == ".": #sometimes not so useful condition better if i < 2:
            print "Goodbye!",
            break
        else:
            if isValidWord(i, updhand, wordList) == False:
                print "Invalid word, please try again.\n"
            else:
                wscore = getWordScore(i, n)
                tscore += wscore
                print "\"" + i + "\"" + " earned " + str(wscore) + " points. Total: " + str(tscore) + " points\n"
                updhand = updateHand(updhand, i)
                if calculateHandlen(updhand) == 0:
                    print "Run out of letters. ",
                    break#maybe not required
    print "Total score: " + str(tscore) + " points."