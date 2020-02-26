'''Deals with audio'''
import requests
import json


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


def create_audio_two(text):
    '''Creates audio file using Soundoftext API'''

    url = "https://api.soundoftext.com"
    headers = {'Content-type': 'application/json'}
    post_body = {
        "engine": "Google",
        "data": {
            "text": text,
            "voice": "km"
        }
    }

    response = requests.post(url, json=post_body, timeout=3)

    print(response.text)


if __name__ == '__main__':
    create_audio_two("សួស្តី")
