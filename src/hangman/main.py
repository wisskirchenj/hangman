import random


class Hangman:

    WORDS = ['python', 'java', 'swift', 'javascript']
    
    def __init__(self, seed: int | None = None):
        self.word_to_guess: str = self.random_word(seed=seed)
        self.letters_asked: set[str] = set()
        self.attempts_left = 8
        
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

    def do_guessing(self) -> bool:
        while self.attempts_left:
            guess = input(f'\n{self.get_progress()}\nInput a letter: ')
            self.check_guess(guess)
            if self.get_progress() == self.word_to_guess:
                print(f'\n{self.word_to_guess}\nYou guessed the word!')
                return True
        return False

    def check_guess(self, guess: str):
        if guess not in self.word_to_guess:
            self.handle_failed_attempt("That letter doesn't appear in the word.")
        elif guess in self.letters_asked:
            self.handle_failed_attempt('No improvements.')
        self.letters_asked.add(guess)

    def handle_failed_attempt(self, message: str):
        self.attempts_left -= 1
        print(message)

    def get_progress(self):
        return ''.join(map(lambda c: c if c in self.letters_asked else '-', self.word_to_guess))

    def main(self):
        self.print_title()
        guessed = self.do_guessing()
        print('You survived!' if guessed else '\nYou lost!')


if __name__ == '__main__':
    Hangman().main()
