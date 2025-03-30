'''Etch A Sketch'''


# from turtle import Turtle, Screen
# cem = Turtle()
# screen = Screen()
#
#
# def forwards():
#     cem.fd(10)
#
#
# def backwards():
#     cem.backward(10)
#
#
# def to_right():
#     cem.right(10)
#
#
# def to_left():
#     cem.left(10)
#
#
# def clear():
#     cem.reset()
#
#
# screen.listen()
# screen.onkey(key="w", fun=forwards)
# screen.onkey(key="s", fun=backwards)
# screen.onkey(key="a", fun=to_left)
# screen.onkey(key="d", fun=to_right)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()

'''Turtle Race'''

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
race = False

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.pu()
    tim.goto(x=-230, y=positions[i])
    all_turtles.append(tim)

if user_bet:
    race = True

while race:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            race = False
            winner = turtle.pencolor()

            if user_bet == winner:
                print("You've won!")

            else:
                print("You've lost.")

        distance = random.randint(0, 10)
        turtle.fd(distance)










screen.exitonclick()
