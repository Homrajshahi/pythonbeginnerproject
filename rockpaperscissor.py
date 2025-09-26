import random

def rock_paper_scissor():
    print("Welcome to the this classic game: Rock,Paper & Scissor")
    print("Type 'rock','paper' or 'scissor' to play")
    print("Type 'quit' to stop\n")

    choices=["rock","scissor","paper"]

    while True:
        #it is the player choice
        player = input("Your choice (rock/paper/scissor): ").lower()

        if player == "quit":
            print(" Thanks for playing game")
            break

        if player not in choices:
            print("Invalid choice,Please try again")
            continue

        computer = random.choice(choices)
        print(f"Computer choice : {computer}")

        if player == computer:
            print("it is a tie")
        
        elif(player == "rock" and computer == "scissor") or \
            (player == "scissor" and computer == "paper") or \
            (player == "paper" and computer == "rock"):
                print("you win!\n")
        else:
            print("you lose!\n")

if __name__ == "__main__":
    rock_paper_scissor()

