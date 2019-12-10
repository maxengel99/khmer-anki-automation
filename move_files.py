import shutil

consonant_arr = ['ក', 'គ', 'ខ', 'ឃ', 'ង', 'ង៉', 'ច', 'ជ',
                              'ឆ', 'ឈ', 'ញ', 'ញ៉', 'ដ', 'ឌ', 'ឋ', 'ឍ', 'ថ',
                              'ធ', 'ណ', 'ន', 'ត', 'ទ']
vowel_arr = ['', 'ា', 'ិ', 'ី', 'ឹ', 'ឺ', 'ុ', 'ូ', 'ួ', 'ើ', 'ឿ']

combo_arr= []

for consonant in consonant_arr:
    for vowel in vowel_arr:
        temp_letter = consonant + vowel
        combo_arr.append(temp_letter)

for combo in combo_arr:
    filename = './files/{}.mp3'.format(combo)
    new_filename = './files/letters/{}.mp3'.format(combo)
    shutil.move(filename, new_filename)