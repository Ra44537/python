#Guess a number game

import random

target = random.randint(1, 5)

while True:
    choice = int(input("choice a number or Quit(Q)"))
    if(choice == "Q"):
        break

    choice = int(choice)
    if(choice == target):
        print("correct choice")
        break

    elif(choice < target):
        print("You number is too small. Take a bigger guess..")
    else:
        print("You number is too large. Take a smaller guess..")    




print("-----Game Over-----")