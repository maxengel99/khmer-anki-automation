'''Deals with audio'''
import requests


def create_audio(word):
    '''creates the audio file'''

    url = 'https://translate.google.com/translate_tts?'
    'ie=UTF-8&tl=km&client=tw-ob&q={}'.format(word)
    doc = requests.get(url)
    filename = 'files/{}.mp3'.format(word)
    with open(filename, "wb") as file:
        print('writing file {}'.format(filename))
        file.write(doc.content)
