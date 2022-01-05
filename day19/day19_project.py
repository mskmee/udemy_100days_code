import random
import turtle
from turtle import Turtle
from turtle import Screen


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='make you bet', prompt='Which turtle will win the race? ').lower()
colors = ['red', 'orange', 'yellow', 'green', 'purple', 'blue']
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f'You are win! The winner is {wining_color}')
            else:
                print(f'You have lost. The winner is {wining_color}')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
