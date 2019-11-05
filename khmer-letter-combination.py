import requests

consonant_arr = ['ក','គ','ខ','ឃ',]
vowel_arr = ['','ា', 'ិ']

combined_arr = []
for consonant in consonant_arr:
    for vowel in vowel_arr:
        combined_arr.append(consonant + vowel)

for combination in combined_arr:
    url="https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q=" + combination
    doc = requests.get(url)
    filename = 'files/' + combination + ".mp3"
    with open(filename, "wb") as f:
        f.write(doc.content)