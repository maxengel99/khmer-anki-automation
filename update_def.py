import json
import urllib.request

vocab_file = open("vocab4.txt", "r", encoding="utf8", errors="ignore")
vocab_content = vocab_file.readlines()

khmer_def_pair_arr = []

for line in vocab_content:
    updated_line = line.replace('\u200b', '')
    khmer_def_pair = updated_line.rstrip().split('/')
    khmer_def_pair_arr.append(khmer_def_pair)

print(khmer_def_pair_arr)

for word in khmer_def_pair_arr:

    body_json_update = {
        "action": "updateNoteFields",
        "version": 6,
        "params": {
            "note": {
                "id": word[0],
                "fields": {
                    "English": word[2]
                }
            }
        }
    }

    response = json.load(urllib.request.urlopen(
        'http://localhost:8765', json.dumps(body_json_update).encode('utf-8')))
    print(response)