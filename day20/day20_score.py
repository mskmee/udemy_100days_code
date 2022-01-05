from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 280)
        self.pencolor('white')
        self.penup()
        self.write(f'Score:  {self.score}', align='center', font=("Verdana", 15, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'The game is over!\n You score is {self.score}', align='center', font=('Verdana', 25, 'bold'))

    def score_change(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='center', font=("Verdana", 15, "normal"))

