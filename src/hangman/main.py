def print_title():
    print('H A N G M A N')


def main():
    print_title()
    guess = input('Guess the word: ')
    print('You survived!' if guess == 'python' else 'You lost!')


if __name__ == '__main__':
    main()
