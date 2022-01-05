import turtle
import pandas
from day25_states_class import State

answers_count = 0
screen = turtle.Screen()
screen.title('U.S. States Game (for quit type "quit")')
image = 'blank_states_img.gif'
screen.addshape(image)

state = State()
turtle.shape(image)

df = pandas.read_csv('50_states.csv')
states_list = df.state.to_list()


def check_state(name):
    """Check the user enter with state list"""
    for el in states_list:
        if el == name:
            return el
        else:
            pass


def unnamed_states(state_list):
    df = pandas.DataFrame(state_list)
    df.to_csv('to_learn.csv')


while answers_count != 50:
    if answers_count == 0:
        answer = screen.textinput(title='Guess the state', prompt='Whats another name?').title()
    else:
        answer = screen.textinput(title=f'{answers_count}/50 States Correct', prompt='Whats another name?').title()
    if check_state(answer):
        state_name = check_state(answer)
        states_list.remove(state_name)  # Delete user enter from states list
        x_y_cor = df[df['state'] == state_name].to_dict()
        x_cor = tuple(x_y_cor['x'].values())
        y_cor = tuple(x_y_cor['y'].values())
        final_cor = x_cor + y_cor
        answers_count += 1
        state.write_state(final_cor, state_name)

    if answer == 'Quit':
        state.quit_from_the_game(answers_count)
        unnamed_states(states_list)
        screen.exitonclick()
        break

state.game_over()
screen.exitonclick()
