import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Catch Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the target
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.goto(random.randint(-250, 250), random.randint(-250, 250))

# Score tracking
score = 0

# Display Score
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

# Player movement functions
def move_up():
    y = player.ycor()
    if y < 290:  # Prevent moving out of bounds
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -290:
        player.sety(y - 20)

def move_left():
    x = player.xcor()
    if x > -290:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 290:
        player.setx(x + 20)

# Keyboard controls
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Game loop
def game_loop():
    global score
    # Check if player catches the target
    if player.distance(target) < 20:
        score += 1
        target.goto(random.randint(-250, 250), random.randint(-250, 250))  # Move target
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 20, "bold"))

    screen.ontimer(game_loop, 100)  # Repeat every 100ms

# Start the game loop
game_loop()

# Keep the window open
screen.mainloop()
