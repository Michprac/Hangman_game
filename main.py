import random
import string
from words import words


def get_valid_word(list_of_words):  # choising word without any symbol like space or hyphen
    word = random.choice(list_of_words)
    while '-' in word or ' ' in word:
        word = random.choice(list_of_words)
