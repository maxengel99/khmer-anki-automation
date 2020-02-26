import json
import requests

vocab_file = open("test.txt", "r", encoding="utf8", errors="ignore")
vocab_content = vocab_file.readlines()

khmer_def_pair_arr = []

for line in vocab_content:
    updated_line = line.replace('\u200b', '')
    khmer_def_pair = updated_line.rstrip().split('/')
    khmer_def_pair_arr.append(khmer_def_pair)


for word in khmer_def_pair_arr:
    url = "https://kheng.info/static/dictionary/audio/" + word[1] + ".mp3"
    doc = requests.get(url)

    if doc.status_code == 200:
        filename = 'files/{}/{}.mp3'.format("words", word[1])
        with open(filename, "wb") as file:
            print('writing file {}'.format(filename))
            file.write(doc.content)
    else:
        print(doc.status_code)