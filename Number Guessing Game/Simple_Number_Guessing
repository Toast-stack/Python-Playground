import random

# Welcome message
print("Welcome to the Number Guessing Game.")
print("I have chosen a number between 1 and 100. \nCan you guess what it is?")

# Randomly select a number 
target_number = random.randint(1, 100)

while True:
    try:
        # Get the user's guess
        guess = int(input("Enter your guess (or type 0 to quit): "))

        # Check if the user wants to quit
        if guess == 0:
            print("Thanks for playing! The number was:", target_number)
            break

        # Provide Feedback
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congrats! You guessed the number!")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")
