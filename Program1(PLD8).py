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

print("\n >>\33[33;1mLOTTERY\33[0m<<")
play = True
while play:
    print("\n\33[32;1mJust Enter three digit numbers from 0 to 9\33[0m")
    intp1 = int(input("\n\33[31;1mEnter your First number\33[0m: "))
    intp2 = int(input("\33[31;1mEnter your Second number\33[0m: "))
    intp3 = int(input("\33[31;1mEnter your Third number\33[0m: "))

    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    num3 = random.randint(0,9)
    user = intp1, intp2, intp3
    lose = (num1, num2, num3)
    if  user == num1 and num2 and num3:
        print("\33[33;1mWinner\33[0m")
        print(lose)
    else:
        print(f"\33[36;1mWinning Number are \33[0m{lose}.")        
        print("\33[33;4mYou Loss\33[0m")
        print(f"\33[32;1mYour input Number are\33[0m {user}")

    ans = input("\n\33[34;1mYou want to continue Yes or No\33[0m?:\n").lower()
    while True:
        if ans == "no":
            print("\33[35;1mThanks for playing\33[0m")
            play = False
            break
        elif ans == "yes":
            play = True
            break