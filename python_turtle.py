import random
import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape("turtle")
t2.shape("turtle")
t1.color("red")
t2.color("blue")

t1.penup()
t1.goto(-200,50)
t1.pendown()

t2.penup()
t2.goto(-200,50)
t2.pendown()

for i in range(50):
    t1.forward(random.randint(1,10))
    t2.forward(random.randint(1,10))

screen.mainloop() 

