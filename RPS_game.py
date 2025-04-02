import random

choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)

user = input("Enter rock, paper, or scissors: ").lower()

if user not in choices:
    print("Invalid input! Please enter rock, paper, or scissors.")
else:
    print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")









# The backslash (\) allows us to write the condition on multiple lines for better readability.