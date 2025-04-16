import random

# Welcome message
print("Welcome to Rock-Paper-Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play. Type 'quit' to exit.")

# Possible choices
choices = ['rock', 'paper', 'scissors']

while True:
    # User in
    user_choice = input("Your choice: ").lower()

    # Checks if the user wants to quit
    if user_choice == 'quit':
        print("Thanks for playing!")
        break

    # Checks for valid input
    if user_choice not in choices:
        print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
        continue
    
    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win!")
    else:
        print("You lose!")
