def begin():
        way_pass = input("You're are a cross road. Where do you want to go?"
                         'Type "left" or "right" \n')
        if way_pass == 'left':
            left_way()
        elif way_pass == 'right':
            right_way()
        else:
            print('You supposte to choose one of 2 values')
            begin()


def left_way():
    pass

def right_way():
    pass

def main(): #the game begins here
    print('Welcome to Tresure Island \n'
          'Your misson is to find the treasure. \n')
    begin()


if __name__ == '__main__':
    main()