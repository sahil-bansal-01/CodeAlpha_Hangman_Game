"""
Hangman Game
------------
A classic text-based Hangman game where the player guesses a randomly selected word.
Includes game statistics, input validation, and ASCII art.
"""

import random

# ASCII Art representations for the Hangman stages corresponding to incorrect guesses (0 to 6)
HANGMAN_STAGES = [
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def choose_word():
    """
    Selects and returns a random word from a predefined list of 5 words.
    """
    words = ["apple", "banana", "mango", "strawberry", 
"orange", "grape", "pineapple", "apricot", "lemon", "coconut", "watermelon", 
"cherry", "papaya", "berry", "peach", "lychee", "muskmelon"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Constructs the display string showing guessed letters and underscores.
    
    Parameters:
        word (str): The target word to guess.
        guessed_letters (list): Letters guessed by the player so far.
        
    Returns:
        str: The formatted string with revealed letters and underscores (e.g. "p y _ h o n").
    """
    revealed_word = []
    for letter in word:
        if letter in guessed_letters:
            revealed_word.append(letter)
        else:
            revealed_word.append("_")
    return " ".join(revealed_word)

def get_valid_guess(guessed_letters):
    """
    Prompts the user for a single letter and validates the input.
    Ensures input is a single alphabetic character that hasn't been guessed yet.
    """
    while True:
        guess = input("Guess a letter: ").strip().lower()

        # Validation 1: Check if input is empty
        if not guess:
            print("Error: Input cannot be empty. Please enter a letter.")
            continue

        # Validation 2: Check if more than one character was entered
        if len(guess) > 1:
            print("Error: Please enter only one letter at a time.")
            continue

        # Validation 3: Check if input is not a letter (e.g. number or symbol)
        if not guess.isalpha():
            print("Error: Invalid character. Please enter an alphabetic letter (A-Z).")
            continue

        # Validation 4: Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"Error: You have already guessed '{guess}'. Try a different letter.")
            continue

        # If all checks pass, return the valid guess
        return guess

def play_game(stats):
    """
    Runs a single game session of Hangman. Updates statistics in-place.
    
    Parameters:
        stats (dict): A dictionary tracking 'total', 'wins', and 'losses'.
    """
    # 1. Initialize game variables
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    stats["total"] += 1

    print("\n" + "=" * 45)
    print("                GAME STARTED!")
    print("=" * 45)

    # 2. Game loop
    while incorrect_guesses < max_incorrect:
        # Display current Hangman stage and game state
        print(HANGMAN_STAGES[incorrect_guesses])
        print(f"Word to guess: {display_word(word_to_guess, guessed_letters)}")
        print(f"Remaining attempts: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print("-" * 45)

        # Get a validated guess from the player
        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        # Check if the guess is in the secret word
        if guess in word_to_guess:
            print(f"\nGood job! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"\nOops! '{guess}' is not in the word.")

        # Check if player has guessed all letters in the word
        current_display = display_word(word_to_guess, guessed_letters).replace(" ", "")
        if current_display == word_to_guess:
            stats["wins"] += 1
            print(HANGMAN_STAGES[incorrect_guesses])
            print("*" * 45)
            print("🎉 CONGRATULATIONS! YOU WON! 🎉")
            print(f"You guessed the word: {word_to_guess.upper()}")
            print("*" * 45)
            break
    else:
        # This executes if the while loop completes without hitting 'break'
        stats["losses"] += 1
        print(HANGMAN_STAGES[incorrect_guesses])
        print("x" * 45)
        print("💀 GAME OVER! YOU RAN OUT OF ATTEMPTS! 💀")
        print(f"The correct word was: {word_to_guess.upper()}")
        print("x" * 45)

def play_again():
    """
    Asks the player if they want to play another game.
    Returns:
        bool: True if they want to play again, False otherwise.
    """
    while True:
        response = input("\nDo you want to play again? (yes/no or y/n): ").strip().lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    # Initialize game stats
    stats = {"total": 0, "wins": 0, "losses": 0}

    print("=" * 45)
    print("             WELCOME TO HANGMAN")
    print("=" * 45)

    # Outer loop to handle multiple games
    playing = True
    while playing:
        play_game(stats)

        # Display updated session stats
        print(f"\n--- SESSION STATISTICS ---")
        print(f"Total Games Played: {stats['total']}")
        print(f"Wins: {stats['wins']}")
        print(f"Losses: {stats['losses']}")
        print(f"Win Rate: {(stats['wins']/stats['total'])*100:.1f}%")
        print("--------------------------")

        playing = play_again()

    print("\nThank you for playing Hangman! Goodbye!")

if __name__ == "__main__":
    main()
