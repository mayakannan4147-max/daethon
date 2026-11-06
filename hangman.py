#!/usr/bin/env python3

import random

MAX_MISTAKES = 6

WORDS = [
    "apple",
    "banana",
    "orange",
    "pineapple",
    "computer",
    "python",
    "keyboard",
    "library",
    "galaxy",
    "mountain",
    "journey",
    "diamond",
    "treasure",
    "adventure",
    "garden",
    "sunshine",
    "shadow",
    "harvest",
    "captain",
    "rocket",
]

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
     / \\ |
          |
    =========
    """,
]


def choose_word(words=None):
    word_pool = words if words is not None else WORDS
    return random.choice(word_pool).lower()


def display_masked_word(secret_word, guessed_letters):
    masked = " "
    for letter in secret_word:
        if letter in guessed_letters:
            masked += f" {letter.upper()} "
        else:
            masked += " _ "
    return masked.strip()


def print_title():
    print("\n=== HANGMAN ===")


def print_status(secret_word, guessed_letters, wrong_guesses):
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Word: {display_masked_word(secret_word, guessed_letters)}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
    print(f"Mistakes left: {MAX_MISTAKES - wrong_guesses}")


def get_valid_guess(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter from A-Z.")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess.upper()}'. No penalty.")
            return None
        return guess


def play_game(secret_word=None):
    word = secret_word.lower() if secret_word else choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print_title()
    print("Guess the hidden word before the hangman is complete.")

    while wrong_guesses < MAX_MISTAKES:
        print_status(word, guessed_letters, wrong_guesses)
        guess = get_valid_guess(guessed_letters)
        if guess is None:
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Correct! '{guess.upper()}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong guess! '{guess.upper()}' is not in the word.")

        if all(letter in guessed_letters for letter in set(word)):
            print_status(word, guessed_letters, wrong_guesses)
            print("\nCongratulations! You won!")
            print(f"The word was: {word.upper()}")
            return True

        if wrong_guesses >= MAX_MISTAKES:
            print_status(word, guessed_letters, wrong_guesses)
            print("\nGame over! The hangman is complete.")
            print(f"The word was: {word.upper()}")
            return False

        print("-" * 40)

    return False


def main():
    while True:
        print_title()
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
