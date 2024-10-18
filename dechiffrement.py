import os
import constantes
import crypto

def open_world_list(path: str) -> list[str]:
    """Ouvre un fichier contenant une liste de mots et retourne cette liste.

    Args:
        path (str): Chemin vers le fichier à ouvrir.

    Returns:
        list[str]: Liste des mots extraits du fichier.

    Raises:
        FileNotFoundError: Si le fichier n'est pas trouvé.
    """
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            words_list = [line.rstrip('\n') for line in lines]
        return words_list
    except FileNotFoundError:
        print('Language file not found')

def check_french_message(message: str) -> bool:
    """Vérifie si un message est potentiellement en français
    en comparant les mots à un dictionnaire de référence.

    Args:
        message (str): Message à vérifier.

    Returns:
        bool: True si le message semble être en français, sinon False.
    """
    mess = message.split(' ')
    for word in range(0, 4):
        if ("'" or "-" or "\n") not in mess[word]:
            if mess[word] not in constantes.DICO:
                return False
    return True

# Phase de test
if __name__ == '__main__':
    # Déchiffrement message1
    print('{0:=^120}'.format('MESSAGE-1'))
    mot = crypto.Substitution("message1_chiffre.txt")
    print(mot.decryptage_naif())

    # Déchiffrement message2
    print('{0:=^120}'.format('MESSAGE-2'))
    mot = crypto.Substitution("message2_chiffre.txt")
    print(mot.dechiffrement_vernam('CINQ'))

    # Déchiffrement message3
    print('{0:=^120}'.format('MESSAGE-3'))
    chars_grid = "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M"
    public_key = 'CRYPTO'
    test = crypto.Substitution('message3_chiffre.txt')
    decrypt_msg = test.dechiffrement_ADFGVX(chars_grid, public_key)
    print(decrypt_msg)
