from KhmerLetters import KhmerLetters
from khmer_words import KhmerWords
from AnkiRequest import AnkiRequest
import sys


def create_audio():
    khmer_letters = KhmerLetters()
    combination_arr = khmer_letters.create_combinations()
    khmer_letters.get_audio(combination_arr)

def create_vocab_audio():
    khmer_words = KhmerWords()
    khmer_word_combo = khmer_words.get_words()
    khmer_words.create_audio(khmer_word_combo)

def add_anki():
    khmer_letters = KhmerLetters()
    anki_request = AnkiRequest()
    combination_arr = khmer_letters.create_combinations()

    for combination in combination_arr:
        anki_arg = anki_request.generate_json_args(combination)
        response = anki_request.invoke(anki_arg)
        print(response)
    
def add_anki_vocab():
    khmer_words = KhmerWords()
    anki_request = AnkiRequest()
    khmer_words_list = khmer_words.get_words()
    
    for word in khmer_words_list:
        anki_arg = anki_request.generate_json_args_vocab(word[0], word[1])
        response = anki_request.invoke(anki_arg)
        print(response)

if __name__ == '__main__':
    if sys.argv[1] == 'audio':
        create_audio()
    elif sys.argv[1] == 'anki':
        add_anki()
    elif sys.argv[1] == 'vocab':
        create_vocab_audio()
    elif sys.argv[1] == 'anki_vocab':
        add_anki_vocab()