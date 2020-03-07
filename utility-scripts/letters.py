import json
import requests

consonant_arr = ['ក', 'គ', 'ខ', 'ឃ', 'ង', 'ង៉', 'ច', 'ជ', 'ឆ', 'ឈ', 'ញ', 'ញ៉',
                 'ដ', 'ឌ', 'ឋ', 'ឍ', 'ថ', 'ធ', 'ណ', 'ន', 'ត', 'ទ', 'ប', 'ប៊',
                 'ប៉', 'ព', 'ផ', 'ភ', 'ម៉', 'ម', 'យ៉', 'យ', 'រ៉', 'រ', 'ឡ',
                 'ល', 'វ៉', 'វ', 'ស', 'ស៊', 'ហ', 'ស៊', 'ហ', 'ហ៊', 'អ', 'អ៊']
new_vowels_arr = ['ោះ', 'ិះ', 'ឹះ']


def create_audio():
    combined_arr = []

    for consonant in consonant_arr:
        for vowel in new_vowels_arr:
            combined_arr.append(consonant + vowel)

    for combo in combined_arr:
        url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q=" + combo
        doc = requests.get(url)
        filename = 'files/letters/{}.mp3'.format(combo)
        with open(filename, "wb") as file:
            print('writing file {}'.format(filename))
            file.write(doc.content)


def add_to_anki():
    combined_arr = []

    for consonant in kl.consonant_arr:
        for vowel in kl.new_vowels_arr:
            combined_arr.append(consonant + vowel)

    for combo in combined_arr:
        """Create json for anki"""
        fields = {'Word': combo}
        audio_url = ('https://raw.githubusercontent.com/maxengel99/'
                     'khmer-letter-anki/master/files/letters/{}.mp3'.format(combo))
        audio_json = {'url': audio_url, 'filename': '{}.mp3'.format(combo),
                      'fields': ['Audio']}
        deck_name = 'Khmer Letters'
        model_name = 'Basic - Word/Audio'
        json_args = {'deckName': deck_name, 'modelName': model_name,
                     'fields': fields, 'options': {'allowDuplicate': False},
                     'tags': [], 'audio': audio_json}
        final_json = {'action': 'addNote', 'params': {'note': json_args}, 'version': 6}
        """Makes request to add anki card"""
        response = json.load(urllib.request.urlopen(
            'http://localhost:8765', json.dumps(params).encode('utf-8')))
        print(response)


if __name__ == '__main__':
    create_audio()
