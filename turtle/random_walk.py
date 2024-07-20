import turtle as t
from random import choice, randint

colors = ["green", "dark red", "olive drab", "teal", "steel blue", "medium blue", "medium violet red",
          "pale violet red", "crimson", "rosy brown"]
angles = [90, 180, 270, 360]
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


tim.pensize(10)
for i in range(100):
    tim.forward(30)
    tim.color(choice(colors))
    tim.color(random_color())
    tim.right(choice(angles))
    tim.speed(100)
    # if i % (choice(range(1,4))) == 0:
    #     tim.right(90)
    # else:
    #     tim.left(90)

screen = t.Screen()
screen.exitonclick()
