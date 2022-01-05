# import colorgram
#
#
# colors = colorgram.extract('paint.jpeg', 112)
# col = []
#
# for el in colors:
#     color = el.rgb
#     red = color[0]
#     blue = color[2]
#     green = color[1]
#
#     col.append((red, green, blue))
#
# print(col)
import random
import turtle
from turtle import Turtle
from turtle import Screen

color_list = [(212, 154, 98), (242, 249, 247), (236, 241, 245), (53, 107, 131), (199, 142, 34), (178, 78, 33), (116, 156, 171), (124, 79, 98), (123, 175, 157), (226, 198, 129), (190, 88, 109), (12, 49, 64), (56, 39, 19), (40, 168, 128), (50, 126, 121), (199, 123, 143), (166, 21, 30), (225, 93, 78), (244, 163, 160), (38, 32, 34), (3, 25, 25), (79, 147, 169), (163, 26, 21), (19, 79, 91), (235, 166, 170), (171, 207, 190), (102, 127, 158), (163, 203, 211), (61, 60, 72), (79, 66, 42), (182, 189, 207), (15, 107, 103)]
t = Turtle()
turtle.colormode(255)
screen = Screen()
turtle.setworldcoordinates(-1, -1, 11, 11)


def dots():
    t.penup()
    for line in range(10):
        t.goto(0, line)
        for _ in range(10):
            t.dot(15, random.choice(color_list))
            t.forward(1)
        line += 0.5
    screen.exitonclick()



dots()


