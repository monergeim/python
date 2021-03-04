
import random as rnd

def guessing_game():
    number = rnd.randint(0, 100)
    while True:
        n = input('Enter a number between 0 and 100 in order to guess: ')
        if (int(n) > number):
            print("Too big")
        elif (int(n) < number):
            print("Too small")
        else:
            print("Bingo")
            break

guessing_game()
