import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game! hope you like it ")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check if guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed it right!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempt(s) to win!")
                break
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
                
            # Give hints based on how close they are
            difference = abs(guess - secret_number)
            if difference <= 5:
                print("You're very close!")
            elif difference <= 15:
                print("You're getting warm!")
            else:
                print("You're cold!")
                
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    # If they run out of attempts
    if attempts >= max_attempts and guess != secret_number:
        print(f"Game Over! You've used all {max_attempts} attempts.")
        print(f"The number I was thinking of was {secret_number}")
    
    # Ask if they want to play again
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again in ['y', 'yes']:
        print("\n" + "="*50 + "\n")
        number_guessing_game()  # Recursive call to start new game
    else:
        print("Thanks for playing! Goodbye!")

# Enhanced version with difficulty levels
def advanced_guessing_game():
    print("Advanced Number Guessing Game!")
    print("Choose your difficulty level:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 6 attempts)")
    
    while True:
        try:
            difficulty = int(input("\nSelect difficulty (1-3): "))
            if difficulty == 1:
                max_num, max_attempts = 50, 10
                break
            elif difficulty == 2:
                max_num, max_attempts = 100, 7
                break
            elif difficulty == 3:
                max_num, max_attempts = 200, 6
                break
            else:
                print("Please choose 1, 2, or 3!")
        except ValueError:
            print("Please enter a valid number!")
    
    print(f"\nI'm thinking of a number between 1 and {max_num}")
    print(f"You have {max_attempts} attempts to guess it!\n")
    
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess (1-{max_num}): "))
            
            if guess < 1 or guess > max_num:
                print(f"Please guess a number between 1 and {max_num}!")
                continue
                
            attempts += 1
            
            if guess == secret_number:
                print(f"Excellent! You got it!")
                print(f"The number was {secret_number}")
                print(f"Score: {max_attempts - attempts + 1}/{max_attempts}")
                break
            elif guess < secret_number:
                print("Higher!")
            else:
                print("Lower!")
                
            # Proximity hints
            difference = abs(guess - secret_number)
            percentage = (difference / max_num) * 100
            
            if percentage < 5:
                print("Burning hot!")
            elif percentage < 10:
                print("Very warm!")
            elif percentage < 20:
                print("Warm!")
            elif percentage < 40:
                print("Cool!")
            else:
                print("Ice cold!")
                
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    if attempts >= max_attempts and guess != secret_number:
        print(f"💔 Out of attempts! The number was {secret_number}")
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again in ['y', 'yes']:
        print("\n" + "="*50 + "\n")
        advanced_guessing_game()
    else:
        print("Thanks for playing!")

# Main menu
def main():
    print("Choose your game version:")
    print("1. Classic Game (1-100, 7 attempts)")
    print("2. Advanced Game (Multiple difficulty levels)")
    
    while True:
        try:
            choice = int(input("\nSelect version (1 or 2): "))
            if choice == 1:
                print("\n" + "="*50 + "\n")
                number_guessing_game()
                break
            elif choice == 2:
                print("\n" + "="*50 + "\n")
                advanced_guessing_game()
                break
            else:
                print("Please choose 1 or 2!")
        except ValueError:
            print("Please enter a valid number!")

# Run the game
if __name__ == "__main__":
    main()