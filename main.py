# random is a module which we are imporing to generate the randomly number.
import random

print("Welcome to the Number Guessing Game! /n you got 5 attempts to guess the number between 1 to 10, lets start the game.")

# loop to generate the random value number between 50 to 100.
number_to_guess = random.randrange(1, 10)

# user has chances to attempt the currect number.
chances = 5

guess_counter = 0

#while loop if user has not started to guess and #make a variable of my_guess to get the input from user.
#while loop uper ki teeno condition ko chalayga pehla random number generate, dusra given 5 chances and third start with 0 count
while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Please Enter your Guess: "))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you find it wright!! in the {guess_counter} attempt.")
        break # if user found the correct number then game has terminate here.
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops! sorry, the number is {number_to_guess} better luck next time!")

    elif my_guess < number_to_guess:
        print("your guess is very low, try again!")

    elif my_guess > number_to_guess:
        print(f"Your guess is very high, Try again later!")

# basically f"" is used in python for dynamically statement print. same like we use baktiks in Nextjs.