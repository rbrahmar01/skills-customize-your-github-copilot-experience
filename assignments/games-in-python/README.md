
# 📘 Assignment: Hangman Game

## 🎯 Objective
Build a text-based Hangman game that practices string manipulation, loops, conditionals, and basic state tracking while handling user guesses interactively.

## 📝 Tasks

### 🛠️ Set Up Game Data
#### Description
Create the core data structures for the game, including the secret word source and variables for tracking progress. Use the provided `starter-code.py` file as a scaffold if included in this folder.
#### Requirements
Completed program should:

- Store a list of at least 8 possible words
- Randomly select one secret word at game start
- Initialize a masked display using underscores for each letter
- Track a set or list of guessed letters
- Define a maximum number of incorrect guesses (e.g., 6)

### 🛠️ Process Player Guesses
#### Description
Implement the input loop that repeatedly asks the player to guess a single letter and updates the game state based on correctness.
#### Requirements
Completed program should:

- Prompt the user for a single letter each turn
- Reject input that is not a single alphabetic character and reprompt
- Prevent duplicate guesses and inform the player if a letter was already tried
- Reveal all positions of correctly guessed letters in the masked word
- Decrement remaining attempts only for incorrect, new guesses

### 🛠️ Display Game Status
#### Description
Show clear feedback after each guess so the player understands progress and remaining chances.
#### Requirements
Completed program should:

- Display the masked word with spaces between unrevealed letters (e.g., `_ a _ _ n`)
- Show the number of incorrect guesses remaining after each turn
- List previously guessed letters in alphabetical order
- Provide a win message when all letters are revealed
- Provide a loss message showing the secret word when attempts reach zero

### 🛠️ Optional Enhancements
#### Description
Add polish or extra challenge features without breaking the core gameplay. These are optional and not required for completion.
#### Requirements
Completed program should (if enhancements added):

- Offer difficulty levels that adjust allowed attempts
- Draw a simple ASCII hangman progression
- Allow replay without restarting the script

---
Example interaction (truncated):
```
Word: _ _ _ _ _
Guesses remaining: 6
Enter a letter: a
Word: a _ a _ _
Guesses remaining: 6
Letters tried: a
...
```

Keep code readable: use functions to separate concerns (e.g., input handling, status display, win/loss detection).
