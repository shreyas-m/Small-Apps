from turtle import Turtle, Screen
from random import choice

tim = Turtle()
tim.shape("turtle")
tim.color("green")

for i in range(3, 10):
    angle = 360/i
    tim.color(choice(["red", "green", "blue"]))
    for _ in range(i):
        tim.forward(100)
        tim.right(angle)

screen = Screen()
screen.exitonclick()