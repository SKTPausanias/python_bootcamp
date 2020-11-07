#!/usr/bin/python

import random
import sys

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and"
      " 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

sol = random.randint(1, 99)
trialnum = 1

while 1:
    print("What's your guess between 1 and 99?")
    n = input(">> ")
    try:
        if n == "exit":
            sys.exit("Goodbye!")
        num = int(n)
        if num == sol:
            if num == 42:
                print("The answer to the ultimate question of life,"
                      " the universe and everything is 42.")
            if trialnum == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("You won in", trialnum, "attempts!")
            sys.exit(0)
        elif num > sol:
            print("Too high!")
        else:
            print("Too low!")
        trialnum += 1
    except ValueError:
        print("That's not a number.")
