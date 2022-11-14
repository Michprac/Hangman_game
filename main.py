#THE IDEA WAS TAKEN FROM THE YouTube

import random
import string
from words import words, prompts


def get_valid_word(list_of_words, list_of_prompts):  # choising word without any symbol like space or hyphen
    word = random.choice(list_of_words)
    while '-' in word or ' ' in word:
        word = random.choice(list_of_words)   #output word
    index_of_word = list_of_words.index(word);   #getting index of chosen word in "words" list
    prompts_for_game = list_of_prompts[index_of_word]   #output prompts
    return word, prompts_for_game

def hangman():
    chosen_word, prompts_for_word = get_valid_word(words, prompts)
    word_for_game = chosen_word.upper()
    letters_of_word = set(word_for_game)
    alphabet = set(string.ascii_uppercase)  # list of letters for guessing
    used_letters = set()
    lives = 5   # you have 5 attempts for make mistake
    prompts_counter = 0

    while len(letters_of_word) > 0 and lives > 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("You have {}".format(lives), "lives and you have used these letters: ", ' '.join(used_letters))
        current_word = [letter if letter in used_letters else '_' for letter in word_for_game]
        print("Current word:", ' '.join(current_word))

        guess = input("Please, choose a letter (for a prompt choose '?', -1 leave): ").upper()   # user is choosing a letter.
        if guess in (alphabet - used_letters):               # It is uppercase, because we work with this font
            used_letters.add(guess)
            if guess in letters_of_word:
                letters_of_word.remove(guess)   # removing correct letter from list of target word
            else:
                lives = lives - 1
        elif guess in used_letters:
            print("\n !!!You have already used this letter. Please, choose another!!! \n")
        elif guess == '?':
            if prompts_counter < 3:
                print(f"???? Your prompt: {prompts_for_word[prompts_counter].upper()} ????")
                print("-1 live")
                lives = lives - 1
                prompts_counter = prompts_counter + 1
            else:
                print("???? Sorry, there are no more prompts for the word ????")
        else:
            print("There is no such kind of symbol in this list")
    if lives == 0:
        print("\nYou loose :(\nThe right word is {}".format(word_for_game))
    else:
        print("\nYou win ;)\nThe right word is {}".format(word_for_game))


hangman()