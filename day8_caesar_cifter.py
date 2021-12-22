from art import logo


def main():
    one_more = True
    check_key = True
    while one_more:
        type_cipher = ''
        while type_cipher != 'encode' and type_cipher != 'decode':
            type_cipher = input("Type 'encode' to encrypt, or 'decode' to decrypt: \n")
        words = input('Type you message: \n')
        while check_key:
            try:
                key = int(input('Enter the shift: \n'))
                check_key = False
            except ValueError:
                print('You suposte to enter number')
                
        caesar(type_cipher, words, key)
        answer = ''
        while answer != 'yes' or answer != 'no':
            answer = input("One more time? Type 'yes' or 'no' \n")
            if answer == 'yes':
                break
            else:
                print('Good Bye')
                one_more = False
                break


def caesar(mode, text, shift):
    out_word = ''
    if mode == 'decode':
        shift *= -1
    for letter in text:
        if ord(letter) in range(32, 65):
            out_word += letter
        else:
            out_word += chr(ord(letter) + shift)
    print(f'{mode}d word is {out_word}')


if __name__ == '__main__':
    print(logo)
    main()




