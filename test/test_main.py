from io import StringIO
from unittest.mock import patch
import unittest

from hangman.main import main


class HangmanTest(unittest.TestCase):

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage2_win_on_right_guess(self, mock_stdout: StringIO, mock_input):
        mock_args = ['python']
        mock_input.side_effect = mock_args
        main()
        assert mock_stdout.getvalue().find('You survived!') >= 0

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage2_loose_on_wrong_guess(self, mock_stdout: StringIO, mock_input):
        mock_args = ['wrong']
        mock_input.side_effect = mock_args
        main()
        assert mock_stdout.getvalue().find('You lost!') >= 0
