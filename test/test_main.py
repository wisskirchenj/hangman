from io import StringIO
from unittest.mock import patch, MagicMock
import unittest

from hangman.main import Hangman


class HangmanTest(unittest.TestCase):

    def test_random_word(self):
        game = Hangman()
        self.assertEquals(game.random_word(1), 'java')
        self.assertEquals(game.random_word(44), 'javascript')
        self.assertEquals(game.random_word(55), 'python')
        self.assertEquals(game.random_word(333), 'swift')

    def test_get_progress(self):
        game = Hangman(1)
        game.letters_asked.add('a')
        self.assertEquals('-a-a', game.get_progress())
        game.letters_asked.add('v')
        self.assertEquals('-ava', game.get_progress())

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage5_do_guessing(self, mock_stdout: StringIO, mock_input: MagicMock):
        mock_args = ['a', 'i', 'o', 'z', 'l', 'p', 'h', 'k']
        mock_input.side_effect = mock_args
        Hangman(seed=44).do_guessing()
        self.assertTrue(mock_stdout.getvalue().count("That letter doesn't appear in the word.") == 5)
        mock_input.assert_called_with("\n-a-a---ip-\nInput a letter: ")
