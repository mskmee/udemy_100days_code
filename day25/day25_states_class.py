from turtle import Turtle


FONT_STATES = ("Courier", 7, "normal")
FONT_GAME = ("Courier", 17, "normal")


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state(self, cords, state):
        self.goto(cords)
        self.write(state, font=FONT_STATES)

    def game_over(self):
        self.goto(0, 0)
        self.write('Well done! The game is over', font=FONT_GAME, align='center')

    def quit_from_the_game(self, answers_count):
        self.clear()
        self.goto(0, 0)
        self.write(f'The game is over. You have guess {answers_count} state(s)', font=FONT_GAME, align='center')
