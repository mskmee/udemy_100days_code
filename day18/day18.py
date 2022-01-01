import turtle
from turtle import Turtle
from turtle import Screen
import random


timmy = Turtle()
screen = Screen()
timmy.shape('turtle')
timmy.color('green')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def cirles_around(size_of_gap):
    turtle.colormode(255)
    for i in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

cirles_around(5)    
# def random_walk():
#     directions = [90, 180, 270, 0]
#     turtle.colormode(255)
#
#     while True:
#         timmy.pensize(10)
#         timmy.pencolor(random_color())
#         timmy.left(random.choice(directions))
#         timmy.forward(15)
#
#
# random_walk()
# def figures():
#     colors = ['aqua', 'black', 'green', 'blue', 'red']
#     i = 2
#     while i in range(10):
#         timmy.pencolor(choice(colors))
#         i += 1
#         for _ in range(i):
#             timmy.left(360 / i)
#             timmy.forward(100)
#
#
#
# figures()
#
#
# def triangle():
#     timmy.pencolor('aqua')
#     for _ in range(3):
#         timmy.left(120)
#         timmy.forward(100)
#
#
# def square():
#     timmy.pencolor('black')
#     for _ in range(4):
#         timmy.left(90)
#         timmy.forward(100)
#
#
# def pentagon():
#     timmy.pencolor('red')
#     for _ in range(5):
#         timmy.left(72)
#         timmy.forward(100)
#
#
# def hexagon():
#     timmy.pencolor('green')
#     for _ in range(6):
#         timmy.left(60)
#         timmy.forward(100)
#
#
# def octagon():
#     timmy.pencolor('blue')
#     for _ in range(7):
#         timmy.left(51.43)
#         timmy.forward(100)
#
#
# def nonagon():
#     timmy.pencolor('green')
#     for _ in range(8):
#         timmy.left(45)
#         timmy.forward(100)
#
#
# def decagon():
#     timmy.pencolor('black')
#     for _ in range(9):
#         timmy.left(40)
#         timmy.forward(100)
#
#
# triangle()
# square()
# pentagon()
# hexagon()
# octagon()
# nonagon()
# decagon()

screen.exitonclick()
