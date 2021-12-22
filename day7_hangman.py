import random


HANGMAN = (
"""
------
|    |
|
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O  |
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   |
|   |
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
--------
"""
)

world_list = ['ardvark', 'baboon', 'camel']
chosen_word = random.choice(world_list)
mask = []
len_word = len(chosen_word)
count_word = len(chosen_word)
try_count = 0
used_letters = []
for letter in chosen_word:
    mask.append('_')
print('The game begins')
while try_count != 7 and count_word != 0:
    guess = input(f'{mask} \nType guess: \n').lower()
    if guess in used_letters:
        print(f'Used letters is {used_letters}')
        print('You are already used this letter')
    elif len(guess) > 1:
        print('You must type 1 letter')
    elif guess in chosen_word:
        used_letters.append(guess)
        for i in range(len_word):
            if guess == chosen_word[i]:
                mask[i] = chosen_word[i]
                count_word -= 1

    else:
        used_letters.append(guess)
        print('Wrong letter')
        print(HANGMAN[try_count])
        try_count += 1
if try_count != 7:
    print(f'You area saved him \nThe word is {chosen_word}')
else:
    print(f'He has dead \nThe word was {chosen_word}')








