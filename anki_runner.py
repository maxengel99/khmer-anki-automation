from KhmerLetters import KhmerLetters
from AnkiRequest import AnkiRequest


def main():
    khmer_letters = KhmerLetters()
    anki_request = AnkiRequest()
    combination_arr = khmer_letters.create_combinations()

    for combination in combination_arr:
        anki_arg = anki_request.generate_json_args(combination)
        response = anki_request.invoke(anki_arg)
        print(response)


if __name__ == '__main__':
    main()
