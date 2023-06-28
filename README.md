# Hangman Game

## Game Rules
You have a limited number of lives to guess the word. The default number of lives is set to 7.

Enter your guess as a single letter. If you enter more than one letter or a word, it will be considered as an incorrect guess.

The game will display the hangman stage and the current state of the word with dashes representing unrevealed letters.

If your guess is correct, the corresponding letters will be revealed in the word.

If your guess is incorrect, the hangman stage will progress, and you will lose one life.

## The game ends in one of two ways:

You correctly guess the entire word and win the game.
You run out of lives, and the game ends in defeat.

## Customizing Word Lists

The game uses different word lists for each difficulty level (easy, medium, hard, and expert). 

The words are stored in a separate module called word_list.py. To customize the word lists, modify the lists in that module.

## File Structure
The Hangman game files are organized as follows:

hangman.py: The main Python file containing the game logic and user interaction code.

word_list.py: A separate module containing word lists for different difficulty levels.

README.md: This file, providing instructions and information about the game.
