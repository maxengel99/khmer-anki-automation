import easygui
from git import Repo
from helper import create_audio

PATH_OF_GIT_REPO = r'.git'  # make sure .git folder is properly configured

def git_push():
def begin():
    
    category = easygui.buttonbox("Would you like to upload letters or vocabulary?", choices=('Letters', 'Vocabulary'))
    
    if(category.lower() == "vocabulary"):
        vocab_file_name = easygui.fileopenbox("Please upload a textfile of the new vocabulary.")
        vocab_file_open = (open(vocab_file_name, 'r', encoding='utf8', errors='ignore'))

        vocab_file_content = vocab_file_open.readlines()

        khmer_english_pair_arr = []
        for line in vocab_file_content:
            khmer_english_pair = line.rstrip().split('/')
            khmer_english_pair_arr.append(khmer_english_pair)
        
        for pair in khmer_english_pair:
            create_audio("words", pair[0])

    
    elif(category.lower() == "letters"):
        easygui.msgbox("etters")

    user_continue = easygui.ynbox("Would you like to perform another command?", choices=("Yes", "No"))
    if user_continue:
        begin()
    else:
        exit()

if __name__ == '__main__':
    begin()