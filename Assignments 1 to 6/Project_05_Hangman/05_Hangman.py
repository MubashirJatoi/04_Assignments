import random
from words import words as words_lists
def hangman():
    secret_word = random.choice(words_lists)
    guessed_letters = []
    lives = 6
    
    print("Welcome to Hangman!")
    print(f"You have {lives} lives to guess the word.")
    
    while lives > 0:
        # Display current progress
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)
        
        # Check if player won
        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: {secret_word}")
            return
        
        # Get player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess not in secret_word:
            lives -= 1
            print(f"Wrong! You have {lives} lives left.")
            if lives == 0:
                print(f"Game over! The word was: {secret_word}")
                return
    
hangman()