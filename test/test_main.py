from io import StringIO
from unittest.mock import patch, MagicMock
import unittest

from hangman.main import Hangman


class HangmanTest(unittest.TestCase):

    def test_random_word(self):
        game = Hangman()
        self.assertEqual(game.random_word(1), 'java')
        self.assertEqual(game.random_word(44), 'javascript')
        self.assertEqual(game.random_word(55), 'python')
        self.assertEqual(game.random_word(333), 'swift')

    def test_get_progress(self):
        game = Hangman(seed=1)
        game.letters_asked.add('a')
        self.assertEqual('-a-a', game.get_progress())
        game.letters_asked.add('v')
        self.assertEqual('-ava', game.get_progress())

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_valid_guess(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_args = ['j-', 'ai', '', 'G', 'g']
        mock_input.side_effect = mock_args
        self.assertEqual('g', Hangman().get_valid_guess())
        self.assertEqual(3, mock_stdout.getvalue().count('Please, input a single letter.'))
        self.assertEqual(1, mock_stdout.getvalue().count('Please, enter a lowercase letter from the English alphabet.'))

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage7_example1_loose(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_args = ['a', 'i', 'o', 'o', 'p', 'p', 'h', 'k', 'a', 'z', 't', 'x', 'b', 'd', 'w']
        mock_input.side_effect = mock_args
        self.assertFalse(Hangman(seed=44).do_guessing())
        self.assertEqual(8, mock_stdout.getvalue().count("That letter doesn't appear in the word."))
        self.assertEqual(3, mock_stdout.getvalue().count("You've already guessed this letter."))
        mock_input.assert_any_call("\n----------\nInput a letter: ")
        mock_input.assert_any_call("\n-a-a------\nInput a letter: ")
        mock_input.assert_any_call("\n-a-a---i--\nInput a letter: ")
        mock_input.assert_any_call("\n-a-a---ip-\nInput a letter: ")
        mock_input.assert_called_with("\n-a-a---ipt\nInput a letter: ")

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage7_example2_win(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_args = ['j', 'i', '+', 'A', 'ii', '++', '', 'g', 'a', 'v']
        mock_input.side_effect = mock_args
        self.assertTrue(Hangman(seed=1).do_guessing())
        self.assertEqual(2, mock_stdout.getvalue().count("That letter doesn't appear in the word."))
        self.assertEqual(3, mock_stdout.getvalue().count('Please, input a single letter.'))
        self.assertEqual(2, mock_stdout.getvalue().count('Please, enter a lowercase letter from the English alphabet.'))
        self.assertEqual(1, mock_stdout.getvalue().count("You guessed the word java!"))
        mock_input.assert_any_call("\nj---\nInput a letter: ")
        mock_input.assert_called_with("\nja-a\nInput a letter: ")

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage8(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_args = ['play', 'h', 'K', 't', 'o', '+', 'K', 'h', 'K', 'n', 'q', 'y', 'h', 'p', 'results', 'exit']
        mock_input.side_effect = mock_args
        Hangman(seed=55).main()
        self.assertEqual(1, mock_stdout.getvalue().count("That letter doesn't appear in the word."))
        self.assertEqual(4, mock_stdout.getvalue().count('Please, enter a lowercase letter from the English alphabet.'))
        self.assertEqual(2, mock_stdout.getvalue().count("You've already guessed this letter."))
        self.assertEqual(1, mock_stdout.getvalue().count("You guessed the word python!"))
        self.assertEqual(1, mock_stdout.getvalue().count("You won: 1 times.\nYou lost: 0 times."))
        mock_input.assert_any_call("\n---h--\nInput a letter: ")
        mock_input.assert_any_call("\n--tho-\nInput a letter: ")
        mock_input.assert_any_call("\n-ython\nInput a letter: ")
        mock_input\
            .assert_called_with('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
