import random 

def diceroller():
    printf("welcome to the dice rolling game")
    while True:
        roll = input("type (y/n): ").lower()

        if roll == "y":
            print("you rolled: ",random.randint(1,6))
        elif roll == "n":
            print("Goodbye")
            break
        else:
            print("invalid choice")
    