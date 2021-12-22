import os


def main():
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    users_and_bids = {}
    enter_new_users = True
    all_bids = []
    print('This is silent auction mod.')
    while enter_new_users:
        user_name = input('Enter you name: \n')
        user_bid = ''
        while not isinstance(user_bid, int):
            try:
                user_bid = int(input('Enter your bid: \n'))
            except ValueError:
                print('You suposte to enter the number')
        users_and_bids[user_name] = user_bid
        while enter_new_users:
            new_user = input('Did you have any other user? Type: yes or no ')
            if new_user == 'yes':
                clearConsole()
                break
            elif new_user == 'no':
                clearConsole()
                for key, value in users_and_bids.items():
                    all_bids.append(value)
                max_bid = max(all_bids)
                for key, value in users_and_bids.items():
                    if value == max_bid:
                        winner = key
                print(f'The winner is {winner}, his bid {max_bid}')
                enter_new_users = False


if __name__ == '__main__':
    main()

