#!/usr/bin/python3

import os
def open_world_list(path:str) -> list[str]:
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            words_list = [line.rstrip('\n') for line in lines]
        return words_list
    except FileNotFoundError:
        print('language file not found')

def check_french_message(message:str, french_words: list[str]) -> bool:
    res = True
    message_word_list = message.split(' ')
    for word in message_word_list:
        if word not in french_words:
            res = False
    return res

#phase de test ==> appuyez sur la petite fleche en haut a droite
if __name__ == '__main__':
    print(open_world_list('french'),'\n', str(len(open_world_list('french'))))
    message_de_test = "ce texte est un message de test"
    print(f"test avec le message\n- '{message_de_test}'\nresult: {check_french_message(message_de_test, open_world_list('french'))}")