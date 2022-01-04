from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-220, 250)
        self.hideturtle()
        self.score = 0
        self.write(f'Score: {self.score}', font=FONT, align='center')

    def appended_score(self):
        self.clear()
        self.goto(-220, 250)
        self.score += 1
        self.write(f'Score: {self.score}', font=FONT, align='center')

    def lose_board(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over. You score is {self.score}', align='center', font=FONT)

    def new_round(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'New round. You score is {self.score + 1}', align='center', font=FONT)