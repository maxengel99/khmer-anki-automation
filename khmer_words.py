'''Handles creating khmer words'''


class KhmerWords:
    '''Handles creating khmer words'''

    def __init__(self, file='lesson12.txt'):
        self.file = file

    def get_words(self):
        '''Gets words from text file'''

        input_file = open(self.file, 'r', encoding='utf8', errors='ignore')
        file_content = input_file.readlines()

        khmer_english_pair_arr = []
        for line in file_content:
            khmer_english_pair = line.rstrip().split('/')
            khmer_english_pair_arr.append(khmer_english_pair)

        return khmer_english_pair_arr
