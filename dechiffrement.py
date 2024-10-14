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