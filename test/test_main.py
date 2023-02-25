from io import StringIO
from unittest.mock import patch, MagicMock
import unittest

from hangman.main import main, random_word


class HangmanTest(unittest.TestCase):

    def test_random_word(self):
        self.assertEquals(random_word(1), 'java')
        self.assertEquals(random_word(44), 'javascript')
        self.assertEquals(random_word(55), 'python')
        self.assertEquals(random_word(333), 'swift')

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage4_win(self, mock_stdout: StringIO, mock_input):
        mock_args = ['java']
        mock_input.side_effect = mock_args
        main(seed=1)
        self.assertTrue(mock_stdout.getvalue().find('You survived!') >= 0)

    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_stage4_loose(self, mock_stdout: StringIO, mock_input):
        mock_args = ['java']
        mock_input.side_effect = mock_args
        main(seed=55)
        self.assertTrue(mock_stdout.getvalue().find('You lost!') >= 0)

    @patch('builtins.input')
    def test_stage4_hidden_word(self, mock_input: MagicMock):
        main(seed=55)
        mock_input.assert_called_once_with('Guess the word pyt---: ')
        main(seed=44)
        mock_input.assert_called_with('Guess the word jav-------: ')