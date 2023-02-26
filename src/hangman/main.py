import random


class Hangman:

    WORDS = ['python', 'java', 'swift', 'javascript']
    
    def __init__(self, seed: int | None = None):
        self.word_to_guess: str = self.random_word(seed=seed)
        self.letters_asked: set[str] = set()
        
    @staticmethod
    def print_title():
        print('H A N G M A N')
    
    @staticmethod
    def print_bye():
        print("\nThanks for playing!")

    def random_word(self, seed: int | None) -> str:
        if seed:
            random.seed(seed)
        return random.choice(self.WORDS)

    def do_guessing(self):
        for _ in range(8):
            guess = input(f'\n{self.get_progress()}\nInput a letter: ')
            self.letters_asked.add(guess)
            if guess not in self.word_to_guess:
                print("That letter doesn't appear in the word.")

    def get_progress(self):
        return ''.join(map(lambda c: c if c in self.letters_asked else '-', self.word_to_guess))

    def main(self):
        self.print_title()
        self.do_guessing()
        self.print_bye()


if __name__ == '__main__':
    Hangman().main()
