import day15_menu
import day_15_art


def coins_check():
    print('Please insert coins.')
    quarters = check_value_type_coins('quarters') * 0.25
    dimes = check_value_type_coins('dimes') * 0.1
    nickles = check_value_type_coins('nickles') * 0.05
    pennies = check_value_type_coins('pennies') * 0.01
    take_money = quarters + dimes + nickles + pennies
    return round(take_money, 2)


def check_value_type_coins(coin):
    check_coins = True
    while check_coins:
        try:
            while not isinstance(coin, int):
                coin = int(input(f'how many {coin}?: '))
            check_coins = False
        except ValueError:
            print('Please enter the number')
    return coin


def check_resources(drink_type):
    for item in drink_type:
        if drink_type[item] > leftovers[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True



leftovers = day15_menu.resources
leftovers['money'] = 0
machine_works = True

while machine_works:
    print(day_15_art.art)
    answer = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if answer == 'espresso':
        drink = day15_menu.MENU['espresso']
        menu = drink['ingredients']
        if check_resources(menu):
            print(day_15_art.espresso)
        else:
            continue
    elif answer == 'latte':
        drink = day15_menu.MENU['latte']
        menu = drink['ingredients']
        if check_resources(menu):
            print(day_15_art.latte)
        else:
            continue
    elif answer == 'cappuccino':
        drink = day15_menu.MENU['cappuccino']
        menu = drink['ingredients']
        if check_resources(menu):
            print(day_15_art.espresso)
        else:
            continue
    elif answer == 'report':
        print(leftovers)
        continue
    elif answer == 'off':
        print('Machine was turned off')
        machine_works = False
        break
    else:
        print('Wrong command')
        continue

    money_got = coins_check()
    if money_got >= drink['cost']:
        leftovers['money'] += drink['cost']
        change = money_got - drink['cost']
        leftovers['water'] -= drink['ingredients']['water']
        leftovers['coffee'] -= drink['ingredients']['coffee']
        if answer != 'espresso':
            leftovers['milk'] -= drink['ingredients']['milk']

        if change >= 0:
            print(f'Here is you ${round(change, 2)} in change')
            print(f'Enjoy you {answer}')
    else:
        print("Sorry that's not enough money. Money refunded.")
    machine_works = True





