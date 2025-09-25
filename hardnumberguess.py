import random
def number_guessing_game():
    print("Welcome to the Number Guessing Game! hope you like it ")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")

    secret_number = random.randint(1,100)
    attempts = 0
    max_attempts = 7

    while attempts<max_attempts:
        try:#i have use the try block so that it can handle the invalid character
            #get user input
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess:"))
            attempts+= 1

            #then after i use the flow control to match the correct or not
            if guess == secret_number:
                print(f"congratulations! You guessed it right!")
                print(f"the number was {secret_number}")
                print(f"it took you {attempts} attempt(s) to win!")
                break
            elif guess<secret_number:
                print("too low , try again")
            else:
                print("too high, try again")
            
            #then after i use the difference between the guess and secret number to find out 
            #more easily

            difference = abs(guess - secret_number)
            if difference <= 5:
                print("you are very close")
            elif difference <= 15:
                print("you are getting close")
            else:
                print("you are cold")
            
        except ValueError:
            print("please enter a valid number")
            continue
    
    #game over scenario
    if attempts >= max_attempts and guess != secret_number:
        print(f"game over! you've used all {max_attempts} attempts.")
        print(f"the number i was thinking of was {secret_number}")
    
    #playagain scenario
    play_again = input("\nwould you like to play again (y/n): ").lower()
    # lower converts whatever the player types into lowercase.
    if play_again in ['y','yes']:
        number_guessing_game()
    else:
        print("thanks for playing game")

#enhancng version with difficulty in this mode
def advanced_guessing_game():
    print("advanced number guessing game!")
    print("choose your difficulty level:")
    print("1. easy (1-50, 10 attempts)")
    print("2. medium (1-100, 7 attempts)")
    print("3. hard (1-200, 6 attempts)")
 
    while True:
        try:
            difficulty = int(input("\nselect difficulty (1-3): "))
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
                print("please choose 1, 2, or 3!")
        except ValueError:
            print("please enter a valid number!")
    
    print(f"\nI am thinking of a number between 1 and {max_num}")
    print(f"you have {max_attempts} attempts to guess it!\n")

    secret_number= random.randint(1, max_num)
    attempts = 0

    while attempts<max_attempts:
        try:
            guess = int(input(f"Attempts {attempt+1}/{max_attempts} - Enter your guess(1- {max_num}):"))

            if guess<1 or guess>max_num:
                print(f"please guess a number between 1 and {max_num}")
                continue
            attempts+=1

            if guess == secret_number:
                print(f"excellent! you got it!")
                print(f"the number was {secret_number}")
                print(f"score: {max_attempts - attempts + 1}/{max_attempts}")
                break
            elif guess < secret_number:
                print("higher!")
            else:
                print("lower!")
            
            #for more hints
            difference = abs(guess - secret_number)
            percentage = (difference / max_num) * 100

            if percentage < 5:
                print("very close 5 !")
            elif percentage < 10:
                print("little close 10!")
            elif percentage < 20:
                print("little little close 20!")
            elif percentage < 40:
                print("not close 40!")
            else:
                print("ice cold!")
        
        except ValueError:
            print("Please enter a valid number!")
            continue

        if attempts >= max_attempts and guess!= secret_number:
            print(f"out of attempts , the number was {secret_number}")
        
        play_again = input("\n playagain? (y/n):").lower()
        if play_again in ['y', 'yes']:
            advanced_guessing_game()
        else:
            print("thanks for playing game")

def main():
    print("Choose your game version:")
    print("1. Classic Game (1-100, 7 attempts)")
    print("2. Advanced Game (Multiple difficulty levels)")

    while True:
        try:
            choice = int(input("\n select option( 1 or 2):"))
            if choice == 1:
                number_guessing_game()
                break
            elif choice == 2:
                advanced_guessing_game()
                break
            else:
                print("enter 1 or 2")
        except ValueError:
            print("please enter a validnumber")

if __name__ == "__main__":
    main()

