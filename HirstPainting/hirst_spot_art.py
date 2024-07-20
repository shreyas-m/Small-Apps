import turtle as t
from main import color_list
import random

t.colormode(255)

t.penup()
t.speed("fastest")
t.setheading(225)
t.forward(300)
t.setheading(0)
for _ in range(10):
    for _ in range(10):
        t.dot(20, random.choice(color_list))
        t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.left(180)

screen = t.Screen()
screen.exitonclick()