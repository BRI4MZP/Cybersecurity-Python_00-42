from random import randint
import string

number = randint(1, 99)
attemps = 0
print("	This is an interactive guessing game!\n	You have to enter a number between 1 and 99 to find out the secret number.\n	Type 'exit' to end the game.\n	Good luck!")
while True:
    attemps+=1
    choice = input("What's your guess between 1 and 99?\n")
    print(choice)
    if choice == "exit":
        quit("good bye :)")
    if int(choice) > number:
        print("Too high!")
    elif int(choice) < number:
        print("Too low!")
    elif int(choice) == number:
        quit("Congratulations, you've got it!\nYou won in {} attemps".format(attemps))
    else:
        print("Thats not a number")