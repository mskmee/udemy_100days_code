import random


def main():
    using_numbs = []
    game = True
    answer = True
    number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking about number between 1 and 100.\n")
    difficulty = ''
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input('Choose a difficulty. Type easy or hard: ')
        print('Please choose one of game mods')
    if difficulty == 'easy':
        difficulty = 10
    else:
        difficulty = 5
    while game:
        while answer:
            guess = ''
            try:
                guess = int(input("Make a guess: "))
                if guess in using_numbs:
                    print('You have tried this number')
                else:
                    using_numbs.append(guess)
                    answer = False
            except ValueError:
                print('Wrong data type. Please enter the number')
        if difficulty > 1:
            range_to_num = guess - number
            if 10 > range_to_num > 0:
                difficulty -= 1
                print('Still high, but you are close\n'
                        f'You have {difficulty} attempts remaining to guess the number.')
                answer = True
            elif -10 < range_to_num < 0:
                difficulty -= 1
                print('Still low, but you are close\n'
                      f'You have {difficulty} attempts remaining to guess the number')
                answer = True

            elif guess > number:
                difficulty -= 1
                print(f'Too high.\nTry again\n'
                      f'You have {difficulty} attempts remaining to guess the number.')
                answer = True
            elif guess < number:
                difficulty -= 1
                print(f'Too low.\nTry again\n'
                      f'You have {difficulty} attempts remaining to guess the number.')
                answer = True
            else:
                print(f'Got it. The answer is {number}')
                game = False
        else:
            print("You've run out of guesses, you lose.\n"
                  f"The answer was {number}")
            game = False


if __name__ == '__main__':
    main()
