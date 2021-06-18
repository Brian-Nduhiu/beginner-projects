#This game will use user input to compare and guess a number randomly chosen by the system

#System randomly selects a number from a range provided by the user
import random
import os
import sys

startNum = int(input("Select the starting value within the random range "))
endNum = int(input("Select the ending value within the random range ")) 

randomNum = random.randint(startNum, endNum)

#Now the random number has been selected, now the user will try and guess what number it is
tries = 3


while (tries > 0):
    guess = int(input("Guess what the number is: "))
    if(guess == randomNum):
        print("Congrats you guessed correctly!")
        break
    elif(guess > randomNum):
        print("Sorry the guess was too high!")
        tries -= 1
    elif(guess < randomNum):
        print("Sorry the guess was too low!")
        tries -= 1

if(tries == 0):
    print("Sorry you ran out of tries, try again later!")
    os.kill