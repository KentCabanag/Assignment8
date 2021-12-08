#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.
print("\n>>\33[33;4mGUESS A NUMBER FROM 0 TO 100\33[0m<<\n")
import random

user = int(input("\33[32;3mEnter you Guess Number here\33[0m: "))
randNum = random.randint(0,100)

while randNum != user:
    if user > randNum:
        print("\n\33[3mYour Guess number is Greater than the random number\33[0m.\n \33[34;3mTry Decreasing your inputed Number\33[0m")
        user = int(input("\n\33[32;3mEnter another Guess Number here\33[0m: "))
        if user == randNum:
            print("\n\33[35;4mYou Guessed the Number correctly\33[0m")
            print(f"\33[35;4mThe random Number is\33[0m \33[33;1m{randNum}\33[0m.")
            break
    elif user < randNum:
        print("\n\n\33[3mYour Guess number is Less than the random number\33[0m.\n \33[34;3mTry Increasing your inputed Number\33[0m")
        user = int(input("\n\33[32;3mEnter another Guess Number here\33[0m: "))
        if user == randNum:
            print("\n\33[35;4mYou Guessed the Number correctly\33[0m")
            print(f"\33[35;4mThe random Number is\33[0m \33[33;1m{randNum}\33[0m.")
            break
