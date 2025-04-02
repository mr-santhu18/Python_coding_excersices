import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Turtle Race Game")

# Create the race track
track = turtle.Turtle()
track.speed(1)
track.penup()
track.goto(-200, 100)
track.pendown()

for i in range(6):  # Draw finish lines
    track.forward(400)
    track.right(90)
    track.forward(200)
    track.right(90)
    track.forward(400)
    track.right(90)
    track.forward(200)
    track.right(90)
    track.penup()
    track.goto(-200, 100 - (i + 1) * 40)
    track.pendown()
track.hideturtle()

# Create turtles (racers)
colors = ["red", "blue", "green", "yellow", "purple"]
turtles = []

for i in range(5):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(-200, 80 - (i * 40))
    turtles.append(racer)

# Start the race
winner = None
while winner is None:
    for racer in turtles:
        racer.forward(random.randint(1, 10))  # Move forward randomly
        if racer.xcor() >= 200:  # Check if any turtle has won
            winner = racer
            break

# Declare the winner
winner.color("gold")  # Change color of winner to gold
print(f"The winner is the {winner.pencolor()} turtle!")

# Keep the window open
turtle.done()
