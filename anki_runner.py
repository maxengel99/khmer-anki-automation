from KhmerLetters import KhmerLetters
from AnkiRequest import AnkiRequest
import sys


def create_audio():
    khmer_letters = KhmerLetters()
    combination_arr = khmer_letters.create_combinations()
    khmer_letters.get_audio(combination_arr)

def add_anki():
    khmer_letters = KhmerLetters()
    anki_request = AnkiRequest()
    combination_arr = khmer_letters.create_combinations()

    for combination in combination_arr:
        anki_arg = anki_request.generate_json_args(combination)
        response = anki_request.invoke(anki_arg)
        print(response)

if __name__ == '__main__':
    if sys.argv[1] == 'audio':
        create_audio()
    elif sys.argv[1] == 'anki':
        add_anki()