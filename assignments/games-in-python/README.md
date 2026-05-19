
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build the classic Hangman word-guessing game in Python to practice string manipulation, loops, conditionals, and user input handling.

## 📝 Tasks

### 🛠️ Implement the Game Logic

#### Description
Create a runnable Python program that picks a secret word, accepts letter guesses from the player, and displays the word progress and remaining attempts until the game ends.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list.
- Accept single-letter guesses (case-insensitive) and update the displayed progress (e.g., _ a _ _ m _ _ ).
- Track and display incorrect guesses and remaining attempts.
- Prevent counting repeated correct guesses as additional wrong attempts.
- End the game with a clear win or lose message and reveal the word when lost.

### 🛠️ (Optional) Add Enhancements

#### Description
Add one or more optional features to improve the game experience.

#### Requirements
Completed enhancements may include (pick at least one):

- Allow guessing the full word.
- Show previously guessed letters.
- Read the word list from an external file (e.g., `data.csv` or `words.txt`).
- Add ASCII-art hangman stages for each wrong guess.

## Example

Playthrough snippet (example):

- Secret word: "python"
- Player guesses: `p` → progress: p _ _ _ _ _
- Player guesses: `y` → progress: p y _ _ _ _
- Wrong guess: `a` → remaining attempts: 5

---

Follow the project assignment template in `templates/assignment-template.md` and keep this file named `README.md`.
