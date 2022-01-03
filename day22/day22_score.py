from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor('white')
        self.left_player_score = 0
        self.right_player_score = 0

    def left_player(self):
        self.goto(-80, 260)
        self.write(f'{self.left_player_score}', font=('Verdana', 25, 'bold'))

    def right_player(self):
        self.goto(80, 260)
        self.write(f'{self.right_player_score}', font=('Verdana', 25, 'bold'))

    def end_game(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write(f'{winner} has won the game', font=('Verdana', 15, 'bold'), align='center')

    def update_score(self, winner):
        self.clear()
        if winner == 'right_player':
            self.right_player_score += 1
        else:
            self.left_player_score += 1
        self.goto(-80, 260)
        self.write(f'{self.left_player_score}', font=('Verdana', 25, 'bold'), align='center')
        self.goto(80, 260)
        self.write(f'{self.right_player_score}', font=('Verdana', 25, 'bold'), align='center')
