def main():
    print('Welcome to the tip calculator.\n')
    try:
        bill = float(input('What was the total bill? '))
        people = float(input('How many people to split the bill? '))
        tips = float(input('What percentage tip you like to give? '))
    except ValueError:
        print('You supposte to enter the number')
        main()

    t_bill = bill + ((bill / 100) * tips)
    answer = t_bill / people
    print(f'Each person should pay: {answer}')


if __name__ == '__main__':
    main()