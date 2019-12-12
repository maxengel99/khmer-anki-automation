'''Runs audio maker and anki adder'''
import sys
import os
from khmer_letters import KhmerLetters
from khmer_words import KhmerWords
from anki_request import AnkiRequest
from helper import create_audio


def create_letter_audio():
    """Creates letter audio files"""
    khmer_letters = KhmerLetters()
    letter_combinations_arr = khmer_letters.create_combinations()
    index = 1
    for combination in letter_combinations_arr:
        if not os.path.isfile('files/letters/{}.mp3'.format(combination)):
            create_audio("letters", combination)
        else:
            print("Skipping letter")
        print("{} / {}".format(index, len(letter_combinations_arr)))
        index += 1


def create_vocab_audio():
    """Creates vocab audio files"""
    khmer_words = KhmerWords()
    khmer_word_arr = khmer_words.get_words()
    for word in khmer_word_arr:
        create_audio(word[0])


def add_letter_anki():
    """Add letters to anki"""
    khmer_letters = KhmerLetters()
    anki_request = AnkiRequest()
    letter_combinations_arr = khmer_letters.create_combinations()

    index = 1
    for combination in letter_combinations_arr:
        anki_arg = anki_request.generate_json('letter', combination)
        response = anki_request.invoke(anki_arg)
        print(response)
        print("{} / {}".format(index, len(letter_combinations_arr)))
        index += 1


def add_anki_vocab():
    """Add vocab to anki"""
    khmer_words = KhmerWords()
    anki_request = AnkiRequest()
    khmer_words_list = khmer_words.get_words()

    for word in khmer_words_list:
        anki_arg = anki_request.generate_json('vocabulary', word[0], word[1])
        response = anki_request.invoke(anki_arg)
        print(response)


def get_combinations():
    khmer_letters = KhmerLetters()
    letter_combinations_arr = khmer_letters.create_combinations()
    for combo in letter_combinations_arr:
        print(combo)

if __name__ == '__main__':
    if sys.argv[1] == 'letter_audio':
        create_letter_audio()
    elif sys.argv[1] == 'vocab_audio':
        create_vocab_audio()
    elif sys.argv[1] == 'letter_anki':
        add_letter_anki()
    elif sys.argv[1] == 'vocab_anki':
        add_anki_vocab()
    elif sys.argv[1] == 'combination':
        get_combinations()
        