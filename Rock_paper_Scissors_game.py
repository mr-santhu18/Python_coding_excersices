# first mini project
print("program for Rock, Paper, Scissors game")
import random

choices = ["rock","paper","scissors"]

computer = random.choice(choices)

user = input("Enter rock, paper, scissors :").lower()

if user not in choices:
    print("Invalid Input..! please enter rock,paper,scissors")
else:
    print(f"computer choice :{computer}")

    if user == computer:
        print("It's a Tie...!")
    elif(user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        print("You win...!")
    else:
        print("You lose...!")