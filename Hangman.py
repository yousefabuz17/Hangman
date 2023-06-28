from random import choice
from word_list import *
from dictionary_api import dictionary



class Hangman:
    def __init__(self, difficulty: str):
        """
        Initialize the Hangman game with the specified difficulty level.
        """
        self.difficulty = difficulty
        self.lives = 8
        self.word = self.get_word().lower()  # Get a random word based on the difficulty
        self.dashes = list('_' * len(self.word))  # Initialize dashes to represent hidden letters
        self.guesses = set()  # Set to store user's guesses
        self.definition = dictionary(self.word)[0]
        self.synonyms = dictionary(self.word)[1]

    def get_word(self):
        """
        Get a random word from the appropriate difficulty level.
        """
        random_word = {key: choice(value) for (key, value) in
                        zip(['easy', 'medium', 'hard', 'expert'],
                            [easy, medium, hard, expert])}
        
        return random_word[self.get_difficulty()]

    def get_difficulty(self):
        """
        Get the current difficulty level.
        """
        return self.difficulty

    def switch(self, letter: str):
        """
        Update the hidden work to reveal correctly guessed letters/word.
        """
        for idx, value in enumerate(self.word):
            if len(letter) < 2 and letter == value:  # If the letter is a single character and matches a letter in the word
                self.dashes[idx] = value  # Update the corresponding dash with the correct letter
            elif letter == self.word:  # If the entire word was guessed correctly
                self.dashes = self.word  # Reveal the entire word
        return self.dashes

    def display(self):
        """
        Display the current state of the game (stage, dashes, and guesses).
        """
        print(self.stage_levels())  # Print the hangman stage based on remaining lives
        self.hint()
        print(f'Lives Left: {self.lives}')
        print(f"{' '.join(self.dashes)}\t\tLetters Tried: {self.guesses}")  # Print the current state of hidden and revealed letters
    
    def hint(self):
        """
        Return a hint for the current word based on the number of remaining lives.
        Hint will return the word's definition and synonyms (if any)
        """
        if 3 < self.lives <= 5:
            print(f'The word starts with \'{self.word[0]}\' and ends with \'{self.word[-1]}\'')
        if self.lives <= 3:
            print(f'Definition: {None if not self.definition else self.definition}')
            print(f'Synonyms: {None if not self.synonyms else self.synonyms}')

    def reset(self):
        """
        Prompt the user to play again or quit the game.
        """
        ans = input('Play again? (y/n): ')
        return main() if ans == 'y' else quit()
    
    def stage_levels(self):
        """
        Return the hangman stage based on the remaining lives.
        """
        return stages[self.lives]  # Retrieve the appropriate stage based on remaining lives


def main():
    try:
        diff = input('Enter level of difficulty (easy/medium/hard/expert): ').lower()
        hang = Hangman(diff);
    except: print('\nDifficulty not chosen, ending program.'); raise SystemExit
    
    RUNNING = True
    try:
        while RUNNING and hang.lives >= 0:
            hang.display()  # Display the current state of the game
            user = input('Enter guessing letter: ')
            if user not in hang.guesses:  # If the letter has not been guessed before
                hang.guesses.add(user.upper())  # Add the letter to the set of guesses
            try:
                if user in hang.word:  # If the guessed letter is in the word
                    hang.switch(user)  # Update the dashes to reveal the correct letter(s)
                elif user not in hang.word:
                    hang.lives -= 1  # Decrement lives if the guess is incorrect
                    print('Try again\n')
                if ''.join(hang.dashes) == hang.word:  # If all the letters have been correctly guessed
                    print('congrats you won')
                    hang.reset()  # Prompt to play again or quit
            except KeyError:
                print('Invalid input. Try again\n')
                # hang.reset()  # Prompt to play again or quit
            if hang.lives == 0:  # If the user has run out of lives
                hang.display()
                print(f'You Lost..... The mystery word was {hang.word}')
                hang.reset()
    except KeyboardInterrupt:
        print('\n\nKeyboardInterrupt detected, ending program...')
        quit()


if __name__ == '__main__':
    main()
