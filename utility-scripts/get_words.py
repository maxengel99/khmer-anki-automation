import json
import urllib.request

body_json_deck = {
    "action": "findNotes",
    "version": 6,
    "params": {
        "query": "deck:'Khmer Vocabulary - Khmer'"
    }
}

response = json.load(urllib.request.urlopen(
            'http://localhost:8765', json.dumps(body_json_deck).encode('utf-8')))

body_json_note = {
    "action": "notesInfo",
    "version": 6,
    "params": {
        "notes": response["result"]
    }
}

response = json.load(urllib.request.urlopen(
            'http://localhost:8765', json.dumps(body_json_note).encode('utf-8')))

f = open("all_vocab.txt", "w+", encoding="utf8", errors="ignore")

for note in response["result"]:
    f.write("{}/{}\ n".format(note["noteId"], note["fields"]["Khmer"]["value"]))