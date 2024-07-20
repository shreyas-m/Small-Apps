from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_left():
    tim.left(10)


def move_right():
    tim.right(10)

def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d") 
screen.onkey(clear, "x")

screen.exitonclick()
