# Number Guessing Game

## Project Information
- **Course**: Introduction to Problem Solving & Programming
- **Project Type**: Individual Project
- **Programming Language**: Python 3.x
- **Submission Date**: November 2025

## Problem Statement
Students and beginners often need engaging ways to practice programming concepts like loops, conditionals, functions, and user input handling. Traditional learning can be boring and doesn't provide immediate feedback. This project creates an interactive number guessing game that makes learning Python fun while reinforcing core programming concepts.

## Objectives
The main objectives of this project are:
1. Create an interactive game that helps users practice logical thinking
2. Implement different difficulty levels to challenge users
3. Provide hints and feedback to guide the user
4. Track game statistics and user performance
5. Make the code modular and easy to understand

## Features
- **Three Difficulty Levels**: Easy (1-50), Medium (1-100), Hard (1-200)
- **Smart Hints**: Tells you if your guess is too high or too low
- **Attempt Tracking**: Shows remaining attempts and guess history
- **Input Validation**: Handles invalid inputs without crashing
- **Game Statistics**: Tracks wins and total games played
- **Play Again Option**: Continue playing multiple rounds
- **User-Friendly Interface**: Clear messages and formatted output

## How It Works
1. User selects difficulty level
2. Computer randomly generates a secret number within the range
3. User makes guesses and receives hints
4. Game ends when user guesses correctly or runs out of attempts
5. Statistics are updated and user can play again

## Technologies Used
- **Python 3.x**
- **random module** - For generating random numbers
- **Built-in functions** - input(), print(), int()

## Installation & Setup

### Prerequisites
- Python 3.x installed on your system
- No external libraries required

### Steps to Run
1. Download or clone this repository
2. Open terminal/command prompt
3. Navigate to project directory
4. Run the command:
   ```
   python number_guessing_game.py
   ```
5. Follow on-screen instructions to play

## Code Structure

### Main Functions:
- `welcome()` - Displays welcome message
- `difficulty()` - Lets user choose difficulty level
- `get_guess()` - Takes and validates user input
- `game()` - Main game logic and flow

### Key Concepts Used:
- Functions and modular programming
- Loops (while loops for game flow)
- Conditionals (if-elif-else for game logic)
- Lists (storing guess history)
- Exception handling (for input validation)
- Random number generation

## Screenshots

### Welcome Screen
![Welcome Screen](screenshots/screenshot1.png)

### Gameplay with Hints
![Gameplay](screenshots/screenshot2.png)

### Win Screen
![Win Screen](screenshots/screenshot3.png)

## Development Process

### Phase 1: Planning
- Identified the problem and target audience
- Decided on features and difficulty levels
- Planned the game flow and logic

### Phase 2: Implementation
- Created basic game structure with functions
- Implemented random number generation
- Added difficulty levels and attempt limits
- Developed hint system (too high/too low)
- Added input validation

### Phase 3: Enhancement
- Added guess history feature
- Implemented statistics tracking
- Created play again functionality
- Improved user interface with formatting

### Phase 4: Testing
- Tested all difficulty levels
- Checked edge cases (invalid inputs, boundary values)
- Verified attempt counting and statistics

## Testing

### Test Cases Performed:
1. **Valid Input Test**: Entered numbers within range - ✓ Passed
2. **Invalid Input Test**: Entered letters and symbols - ✓ Handled properly
3. **Boundary Test**: Tested numbers at range limits - ✓ Passed
4. **Win Condition**: Guessed correct number - ✓ Works correctly
5. **Loss Condition**: Used all attempts - ✓ Game ends properly
6. **Statistics Test**: Played multiple games - ✓ Stats update correctly

### Bugs Fixed:
- Fixed issue where invalid input crashed the program
- Corrected attempt counter logic
- Improved hint messages for better clarity

## Challenges Faced
1. **Input Validation**: Had to handle cases where users enter non-numeric values
   - Solution: Used try-except block
2. **Game Loop**: Making sure the game restarts properly
   - Solution: Used while loop with proper exit condition
3. **Statistics Tracking**: Maintaining stats across multiple games
   - Solution: Used variables outside the game function

## What I Learned
- How to structure a program using functions
- Importance of input validation and error handling
- Using random module for unpredictability
- Creating user-friendly interfaces with clear messages
- Debugging and testing programs systematically

## Future Enhancements
- Add a leaderboard system to save high scores
- Implement time-based scoring
- Add sound effects for win/loss
- Create GUI version using Tkinter
- Add multiplayer mode
- Save game history to a file

## Sample Output
```
==================================================
     WELCOME TO NUMBER GUESSING GAME
==================================================

Try to guess the number I'm thinking of!
I'll give you hints along the way.

Choose difficulty level:
1. Easy (1-50, 10 attempts)
2. Medium (1-100, 7 attempts)
3. Hard (1-200, 5 attempts)

Enter your choice (1/2/3): 2

Great! I've picked a number between 1 and 100.
You have 7 attempts. Good luck!

Enter your guess (1-100): 50
Too high! Try a lower number.
Attempts remaining: 6
Your guesses so far: [50]
```

## Conclusion
This project successfully demonstrates core Python programming concepts through an engaging interactive game. The implementation follows good programming practices with modular code structure and proper error handling. The game is fully functional and provides an enjoyable user experience while serving as a practical learning tool.

## Author-
- Name: Pranav Chauhan
- Registration Number: 25BCE11289
- Email: pranav.bce11289@vitbhopal.ac.in

## Repository Information
- GitHub Repository: [Your Repository Link]
- Project Submission Date: November 20, 2025

---
**Note**: This project was created as part of the VITyarthi course assignment and follows all the guidelines provided in the course material.
