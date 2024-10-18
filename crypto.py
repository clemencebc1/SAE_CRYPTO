#!/usr/bin/python3

from textwrap import wrap
import constantes
import dechiffrement

class Substitution:

    def __init__(self, fichier):
        """Initialise la classe avec le fichier donné.

        Args:
            fichier (str): Le nom du fichier à ouvrir.
        """
        self.fichier = open(fichier, "r").read()

    def passage_pourcentage(self, dictionnaire_apparation, longueur):
        """Convertit les occurrences d'apparition des lettres en pourcentage.

        Args:
            dictionnaire_apparation (dict): Dictionnaire d'occurrence des lettres.
            longueur (int): Longueur totale du message.

        Returns:
            dict: Dictionnaire avec les fréquences en pourcentage.
        """
        dictionnaire_frequence = dict()
        for key, value in dictionnaire_apparation.items():
            dictionnaire_frequence[key] = value * 100 / longueur
        return dictionnaire_frequence

    def frequence_lettres(self):
        """Calcule la fréquence d'apparition de chaque lettre dans le fichier.

        Returns:
            dict: Dictionnaire des lettres et de leurs occurrences.
        """
        dico_apparition = {}
        mes = self.fichier.split("\n")
        for line in mes:
            for char in line:
                if char.isalpha():
                    if char not in dico_apparition.keys():
                        dico_apparition[char] = 1
                    else:
                        dico_apparition[char] += 1
        return dico_apparition

    def compare_frequence_lettres(self):
        """Compare les fréquences des lettres dans le fichier à une distribution de référence."""
        return None

    def longueur_message(self):
        """Calcule la longueur totale du message, c'est-à-dire le nombre de caractères.

        Returns:
            int: Longueur du message.
        """
        longueur = 0
        for line in self.fichier:
            longueur += len(line)
        return longueur

    def decrypt(self, cle: int) -> str:
        """Déchiffre le message en utilisant une clé de substitution.

        Args:
            cle (int): Le nombre de décalage de l'alphabet.

        Returns:
            str: Le message déchiffré.
        """
        res = ""
        for line in self.fichier:
            for char in line:
                if not char.isalpha():
                    res += char
                    continue
                index = constantes.ALPHABET.index(char.lower())
                nv_char = constantes.ALPHABET[(index - cle) % constantes.ALPHABET_SIZE]
                res += nv_char
        return res

    def decryptage_naif(self):
        """Déchiffre un message en essayant toutes les clés possibles (version naïve).

        Returns:
            str: Le message déchiffré correct.
        """
        for cle in range(1, constantes.ALPHABET_SIZE):
            message = self.decrypt(cle)
            if dechiffrement.check_french_message(message):
                return message
        return self.fichier

    def ascii_caractere(self, carac, indice):
        """Modifie un caractère ASCII en ajoutant un indice, si cela dépasse 123, on revient à 122.

        Args:
            carac (str): Le caractère à modifier.
            indice (int): L'indice de décalage.

        Returns:
            int: Le nouveau code ASCII.
        """
        code = ord(carac)
        if code + indice > 123:
            code += (122 - code)

    def dechiffrement_vernam(self, key: str):
        """Déchiffre un message chiffré avec la méthode de Vernam.

        Args:
            key (str): La clé utilisée pour le chiffrement.

        Returns:
            str: Le message déchiffré.
        """
        liste_mot = self.fichier.split(' ')
        liste_mot = [mot.rstrip('\n') for mot in liste_mot]
        ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key_index = 0

        result = []
        for word in liste_mot:
            result_word = ""
            for letter in word:
                if key_index < len(key):
                    if letter in ALPHA:
                        deciphered_letter_index = (ALPHA.index(letter) - ALPHA.index(key[key_index])) % 26
                        result_word += ALPHA[deciphered_letter_index]
                        key_index += 1
                    else:
                        result_word += letter
                else:
                    key_index = 0
                    if letter in ALPHA:
                        deciphered_letter_index = (ALPHA.index(letter) - ALPHA.index(key[key_index])) % 26
                        result_word += ALPHA[deciphered_letter_index]
                        key_index += 1
                    else:
                        result_word += letter
            result.append(result_word)
        result = ' '.join(result)
        return result

    def dechiffrement_ADFGVX(self, bind_grid: str, public_key: str = 'CRYPTO') -> str:
        """Déchiffre un message chiffré avec la méthode ADFGVX.

        Args:
            bind_grid (str): La grille de chiffrement.
            public_key (str, optional): La clé publique. Par défaut 'CRYPTO'.

        Returns:
            str: Le message déchiffré.
        """
        matrix = build_matrix_key(self.fichier, public_key)
        decyphering_grid = build_decyphering_grid(matrix, public_key)
        cyphering_grid = build_cyphering_grid(chars_grid=bind_grid)
        antigramme = build_antigramme(decyphering_grid)
        clear_msg = decrypt_antigramme(cyphering_grid, antigramme)
        clear_msg = clear_msg.replace('  ', '\n')
        return clear_msg


# ================================== ADFGVX Functions ================================== #

def build_matrix_key(msg: str, key: str) -> list[list[str]]:
    """Crée une matrice du message parfaitement divisé en colonnes selon la longueur de la clé.

    Args:
        msg (str): Le message chiffré.
        key (str): La clé de la matrice.

    Returns:
        list[list[str]]: La matrice des colonnes.
    """
    lines = msg.splitlines()
    cut_msg = ""
    first_line = True
    matrix = []
    index = 0
    for ligne in lines:
        if ligne != "":
            if first_line:
                cut_msg += ligne
            else:
                cut_msg += " " + ligne
            first_line = False
    for i in range(1, len(key) + 1):
        msg_part = cut_msg[index:int(len(cut_msg) / 6) * i]
        matrix.append(list(msg_part))
        index = int(len(cut_msg) / 6) * i
    return matrix


def build_cyphering_grid(chars_grid: str = 'AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M') -> dict[str, list]:
    """Construit la grille de chiffrement ADFGVX.

    Args:
        chars_grid (str, optional): La grille de caractères. Par défaut une valeur prédéfinie.

    Returns:
        dict: La grille de chiffrement.
    """
    KEY = "ADFGVX"
    if len(chars_grid) != 36:
        return "Longueur de grille incorrecte"
    cyphering_grid = {}
    index = 0
    for i in range(1, 7):
        for k in range(1, 7):
            current_key = KEY[i - 1] + KEY[k - 1]
            current_char = chars_grid[index]
            cyphering_grid[current_key] = current_char
            index += 1
    return cyphering_grid


def build_antigramme(decyphering_grid: dict, key: str = 'CRYPTO') -> list[str]:
    """Construit l'antigramme utilisé pour déchiffrer le message ADFGVX.

    Args:
        decyphering_grid (dict): La grille de déchiffrement.
        key (str, optional): La clé publique. Par défaut 'CRYPTO'.

    Returns:
        list[str]: L'antigramme du message.
    """
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    iter = len(decyphering_grid[key[0]])
    res = []
    cyphered_antigramme = ''
    splited_antigramme = ''
    for i in range(iter):
        for value in decyphering_grid.values():
            cyphered_antigramme += value[i]
    for i in range(len(cyphered_antigramme)):
        if cyphered_antigramme[i] in ALPHA:
            splited_antigramme += cyphered_antigramme[i]
        else:
            res.append(cyphered_antigramme[i])
        if len(splited_antigramme) == 2:
            res.append(splited_antigramme)
            splited_antigramme = ''
    return res


def decrypt_antigramme(ciphering_grid: dict, antigramme: list[str]) -> str:
    """Déchiffre l'antigramme pour récupérer le message.

    Args:
        ciphering_grid (dict): La grille de chiffrement.
        antigramme (list[str]): L'antigramme à déchiffrer.

    Returns:
        str: Le message déchiffré.
    """
    res = ""
    antigramme_array = []
    for combinaison in antigramme:
        valid = True
        for letter in combinaison:
            if letter not in 'ADFGVX':
                valid = False
        if valid:
            antigramme_array.append(ciphering_grid[combinaison])
        else:
            antigramme_array.append(combinaison)
    res = res.join(antigramme_array)
    return res


def build_decyphering_grid(matrice: list[list[str]], key: str) -> dict[str, list]:
    """Construit la grille de déchiffrement à partir de la matrice et de la clé.

    Args:
        matrice (list[list[str]]): La matrice du message.
        key (str): La clé publique.

    Returns:
        dict: La grille de déchiffrement.
    """
    if len(key) != 6:
        return "Clé incorrecte"
    keys = [l for l in key]
    sorted_keys = sorted(keys)
    decyphering_grid = {}
    for letter in key:
        i = sorted_keys.index(letter)
        value = matrice[i]
        decyphering_grid[letter] = value
    return decyphering_grid
