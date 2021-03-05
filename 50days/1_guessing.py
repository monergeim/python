
import random as rnd

def guessing_game():
    number = rnd.randint(0, 100)
    while s := input('Enter a number between 0 and 100 in order to guess: '):
        if (int(s) > number):
            print("Too big")
        elif (int(s) < number):
            print("Too small")
        else:
            print("Bingo")
            break

guessing_game()
