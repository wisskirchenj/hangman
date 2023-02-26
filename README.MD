# IDEA EDU Course

Project implemented in the track 'Python for Beginners' of hyperskill.org JetBrains Academy. Purpose of doing this
project is to further practice and stay in touch with Python programming.

## Technology / External Libraries

- Python 3.11.2,
- with packages: argparse, math, io, unittest, unittest.mock

## Repository Contents

The sources of main project tasks (8 stages) and pytest testing.

## Installation

Install the wheel file using pip after clone/fork:

    > pip install dist/hangman-3.11.2.post1-py3-none-any.whl

## Program description

Hangman is a popular yet grim puzzle game. A cruel computer hides a word from you, which you try to guess letter by letter.
If you fail, you'll be “hanged”. If you win, you'll survive.

Have fun!

## Project completion

[//]: # (Project was completed on 08.01.23)

## Progress

25.02.23 Project started - gitHub repo and project structure setup.

25.02.23 Stage 1 completed. Just print output.

25.02.23 Stage 2 completed. Just one word guess.

25.02.23 Stage 3 completed. A word guess for a randomly picked word from a given list.

25.02.23 Stage 4 completed. A word guess for a randomly picked word from a given list - now with three beginning letters
shown and '-' for missing letters. MagicMock.assert_called_with() used.

26.02.23 Stage 5 completed. Real hangman game with covered letters and 8 tries - but without ready check still. Used map()

26.02.23 Stage 6 completed. Complete hangman game now with 8 allowed fail attempts and proper win / loose message.
