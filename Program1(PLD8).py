#Assignment 8

#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import random

def Wnumbers():
    intp1 = int(input("Enter your First number: "))
    intp2 = int(input("Enter your Second number: "))
    intp3 = int(input("Enter your Third number: "))

    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    user = (intp1, intp2, intp3)
    win = (num1, num2, num3)
    lose = (num1, num2, num3)
    if  user == win:
        print("You, Win")
        print(win)
    else:
        print("You, Lose")
        print(f"Lottery Number are {lose}.")

def Play():
    play = input("You want to continue Y/N?\n")
    if play == ("Y") or ("y") or ("YES") or ("Yes") or ("yes"):
        print(Wnumbers())
        print(Play(),Play(),Play(),Play(),Play(),Play(),Play(),Play(),Play(),Play(),Play())
    else:
        print("Done")
Wnumbers()
Play()

