'''Deals with audio'''
import requests


def create_audio(category, word):
    '''creates the audio file'''
    url="https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q=" + word

    #url = 'https://translate.google.com/translate_tts?'
    #'ie=UTF-8&tl=km&client=tw-ob&q={}'.format(word)
    print(url)
    doc = requests.get(url)
    filename = 'files/{}/{}.mp3'.format(category, word)
    print(filename)
    with open(filename, "wb") as file:
        print('writing file {}'.format(filename))
        file.write(doc.content)
