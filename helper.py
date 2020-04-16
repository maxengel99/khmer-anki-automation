'''Deals with audio'''
import requests
import json


def create_audio(category, word):

    first_url = "https://kheng.info/static/dictionary/audio/" + word + ".mp3"
    doc = requests.get(first_url)

    if doc.status_code == 200:
        filename = 'files/{}/{}.mp3'.format("words", word)
        with open(filename, "wb") as file:
            print('writing file {}'.format(filename))
            file.write(doc.content)

        return

    print("First audio link doesn't have the file")

    '''creates the audio file'''
    url = "https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q=" + word

    # url = 'https://translate.google.com/translate_tts?'
    # 'ie=UTF-8&tl=km&client=tw-ob&q={}'.format(word)
    print(url)
    doc = requests.get(url)
    filename = 'files/{}/{}.mp3'.format(category, word)
    print(filename)
    with open(filename, "wb") as file:
        print('writing file {}'.format(filename))
        file.write(doc.content)
        print("File writing completed for " + word)

    return "completed"


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
