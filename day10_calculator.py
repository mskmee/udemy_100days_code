def number():
    number = ''
    while not isinstance(number, float):
        try:
            number = float(input("What's the number?: "))
        except ValueError:
            print('You suppose to enter the number')
    return number


def choose_mod():
    mod = ''
    while mod != '+' and mod != '-' and mod != '*' and mod != '/':
        mod = input('+\n'
                    '-\n'
                    '*\n'
                    '/\n'
                    'pick an operation: ')
    return mod


def main():
    first_number = ''
    print('It is calculator (logo...)')
    calculator_stop = False
    while not calculator_stop:
        next_operation = ''
        if first_number == '':
            first_number = number()
        mod = choose_mod()
        next_number = number()
        result = calculated(first_number, mod, next_number)
        print(f'{first_number} {mod} {next_number} = {result}')
        while next_operation != 'y' and next_operation != 'n' and next_operation != 'q':
            next_operation = input(f"Type 'y' to continue with {next_number},"
                                   f" or type 'n' to start a new calculate. Type 'q' to quit ")
            if next_operation == 'y':
                first_number = next_number
            elif next_operation == 'n':
                first_number = ''
                break
            elif next_operation == 'q':
                print('Good Bye!')
                calculator_stop = True
            else:
                print('Choose one of options')


def calculated(f_num, mod, next_num):
    """Checking mod and use it to variables"""
    if mod == '+':
        return f_num + next_num
    elif mod == '-':
        return f_num - next_num
    elif mod == '*':
        return f_num * next_num
    else:
        return f_num / next_num


if __name__ == '__main__':
    main()
    