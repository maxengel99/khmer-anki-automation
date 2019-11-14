import requests

class KhmerWords:

    def get_words(self):
        input_file = open('vocab.txt', 'r', encoding='utf8', errors='ignore')
        file_content = input_file.readlines()

        khmer_english_pair_arr = []
        for line in file_content:
            khmer_english_pair = line.rstrip().split('/')
            khmer_english_pair_arr.append(khmer_english_pair)
        
        print(khmer_english_pair_arr)    
        return khmer_english_pair_arr
    
    def create_audio(self, combo):
        for combination in combo:
            url = 'https://translate.google.com/translate_tts?ie=UTF-8&tl=km&client=tw-ob&q={}'.format(combination)
            doc = requests.get(url)
            filename = 'files/{}.mp3'.format(combination)
            with open(filename, "wb") as f:
                f.write(doc.content)
