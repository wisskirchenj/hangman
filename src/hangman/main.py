import random

WORDS = ['python', 'java', 'swift', 'javascript']


def print_title():
    print('H A N G M A N')


def random_word() -> str:
    return random.choice(WORDS)


def main():
    print_title()
    guess = input('Guess the word: ')
    print('You survived!' if guess == random_word() else 'You lost!')


if __name__ == '__main__':
    main()
