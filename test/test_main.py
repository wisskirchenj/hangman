from io import StringIO
from unittest.mock import patch
import unittest

from hangman.main import main, random_word, WORDS


class HangmanTest(unittest.TestCase):

    def test_random_word(self):
        self.assertIn(random_word(), WORDS)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage3_win_or_loose(self, mock_stdout: StringIO, mock_input):
        mock_args = ['java']
        mock_input.side_effect = mock_args
        main()
        self.assertTrue(mock_stdout.getvalue().find('You survived!') >= 0 or
                        mock_stdout.getvalue().find('You lost!') >= 0)
