import random

WORDS = ['python', 'java', 'swift', 'javascript']


def print_title():
    print('H A N G M A N')


def random_word(seed: int | None) -> str:
    if seed:
        random.seed(seed)
    return random.choice(WORDS)


def main(seed=None):
    print_title()
    to_guess = random_word(seed)
    hidden = to_guess[:3] + '-' * (len(to_guess) - 3)
    guess = input(f'Guess the word {hidden}: ')
    print('You survived!' if guess == to_guess else 'You lost!')


if __name__ == '__main__':
    main()
