# Python Word Guessing Game

## Description
This Python program automatically guesses words against a Wordle-like API. Using feedback from previous guesses, the program refines its future guesses until it finds the correct word. 

## Features
- Generates random 5-letter word guesses.
- Processes feedback to track correct letters, present letters, and absent letters.
- Continues guessing until the correct word is found.
- Supports running in a command-line interface.
- Suppresses SSL warnings for insecure connections.

## Requirements
- Python 3.x
- `requests` library

## Installation
1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Install the required packages (if requests is not installed):

   ```bash
   pip install requests

## Usage
1. Open a terminal and navigate to the project directory.

2. Run the program:
   ```bash
    python word_guess.py

3. The program will continuously make guesses until it finds the correct word.

## Example Output

    ```css
    Guess: bjyom, Response: [{'slot': 0, 'guess': 'b', 'result': 'absent'}, {'slot': 1, 'guess': 'j', 'result': 'absent'}, ...]
    Guess: theft, Response: [{'slot': 0, 'guess': 't', 'result': 'correct'}, ...]
    Correct word found: theft

## Acknowledgments

- **Code Assistance**: Special thanks to ChatGPT for providing valuable guidance and code examples throughout the development of this project.


