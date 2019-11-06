from KhmerLetters import KhmerLetters
import json
import urllib.request


def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}


def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(
        urllib.request.Request('http://localhost:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']


def generate_json_args(combination):
    fields = {'Word': combination}
    audio_url = 'https://raw.githubusercontent.com/maxengel99/khmer-letter-anki/master/files/{}.mp3'.format(
        combination)
    audio_json = {'url': audio_url,
                  'filename': '{}.mp3'.format(combination), 'fields': ['Audio']}
    json_args = {'deckName': 'Khmer Letters', 'modelName': 'Basic - Word/Audio', 'fields': fields,
                 'options': {'allowDuplicate': False}, 'tags': [], 'audio': audio_json}
    return {'action': 'addNote', 'params': {'note': json_args}, 'version': 6}


khmer_letters = KhmerLetters()
combination_arr = khmer_letters.create_combinations()

for combination in combination_arr:
    anki_arg = generate_json_args(combination)
    response = json.load(urllib.request.urlopen(
        'http://localhost:8765', json.dumps(anki_arg).encode('utf-8')))
    print(response)
