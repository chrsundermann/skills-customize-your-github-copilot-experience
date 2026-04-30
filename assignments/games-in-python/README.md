# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python using loops, conditionals, and strings. In this assignment, you will practice managing game state, validating user input, and creating a fun command-line game experience.

## 📝 Tasks

### 🛠️	Build the Core Hangman Loop

#### Description
Create a Hangman game that randomly selects a word and allows the player to guess one letter at a time until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select one word from the provided word list.
- Display the hidden word as underscores for unguessed letters (for example: `_ _ _ _ _ _`).
- Prompt the user to enter one letter per turn.
- Reveal correctly guessed letters in all matching positions.
- Decrease remaining attempts only when the guess is incorrect.
- Stop when the full word is guessed or no attempts remain.


### 🛠️	Handle Input and End Messages

#### Description
Improve the game so it handles user input cleanly and gives clear feedback when the game ends.

#### Requirements
Completed program should:

- Reject invalid guesses (such as empty input, multiple characters, numbers, or symbols).
- Prevent duplicate guesses from reducing attempts more than once.
- Show the player which letters have already been guessed.
- Print a clear win message when the player guesses the word.
- Print a clear lose message with the correct word when attempts reach zero.
