import turtle as t
from random import choice, randint

tim = t.Turtle()
tim.shape("turtle")
tim.color("green")
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_code = (r, g, b)
    return color_code


tim.speed('fastest')
for i in range(10, 360, 10):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(i)

screen = t.Screen()
screen.exitonclick()
