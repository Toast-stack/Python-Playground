# Number Guessing Game

## Description
The number Guessing Game is a fun and interactive Python project where the computer randomly selects a number within a range, and the player has to guess it. The game provides helpful hints ("Too high" or "Too low") to guide the player and includes error handling to ensure a smooth experience.
This project is beginner-friendly and a great way to practice Python concepts like loops, conditionals, and random number generation.

## Features
- Randomly generates a number between 1 and 100
- Provides hints to guide the player ("Too high" or "Too low").
- Includes error handling for non-numeric inputs.
- Allows the player to quit the game at any time by entering `0`.

## How to Run
1. Ensures Python is installed on your system. Download it [here](https://www.python.org/).
2. Clone or download this project to your computer.
3. Open a terminal, navigate to the project folder, and run the script:
```bash
python Simple_Number_guessing.py
```

## Example Gameplay
```
Welcome to the Number Guessing Game.
I have chosen a number between 1 and 100.
Can you guess what it is?
Enter your guess (or type 0 to quit): 50
Too low! Try again.
Enter your guess (or type 0 to quit): 75
Too high! Try again.
Enter your guess (or type 0 to quit): 63
Congrats! You guessed the number!
```

## Concepts Covered
- **Random Number Generation**: Using Python's `random` module.
- **Loops**: Repeating actions until a condition is met.
- **Conditionals**: Making decisions based on user input.
- **Error Handling**: Managing invalid inputs with `try` and `except`.

## Possible Enhancements
If you'd like to expand this project, consider the following:
1. **Add a Guess Counter**: Track the number of attempts taken by the player.
2. **Custom Ranges**: Let the player define the range of numbers at the start of the game.
3. **Difficulty Levels**: Introduce difficulty levels with smaller or larger ranges.
4. **Replay Option**: Allow players to replay the game without restarting the program.

## Notes
- If you guess the correct number, the game will celebrate your win and end automatically.
- Entering `0` at any point will gracefully exit the game and reveal the correct number.

## Additional Rescources
- Resource: [Python’s `random` Module Guide - Real Python](https://realpython.com/python-random/)
- Tutorial: [Build a Number Guessing Game - YouTube Video Tutorial](https://www.youtube.com/watch?v=8ext9G7xspg) *(video with hands-on instructions)*
- Practice Platform: [Codewars - Beginner Logical Challenges](https://www.codewars.com/)
