#write a program to produce the game and guessing a random number from 1-10
import random

print("Welcome to the guessing game")
print("I'm thinking of a number between 1 and 10")
number = random.randint(1,10)
while True:
    guess = int(input("What is your guess? "))

    if guess == number:
        print("You guessed it right!")
        break
    elif guess > number:
        print('Too high')
    else:
        print('Too low')