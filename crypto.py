#!/usr/bin/python3

from textwrap import wrap
import constantes

import dechiffrement

class Substition:

    def __init__ (self, fichier) :
        self.fichier = open(fichier, "r").read()

    def passage_pourcentage(self, dictionnaire_apparation, 
                            longueur):
        """a partir d'un dictionnaire d'occurence
        d'apparition d'une lettre, calcule la frequence
        d'apparition dans le mot

        Args:
            dictionnaire_apparation (dict): dico d'occurence
            longueur (int): longueur du message

        Returns:
            dict: dico de frequence
        """
        dictionnaire_frequence = dict()
        for key,value in dictionnaire_apparation.items():
            dictionnaire_frequence[key]=value*100/longueur
        return dictionnaire_frequence
            
    def frequence_lettres(self):
        dico_apparition = {}
        mes = self.fichier.split("\n")
        for line in mes:
            for char in line :
                # Est une lettre de l'alphabet
                if char.isalpha():
                    if char not in dico_apparition.keys():
                        dico_apparition[char] = 1
                    else :
                        dico_apparition[char] += 1
        return dico_apparition
        
    def compare_frequence_lettres(self):
        return None
    
    def longueur_message(self):
        """ Calcule la longueur totale du message, c'est à dire le nombre de caractère
        """
        longueur = 0
        for line in self.fichier:
            longueur += len(line)
        return longueur

    
    def decrypt(self, cle : int) -> str:
        """ Déchiffre le message en utilisant la clé de substitution

        Args:
            cle (int): le nombre de décalage de l'alphabet

        Returns:
            str: le message déchiffré
        """
        res = ""
        for line in self.fichier:
            for char in line :
                if not char.isalpha(): 
                    res += char
                    continue

                index = constantes.ALPHABET.index(char.lower()) # index de la lettre dans l'alphabet
                nv_char = constantes.ALPHABET[(index - cle) % constantes.ALPHABET_SIZE] # nouveau caractère (index - clé modulo 26) 

                res += nv_char
        return res
    

    # décryptage temporaire sans l'utilisation des fréquences
    def decryptage_naif(self):
        """ Déchiffre un message par substitution jusqu'à trouver un message cohérent (version naive)

        Returns:
            str: le message déchiffré correct
        """
        for cle in range(1, constantes.ALPHABET_SIZE):
            message = self.decrypt(cle)
            if dechiffrement.check_french_message(message):
                return message
        return self.fichier
    def ascii_caractere(self, carac, indice):
        code = ord(carac)
        if code+indice>123:
            code += (122-code)

    def dechiffrement_vernam(self, key:str):
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
                        result_word+=ALPHA[deciphered_letter_index]
                        key_index+=1
                    else:
                        result_word += letter
                else:
                    key_index=0
                    if letter in ALPHA:
                        deciphered_letter_index = (ALPHA.index(letter) - ALPHA.index(key[key_index])) % 26

                        result_word += ALPHA[deciphered_letter_index]
                        key_index+=1
                    else:
                        result_word += letter
            result.append(result_word)
        result = ' '.join(result)
        return result
    
    def dechiffrement_message_ADFGVX(self, bind_grid:str, public_key:str='CRYPTO'):
        matrix = build_matrix_key(self.fichier, public_key)
        uncyphering_grid = build_uncyphering_grid(matrix, public_key)
        cyphering_grid = build_cyphering_grid(chars_grid=bind_grid)
        antigramme = build_antigramme(uncyphering_grid)
        clear_msg = decrypt_antigramme(cyphering_grid,antigramme)
        clear_msg = clear_msg.replace('  ', '\n')
        return clear_msg
    
#=========================================================ADFGVX=============================================================================================================
def build_matrix_key(msg:str, key: str) -> list[list[str]]:
    """cree une matrice du message parfaitement divisé en n (longeur de la clé) colonnes, sous forme de liste de liste 
    Args:
        msg (str): message chiffre sous forme de triple-quoted
        strings ou de str simple (sur une ou plusieurs lignes) 
        key (str): la cle de la matrice 
    Returns:
        list[list[int]]: la matrice des colonnes
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
        msg = int(len(cut_msg) / 6) * i
        msg_part = cut_msg[index:msg]
        matrix.append(list(msg_part))
        index = msg
    return matrix

def build_cyphering_grid(chars_grid:str = 'AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M') -> dict[str:list]:
    KEY = "ADFGVX"
    if not len(chars_grid) == 36: return "longueur de grille incorect"
    cyphering_grid = {}
    index=0
    for i in range(1,7,1):
        for k in range(1,7,1):
            current_key = KEY[i-1] + KEY[k-1]
            current_char = chars_grid[index]
            cyphering_grid[current_key] = current_char
            index+=1
    return cyphering_grid

def build_antigramme(uncyphering_grid:dict, key:str = 'CRYPTO') -> list[str]:
    ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    iter = len(uncyphering_grid[key[0]])
    res = []
    cyphered_antigramme = ''
    splited_antigramme = ''
    for i in range(iter):
        for value in uncyphering_grid.values():
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

def decrypt_antigramme(ciphering_grid:dict, antigramme:list[str]) -> str:
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

def build_uncyphering_grid(matrice:list[list[str]], key:str):
    if not len(key) == 6: return "Clé incorrect"
    keys = [l for l in key]
    sorted_keys = sorted(keys)
    uncyphering_grid = {}
    for letter in key:
        i = sorted_keys.index(letter)
        value = matrice[i]
        uncyphering_grid[letter] = value
    return uncyphering_grid
