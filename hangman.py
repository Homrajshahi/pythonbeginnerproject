import random

# Some words to play with
WORDS = ["python", "computer", "hangman", "keyboard", "programming", "openai"]

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def hangman():  
    print("Welcome to Hangman!")
    word = random.choice(WORDS)  # Pick a random word
    guessed = set()
    lives = len(HANGMAN_PICS) - 1
    game_over = False

    while not game_over:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - lives])
        
        # Display word with guessed letters
        display_word = [letter if letter in guessed else "_" for letter in word]
        print("Word:", " ".join(display_word))
        print(f"Lives left: {lives}")
        print("Guessed letters:", " ".join(sorted(guessed)) if guessed else "None")

        # Check win
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", word)
            break

        # Ask player for a guess
        guess = input("\nEnter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.add(guess)

        if guess not in word:
            lives -= 1
            print(f"❌ '{guess}' is not in the word.")
            if lives == 0:
                print(HANGMAN_PICS[-1])
                print("\nGame Over! The word was:", word)
                game_over = True

if __name__ == "__main__":
    hangman()
