import random
import os


def bank_generate():
    player_bank = ''
    while not isinstance(player_bank, int):
        try:
            player_bank = int(input('What is the bank? \n'))
        except ValueError:
            print('Wrong type of data. Please enter the number.')
    return player_bank


def bid(player, dealer):
    round_bid = int
    while not isinstance(round_bid, int):
            try:
                round_bid = int(input('Place a bid: '))
            except ValueError:
                print('Please enter the number')

    return round_bid


def main():
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    player_bank = bank_generate()
    dealer_bank = player_bank
    game = True
    while game:
        take_more_cards = True
        bid_check = True
        clearConsole()
        bid_value = bid(player_bank, dealer_bank)
        while bid_check:
            if bid_value > player_bank:
                print(f'Player got not enought money. Bid was correct to {player_bank}')
                bid_value = player_bank
                bid_check = False
            elif bid_value > dealer_bank:
                print(f'Dealer got not enought money. Bid was correct to {dealer_bank}')
                bid_value = dealer_bank
                bid_check = False
            else:
                bid_check = False
        ask = ''
        player_cards = []
        dealer_cards = []
        check_continue = True
        player_score = ''
        dealer_score = ''
        player_cards.append(taking_card())
        player_cards.append(taking_card())
        print(f'You cards: {player_cards}')
        print(f'You bank is {player_bank}$')
        dealer_cards.append(taking_card())
        dealer_score = sum_count(dealer_cards)
        print(f'Dealer first card is {dealer_cards}')
        print(f'Dealer bank is {dealer_bank}$')
        player_score = sum_count(player_cards)
        while take_more_cards:
            ask = ''
            while ask != 'y' and ask != 'n':
                ask = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if ask == 'y':
                player_cards.append(taking_card())
                print(f'Player hand is {player_cards}')
                player_score = sum_count(player_cards)
                if player_score > 21:
                    print('You got too much points')
                    take_more_cards = False
            if ask == 'n':
                take_more_cards = False
        final_player_sum = sum_count(player_cards)
        print(f'Player hand is {player_cards}')
        if final_player_sum < 22:
            while dealer_score < 19 and dealer_score < final_player_sum:
                dealer_cards.append(taking_card())
                dealer_score = sum_count(dealer_cards)
            if final_player_sum < dealer_score <= 21:
                print(f"Dealer final hand: {dealer_cards} ")
                dealer_bank = dealer_bank + bid_value
                player_bank = player_bank - bid_value
                print('Dealer wins the round.')
            elif final_player_sum > dealer_score:
                print(f"Dealer final hand: {dealer_cards} ")
                dealer_bank = dealer_bank - bid_value
                player_bank = player_bank + bid_value
                print('Player Wins the round')
            elif final_player_sum == dealer_score:
                print(f'Dealer final hand: {dealer_cards}')
                print("Draw")
            elif dealer_score < player_score < 22:
                print(f"Dealer final hand: {dealer_cards} ")
                dealer_bank = dealer_bank - bid_value
                player_bank = player_bank + bid_value
                print('Player wins the round')
            elif dealer_score > 21:
                print(f"Dealer final hand: {dealer_cards} ")
                dealer_bank = dealer_bank - bid_value
                player_bank = player_bank + bid_value
                print('Player wins the round')
            else:
                print(f'test variable play {player_cards}, deal {dealer_cards}')
        else:
            print(f'Dealer final hand is {dealer_cards}\nPlayer lose the round.\n')
            player_bank = player_bank - bid_value
            dealer_bank = dealer_bank + bid_value
        print(f'Bank values:\n'
              f'Player bank is {player_bank}$\n'
              f'Dealer bank is {dealer_bank}$')
        continue_game = ''
        if dealer_bank <= 0:
            print(f'Player has won the game.')
            check_continue = False
            game = False

        elif player_bank <= 0:
            print(f'Dealer has won!')
            check_continue = False
            game = False

        while check_continue:
            while continue_game != 'y' and continue_game != 'n':
                continue_game = input('Next round? Type y or n: ')
                if continue_game == 'y':
                    break
                elif continue_game == 'n':
                    print(f'See you soon')
                    game = False
            check_continue = False


def sum_count(cards):
    cards_values = []
    for el in cards:
        if not isinstance(el, int):
            if el == 'A':
                el = 11
            else:
                el = 10
        cards_values.append(el)
    return sum(cards_values)


def taking_card():
    cards_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    giving_card = random.choice(cards_values)
    return giving_card


if __name__ == '__main__':
    main()
