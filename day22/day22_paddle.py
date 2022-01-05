from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square')
        self.resizemode('user')
        self.shapesize(3, 0.5, 0.5)
        self.goto(-280, 0)

    def move_up(self):
        if self.ycor() < 260:
            new_ycor = self.ycor() + 20
            self.goto(self.xcor(), new_ycor)

    def move_down(self):
        if self.ycor() > -260:
            new_ycor = self.ycor() - 20
            self.goto(self.xcor(), new_ycor)

