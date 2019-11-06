from KhmerLetters import KhmerLetters
import json
import urllib.request


class AnkiRequest:

    def generate_json_args(self, combination):
        fields = {'Word': combination}
        audio_url = 'https://raw.githubusercontent.com/maxengel99/khmer-letter-anki/master/files/{}.mp3'.format(
            combination)
        audio_json = {'url': audio_url,
                      'filename': '{}.mp3'.format(combination), 'fields': ['Audio']}
        json_args = {'deckName': 'Khmer Letters', 'modelName': 'Basic - Word/Audio', 'fields': fields,
                     'options': {'allowDuplicate': False}, 'tags': [], 'audio': audio_json}
        return {'action': 'addNote', 'params': {'note': json_args}, 'version': 6}

    def invoke(self, params):
        response = json.load(urllib.request.urlopen(
            'http://localhost:8765', json.dumps(params).encode('utf-8')))
        return response
