import turtle
from turtle import Turtle
from turtle import Screen


timmy = Turtle()
screen = Screen()
timmy.shape('turtle')
timmy.color('green')
forvard = 0


def triangle():
    timmy.pencolor('aqua')
    for _ in range(3):
        timmy.left(120)
        timmy.forward(100)


def square():
    timmy.pencolor('black')
    for _ in range(4):
        timmy.left(90)
        timmy.forward(100)


def pentagon():
    timmy.pencolor('red')
    for _ in range(5):
        timmy.left(72)
        timmy.forward(100)


def hexagon():
    timmy.pencolor('green')
    for _ in range(6):
        timmy.left(60)
        timmy.forward(100)


def octagon():
    timmy.pencolor('blue')
    for _ in range(7):
        timmy.left()
        timmy.forward(100)


def nonagon():
    timmy.pencolor('green')
    for _ in range(8):
        timmy.left(45)
        timmy.forward(100)


triangle()
square()
pentagon()
hexagon()
octagon()
nonagon()

screen.exitonclick()

