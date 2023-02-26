import random


class Hangman:

    WORDS = ['python', 'java', 'swift', 'javascript']
    
    def __init__(self, seed: int | None = None):
        self.word_to_guess: str = self.random_word(seed=seed)
        self.letters_asked: set[str] = set()
        self.attempts_left = 8
        self.wins = 0
        self.losses = 0
        
    @staticmethod
    def print_title():
        print('H A N G M A N')

    def random_word(self, seed: int | None) -> str:
        if seed:
            random.seed(seed)
        return random.choice(self.WORDS)

    def do_guessing(self) -> bool:
        while self.attempts_left:
            self.handle_guess()
            if self.get_progress() == self.word_to_guess:
                print(f'You guessed the word {self.word_to_guess}!')
                self.wins += 1
                return True
        self.losses += 1
        return False

    def handle_guess(self):
        guess = self.get_valid_guess()
        if guess in self.letters_asked:
            print("You've already guessed this letter.")
        elif guess not in self.word_to_guess:
            self.handle_failed_attempt("That letter doesn't appear in the word.")
        self.letters_asked.add(guess)

    def get_valid_guess(self) -> str:
        valid_input = False
        while not valid_input:
            guess = input(f'\n{self.get_progress()}\nInput a letter: ')
            if len(guess) != 1:
                print('Please, input a single letter.')
            elif not guess.islower():
                print('Please, enter a lowercase letter from the English alphabet.')
            else:
                return guess

    def handle_failed_attempt(self, message: str):
        self.attempts_left -= 1
        print(message)

    def get_progress(self):
        return ''.join(map(lambda c: c if c in self.letters_asked else '-', self.word_to_guess))

    def play(self):
        guessed = self.do_guessing()
        print('You survived!' if guessed else '\nYou lost!')
        self.reset_game()

    def results(self):
        print(f'You won: {self.wins} times.')
        print(f'You lost: {self.losses} times.')

    def reset_game(self):
        self.word_to_guess = self.random_word(None)
        self.attempts_left = 8
        self.letters_asked = set()

    def main(self):
        self.print_title()
        choice = ''
        while choice != 'exit':
            choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
            match choice:
                case 'play':
                    self.play()
                case 'results':
                    self.results()


if __name__ == '__main__':
    Hangman().main()
