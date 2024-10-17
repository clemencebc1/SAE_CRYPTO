
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
    mot = crypto.Substition("message1_chiffre.txt")
    print(mot.decryptage_naif())
    ciphered = "UCVLGH YUU BEQEMF TG ORETORI RIVDXQA QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O KEORBB"
    message_2 = crypto.Substition.dechiffrement_vernam(ciphered, "CINQ")
    print(message_2)
    message_3 = crypto.Substition("message3_chiffre.txt")
    grille = message_2.split()[6]
    mot_clef = message_2.split()[7]
    print(message_3.construction_grille(grille, "adfgvx"))

