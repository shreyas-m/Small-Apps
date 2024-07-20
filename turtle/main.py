from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# print(timmy)
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

tim = Turtle()
tim.shape("turtle")
tim.color("black")
for i in range(100):
    if i % 8 == 0:
        tim.right(30)
    if i % 2 == 0:
        tim.pendown()
    else:
        tim.penup()
    tim.forward(10)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("name", ["Shreyas", "Mahajan"])
# table.add_column("job", ["Problem Solver", "Developer"])
#
# print(table)
