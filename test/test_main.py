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
    def test_stage6_do_guessing_win(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_args = ['j', 'i', 'g', 'g', 'g', 'g', 'a', 'v']
        mock_input.side_effect = mock_args
        self.assertTrue(Hangman(seed=1).do_guessing())
        self.assertEqual(5, mock_stdout.getvalue().count("That letter doesn't appear in the word."))
        self.assertEqual(0, mock_stdout.getvalue().count("No improvements."))
        self.assertEqual(1, mock_stdout.getvalue().count("\njava\nYou guessed the word!"))
        mock_input.assert_any_call("\nj---\nInput a letter: ")
        mock_input.assert_called_with("\nja-a\nInput a letter: ")

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage6_do_guessing_loose(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_args = ['a', 'i', 'o', 'z', 'l', 'p', 'h', 'k', 'j', 'j', 'a', 'i']
        mock_input.side_effect = mock_args
        self.assertFalse(Hangman(seed=44).do_guessing())
        self.assertEqual(5, mock_stdout.getvalue().count("That letter doesn't appear in the word."))
        self.assertEqual(3, mock_stdout.getvalue().count("No improvements."))
        mock_input.assert_any_call("\n-a-a------\nInput a letter: ")
        mock_input.assert_any_call("\n-a-a---i--\nInput a letter: ")
        mock_input.assert_any_call("\n-a-a---ip-\nInput a letter: ")
        mock_input.assert_called_with("\nja-a---ip-\nInput a letter: ")
