#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

import random

user = int(input("Enter you Guess Number here: "))
randNum = random.randint(0,100)

while randNum in user:
    if user > randNum:
        print("Your Guess is Greater than the random number.\n Try Decreasing your inputed Number")
        user = int(input("Enter another Guess Number here:"))
        if user == randNum:
            print("You Guessed the Number correctly")
            print(f"The random Number is {randNum}.")
            break
    elif user < randNum:
        print("Your Guess is Less than the random number.\n Try Increasing your inputed Number")
        user = int(input("Enter another Guess Number here:"))
        
