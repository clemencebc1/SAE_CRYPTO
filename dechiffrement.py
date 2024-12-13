
import os
import constantes
import crypto

def open_world_list(path:str) -> list[str]:
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            words_list = [line.rstrip('\n') for line in lines]
        return words_list
    except FileNotFoundError:
        print('language file not found')

def check_french_message(message:str) -> bool:
    mess = message.split(' ')
    for word in range(0,4):
        if ("'" or "-" or "\n") not in mess[word]:
            if mess[word] not in constantes.DICO:
                return False
    return True
                
#phase de test ==> appuyez sur la petite fleche en haut a droite
if __name__ == '__main__':
    #Dechiffrement message1
    print('{0:=^120}'.format('MESSAGE-1'))
    mot = crypto.Substition("message1_chiffre.txt")
    print(mot.decryptage_naif())

    #Dechiffrement message2
    print('{0:=^120}'.format('MESSAGE-2'))
    mot = crypto.Substition("message2_chiffre.txt")
    print(mot.dechiffrement_vernam('CINQ'))

    #Dechifrement message3
    print('{0:=^120}'.format('MESSAGE-3'))
    chars_grid = "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M"
    public_key = 'CRYPTO'
    test = crypto.Substition('message3_chiffre.txt')
    decrypt_msg = test.dechiffrement_message_ADFGVX(chars_grid,public_key)
    print(decrypt_msg)

