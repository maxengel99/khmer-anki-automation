import easygui
import os
from github_handler import GithubHandler
from helper import create_audio


def begin():
    '''Starts the textbox conversation'''

    category = easygui.buttonbox("Would you like to upload letters or vocabulary?", choices=('Letters', 'Vocabulary'))

    if(category == "Vocabulary"):
        vocab_file_name = easygui.fileopenbox("Please upload a textfile of the new vocabulary.")
        vocab_file_open = (open(vocab_file_name, 'r', encoding='utf8', errors='ignore'))
        vocab_file_content = vocab_file_open.readlines()
        
        print("Uploading text file")

        khmer_english_pair_arr = []
        for line in vocab_file_content:
            khmer_english_pair = line.rstrip().split('/')
            khmer_english_pair_arr.append(khmer_english_pair)

        print("Creating Khmer-English array")
        
        audio_option = easygui.ynbox("Do you need to create audio?", choices=("Yes", "No"))

        if audio_option:
            github_handler = GithubHandler()

            for pair in khmer_english_pair_arr:
                if not os.path.isfile('files/words/{}.mp3'.format(pair[0])):
                    create_audio("words", pair[0])
                    print("Creating audio for - {}".format(pair[1]))
                else:
                    print("Skipping word - {}".format(pair[1]))
            
            print("Completed creating audio")
            
            commit_message = easygui.enterbox()
            github_handler.add_to_github(commit_message)

    elif(category.lower() == "letters"):
        easygui.msgbox("letters")

    user_continue = easygui.ynbox("Would you like to perform another command?", choices=("Yes", "No"))
    if user_continue:
        begin()
    else:
        exit()

if __name__ == '__main__':
    begin()