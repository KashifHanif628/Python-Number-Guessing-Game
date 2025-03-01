# 🎯 Python-Number-Guessing-Game


Welcome to the Number Guessing Game! This is a simple Python-based game where the player has to guess a randomly generated number within a given range and a limited number of attempts.

📌 **Features**

Generates a random number between 1 to 10.

The player gets 5 attempts to guess the correct number.

Provides hints whether the guessed number is too high or low.

Displays a winning message if the player guesses correctly.

Shows the correct number if all attempts are used.

🛠️ **How to Run the Game**

Make sure you have Python installed (Python 3.x recommended).

Clone or download the script to your local machine.

Open a terminal or command prompt and navigate to the script directory.

Run the following command:

python number_guessing_game.py

Start guessing the number!

🚀 **How the Game Works**

The game randomly generates a number between 1 and 10.

You have 5 chances to guess the correct number.

After each guess, the game will give you a hint:

"Your guess is very low, try again!" → if your guess is too low.

"Your guess is very high, try again later!" → if your guess is too high.

"The number is X and you found it right!!" → if you guessed correctly.

If you use all your chances without guessing the number, the game will reveal the correct answer.

📋 **Example Output**

Welcome to the Number Guessing Game!
You got 5 attempts to guess the number between 1 to 10, let's start the game.
Please Enter your Guess: 3
Your guess is very low, try again!
Please Enter your Guess: 7
Your guess is very high, Try again later!
Please Enter your Guess: 5
The number is 5 and you found it right!!

📝 **Notes**

The script uses Python's random module to generate a random number.

Uses a while loop to allow multiple guesses within the limit.

Implements f-strings for formatted output.

If the player guesses correctly, the game ends immediately.

Enjoy playing the game! 🎉

