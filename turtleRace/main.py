from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen_width = 500
screen_height = 400
screen.setup(500, 400)

user_bet = screen.textinput("Make your bet", "Which turtle win the race, enter colour:")
colors = ["red", "blue", "green", "yellow", "orange", "violet"]
participants = []
for i in range(0, len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[i])
    participants.append(tim)
    tim.penup()
    tim.goto(-(screen_width / 2) + 20, -(screen_height / 2) + ((screen_height - (20 * len(colors))) / 2) + 30 * i)
winner = user_bet

while is_race_on:
    tim = participants[random.randint(0, len(participants) - 1)]
    tim.forward(random.randint(0, 10))
    print(f"{tim.pencolor()} x cor -> {tim.xcor()} -- run? {is_race_on}")
    if tim.xcor() > 230:
        is_race_on = False
        winner = tim.pencolor()

if user_bet == winner:
    print("You Win!!!")
else:
    print(f"{winner} was a winner! You lose")

print(user_bet)

screen.exitonclick()
