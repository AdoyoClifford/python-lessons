import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

player = input("Enter your choice(rock, paper, scissors):").lower()

print(f"computer chose: {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif player == "paper":
    if computer == "rock":
        print("You win!")
    else:
        print("You lose!")
elif player == "scissors":
    if computer == "paper":
        print("You win!")
    else:
        print("You lose!")
else:
    print("Invalid choice!")