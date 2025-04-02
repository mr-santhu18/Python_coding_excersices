import cv2
import numpy as np
import turtle

# Load the image
image_path = "1693558225781.jpg"  # Ensure the correct path
img = cv2.imread(image_path)

# Check if image is loaded properly
if img is None:
    print("Error: Could not load image. Check the file path.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny edge detection
edges = cv2.Canny(blurred, 50, 150)

# Get image dimensions
height, width = edges.shape

# Set up Turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)  # Turn off automatic updates to speed up drawing

# Initialize the turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(1)
t.color("black")
t.penup()

# Scale factors for fitting the image in the turtle screen
scale_x = 500 / width
scale_y = 500 / height
scale = min(scale_x, scale_y)

# Move to starting position
start_x = -width * scale / 2
start_y = height * scale / 2
t.goto(start_x, start_y)

# Draw the edges using Turtle
for y in range(height):
    for x in range(width):
        if edges[y, x] == 255:  # If it's an edge
            t.goto((x - width / 2) * scale, (height / 2 - y) * scale)
            t.pendown()
        else:
            t.penup()

# Update the screen and finish
screen.update()
turtle.done()
