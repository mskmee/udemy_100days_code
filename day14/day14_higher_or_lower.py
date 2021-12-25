import day_14_art
from day14_data import data
import random


def versus():
    '''versus pare and return winner'''
    compare1 = picked()
    compare2 = picked()
    if compare1['name'] == compare2['name']:
        compare2 = picked()
    print('Compare A: ' + compare1['name'] + ', a ' + compare1['description'] + ', from ' + compare1['country'])
    print(day_14_art.vs)
    print('Compare B: ' + compare2['name'] + ', a ' + compare2['description'] + ', from ' + compare2['country'])
    return [compare1, compare2]


def picked():
    return random.choice(data)


def game():
    game = True
    score = 0
    while game:
        answer = ''
        print(day_14_art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        check = versus()
        while answer != 'a' and answer != 'b':
            answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        if answer == 'a':
            if check[0]['follower_count'] > check[1]['follower_count']:
                score += 1
            else:
                if score == 0:
                    print("Sorry, that's wrong.")
                    return 0
                else:
                    print(f"Sorry, that's wrong. Final score: {score}")
                    return 0

        elif answer == 'b':
            if check[1]['follower_count'] > check[0]['follower_count']:
                score += 1
            else:
                if score == 0:
                    print("Sorry, that's wrong.")
                    return 0
                else:
                    print(f"Sorry, that's wrong. Final score: {score}")
                    return 0


if __name__ == '__main__':
    game()

