import requests
import random
import string
import time
import urllib3
import sys

# Suppress SSL warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the API endpoint and seed
API_URL = "https://wordle.votee.dev:8000/random"
SEED = 1234  # Example seed value

# Track which letters are correct, present, and absent
correct_positions = [None] * 5
present_letters = set()
absent_letters = set()

# Function to generate a filtered random word based on previous feedback
def generate_filtered_word():
    word = []
    for i in range(5):
        if correct_positions[i]:
            word.append(correct_positions[i])  # Use correct letter
        else:
            # Avoid using absent letters or repeating present letters too much
            letter = random.choice([ch for ch in string.ascii_lowercase if ch not in absent_letters])
            word.append(letter)
    return ''.join(word)

# Function to process the response and update the feedback
def process_response(guess, response):
    global correct_positions, present_letters, absent_letters
    for i, feedback in enumerate(response):
        letter = guess[i]
        result = feedback["result"]
        if result == "correct":
            correct_positions[i] = letter
        elif result == "present":
            present_letters.add(letter)
        elif result == "absent":
            absent_letters.add(letter)

# Function to make a guess and process feedback
def make_guess(seed=SEED):
    word = generate_filtered_word()
    url = f"{API_URL}?guess={word}&seed={seed}"
    try:
        # Send the GET request with SSL verification disabled
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            feedback = response.json()  # Parse JSON response
            print(f"Guess: {word}, Response: {feedback}")
            process_response(word, feedback)
            # Check if we've found the correct word
            if all(feedback[i]["result"] == "correct" for i in range(5)):
                print(f"Correct word found: {word}")
                return True
        else:
            print(f"Failed to guess '{word}' - Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
    return False

# Main function to guess random words
def guess_random_words():
    try:
        while True:
            if make_guess():
                break  # Exit loop when the correct word is found
            time.sleep(1)  # Delay between guesses
        sys.exit()  # Exit the program when the correct word is found
    except KeyboardInterrupt:
        print("Program interrupted. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    guess_random_words()
