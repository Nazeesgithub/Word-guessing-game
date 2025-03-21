import random
import time

# Function to load words from a text file
def load_words_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

# Function to display the hangman when user enters a wrong letter
def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    print(stages[7 - attempts])

# Function to play the guessing game
def guessing_game():
    fruits = load_words_from_file("c:\\Users\\nazee\\Desktop\\coding-lesson\\PYTHON\\word guesser\\fruits.txt")  # my txt file location
    if not fruits:
        print("No fruits found. Please check the file.")
        return

    # Difficulty levels
    print("Choose difficulty level:")
    print("1. Easy (8 attempts)")
    print("2. Medium (6 attempts)")
    print("3. Hard (4 attempts)")
    difficulty = input("Enter your choice (1/2/3): ")

    if difficulty == "1":
        attempts = 8
    elif difficulty == "2":
        attempts = 6
    elif difficulty == "3":
        attempts = 4
    else:
        print("Invalid choice. Defaulting to Easy difficulty.")
        attempts = 8

    # Select a random fruit
    word = random.choice(fruits).lower()
    guessed_word = ["_"] * len(word)  # underscores for unguessed letters
    guesses = set()  # Track guessed letters
    start_time = time.time()  # Start timer
    print("*-------------------------------------------------------------------------------*")
    print("*                                                                               *")
    print("*-------------Welcome to the fruit Guessing Game with hangman!----------------- *")
    print("*                                                                               *")
    print("*-------------------------------------------------------------------------------*")

    print ("About game:\n  Guess the words to Identify the random fruit \n you will have 7 chances to find the  ");
    print(f"You have {attempts} attempts to guess the fruit.")
    print(" ".join(guessed_word))  # Display initial state of the word

    while attempts > 0:
        guess = input("\nGuess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guesses:
            print(f"You've already guessed '{guess}'. Try a different letter.")
            continue

        # Add the guess to the set of guessed letters
        guesses.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            # Update the guessed_word with the correctly guessed letter
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word. You have {attempts} attempts left.")
            display_hangman(attempts)  # Display hangman art

        # Display the current state of the word
        print(" ".join(guessed_word))

        # Check if the player has guessed the entire word
        if "_" not in guessed_word:
            end_time = time.time()
            time_taken = int(end_time - start_time)
            print(f"\nCongratulations! You guessed the fruit: {word}")
            print(f"Time taken: {time_taken} seconds")
            return

    # If the player runs out of attempts
    print(f"\nOut of attempts! The fruit was: {word}")

# Run the game
guessing_game()