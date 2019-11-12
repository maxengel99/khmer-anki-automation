import requests


class KhmerLetters:

    def __init__(self):
        self.consonant_arr = ['ក', 'គ', 'ខ', 'ឃ', 'ង', 'ង៉', 'ច', 'ជ']
        self.vowel_arr = ['', 'ា', 'ិ', 'ី', 'ឹ']

    def create_combinations(self):
        combined_arr = []
        for consonant in self.consonant_arr:
            for vowel in self.vowel_arr:
                combined_arr.append(consonant + vowel)

        return combined_arr

    def get_audio(self, combined_arr):
        for combination in combined_arr:
            url ='https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q={}'.format(combination)
            doc = requests.get(url)
            filename = 'files/{}.mp3'.format(combination)
            with open(filename, "wb") as f:
                f.write(doc.content)
