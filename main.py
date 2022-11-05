#THE IDEA WAS TAKEN FROM THE YouTube

import random
import string
from words import words


def get_valid_word(list_of_words):  # choising word without any symbol like space or hyphen
    word = random.choice(list_of_words)
    while '-' in word or ' ' in word:
        word = random.choice(list_of_words)
    return word

def hangman():
    word_for_game = get_valid_word(words).upper()
    letters_of_word = set(word_for_game)
    alphabet = set(string.ascii_uppercase)  # list of letters for guessing
    used_letters = set()
    lives = 5   # you have 5 attempts for make mistake

    while len(letters_of_word) > 0 and lives > 0:
        print("You have {}".format(lives), " lives and you have used these letters: ", ' '.join(used_letters))
        current_word = [letter if letter in used_letters else '_' for letter in word_for_game]
        print(f"Current word:{current_word}")

        guess = input("Please, choose a letter: ") #user is choosing a letter
        if guess in (alphabet - used_letters):
            used_letters.add(guess)
            if guess in letters_of_word:
                