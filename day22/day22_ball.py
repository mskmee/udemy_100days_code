from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.resizemode('user')
        self.shapesize(0.6, 0.6, 0.6)
        self.x_move = 10
        self.y_move = 10

    def start_ball(self):
        self.speed(1)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce(self):
        self.y_move *= -1

    def ball_bounce_paddle(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.ball_bounce_paddle()
