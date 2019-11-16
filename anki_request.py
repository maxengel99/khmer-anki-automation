'''Handles interaction with anki'''
import json
import urllib.request


class AnkiRequest:
    """Handles interaction with anki"""

    def generate_json(self, category, khmer, english='none'):
        """Create json for anki"""
        fields = ({'Word': khmer} if category == 'letter'
                  else {'Khmer': khmer, 'English': english})
        audio_url = ('https://raw.githubusercontent.com/maxengel99/'
                     'khmer-letter-anki/master/files/{}.mp3'.format(khmer))
        audio_json = {'url': audio_url, 'filename': '{}.mp3'.format(khmer),
                      'fields': ['Audio']}
        deck_name = ('Khmer Letters' if category == 'letter'
                     else 'Khmer Vocabulary -  Khmer')
        model_name = ('Basic - Word/Audio' if category == 'letter'
                      else 'Khmer Vocabulary')
        json_args = {'deckName': deck_name, 'modelName': model_name,
                     'fields': fields, 'options': {'allowDuplicate': False},
                     'tags': [], 'audio': audio_json}
        return {'action': 'addNote', 'params': {'note': json_args},
                'version': 6}

    def generate_json_args(self, combination):
        '''Generates the json'''
        fields = {'Word': combination}
        audio_url = 'https://raw.githubusercontent.com/maxengel99/khmer-letter-anki/master/files/{}.mp3'.format(
            combination)
        audio_json = {'url': audio_url,
                      'filename': '{}.mp3'.format(combination), 'fields': ['Audio']}
        json_args = {'deckName': 'Khmer Letters', 'modelName': 'Basic - Word/Audio', 'fields': fields,
                     'options': {'allowDuplicate': False}, 'tags': [], 'audio': audio_json}
        return {'action': 'addNote', 'params': {'note': json_args}, 'version': 6}

    def invoke(self, params):
        """Makes request to add anki card"""
        response = json.load(urllib.request.urlopen(
            'http://localhost:8765', json.dumps(params).encode('utf-8')))
        return response

    def generate_json_args_vocab(self, khmer_word, english_word):
        fields = {'Khmer': khmer_word, 'English': english_word}
        audio_url = 'https://raw.githubusercontent.com/maxengel99/khmer-letter-anki/master/files/{}.mp3'.format(
            khmer_word)
        audio_json = {'url': audio_url,
                      'filename': '{}.mp3'.format(khmer_word), 'fields': ['Audio']}
        json_args = {'deckName': 'Khmer Vocabulary - Khmer', 'modelName': 'Khmer Vocabulary', 'fields': fields,
                     'options': {'allowDuplicate': False}, 'tags': [], 'audio': audio_json}
        return {'action': 'addNote', 'params': {'note': json_args}, 'version': 6}
