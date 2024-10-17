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

    def dechiffrement_vernam(mot:str, key:str):
        liste_mot = mot.split(' ')
        liste_mot = [mot.rstrip('\n') for mot in liste_mot]
        ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key_index = 0
        
        result = []
        # print(liste_mot)
        for word in liste_mot:
            # print(word)
            result_word = ""
            for letter in word:
                if key_index < len(key):
                    if letter in ALPHA:
                        deciphered_letter_index = (ALPHA.index(letter) - ALPHA.index(key[key_index])) % 26
                        # print(deciphered_letter_index)
                        # print(ALPHA[deciphered_letter_index])
                        result_word+=ALPHA[deciphered_letter_index]
                        key_index+=1
                    else:
                        result_word += letter
                else:
                    key_index=0
                    if letter in ALPHA:
                        deciphered_letter_index = (ALPHA.index(letter) - ALPHA.index(key[key_index])) % 26
                        # print(deciphered_letter_index)
                        # print(ALPHA[deciphered_letter_index])
                        result_word += ALPHA[deciphered_letter_index]
                        key_index+=1
                    else:
                        result_word += letter

            # print(result_word)
            result.append(result_word)
        result = ' '.join(result)
        # print("result:", result)
        return result
    

#==========================================================================================ADFGVX================================================================================================================================================================================
def cree_mat(message_str: str, key: str) -> list[list[str]]:
    """cree une matrice du message parfaitement divisé en
    n (longeur de la clé) colonnes, sous forme de liste de liste 

    Args:
        message_str (str): message chiffre sous forme de triple-quoted
        strings ou de str simple (sur une ou plusieurs lignes) 
        key (str): la cle de la matrice 

    Returns:
        list[list[int]]: la matrice des colonnes
    """
    mess_ligne = message_str.splitlines()
    message_coupe = ""
    premier_ligne = True
    matrice_final = []
    index = 0

    for ligne in mess_ligne:
        if ligne != "":
            if premier_ligne:
                message_coupe += ligne
            else:
                message_coupe += " " + ligne
            premier_ligne = False

    for i in range(1, len(key) + 1):
        vrai_message = int(len(message_coupe) / 6) * i
        partie_message = message_coupe[index:vrai_message]
        matrice_final.append(list(partie_message))
        index = vrai_message
    return matrice_final

def make_ciphering_grid(chars_grid:str = 'AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M'):
    KEY = "ADFGVX"
    if not len(chars_grid) == 36: return "longueur de grille incorect"
    grid = {}
    index=0
    for i in range(1,7,1):
        for k in range(1,7,1):
            current_key = KEY[i-1] + KEY[k-1]
            current_char = chars_grid[index]
            grid[current_key] = current_char
            index+=1
    return grid

def make_antigramme(unciphering_grid:dict):
    res = []
    iter = len(unciphering_grid['C'])
    print(iter)
    for i in range(47):
        tmp_char = ""
        for key,value in unciphering_grid.items():
            tmp_char += value[i]
        if tmp_char == '':
            res.append(' ')
        else:
            res.append(tmp_char)
    print(res)
    res = "".join(res)
    res = wrap(res, 2)
    print(res)
    print(len(res))
    return res

def decrypt_antigramme(ciphering_grid:dict, antigramme:list[str]):
    res = ""
    tmp = []
    for combinaison in antigramme:
        exec = True
        for l in combinaison: 
            if l not in 'ADFGVX':
                exec = False
        if exec:
            tmp.append(ciphering_grid[combinaison])
        else:
            tmp.append(combinaison)
    print(tmp)
    res = res.join(tmp)
    return res


def construction_grille_dechiffrement(matrice:list[list[str]], key:str):
    if not len(key) == 6: return "Clé incorrect"
    key = [l for l in key]
    sorted_key = sorted(key)
    unciphering_grid = {}
    for letter in key:
        i = sorted_key.index(letter)
        value = matrice[i]
        unciphering_grid[letter] =  value
    return unciphering_grid
            
    # def dechiffrement_message_ADFGVX(self, chars_grind:str, public_key:str='CRYPTO'):
    #     message = Substition.group_de_six()

    #     #TODO fonction dechiffrment ADFGX en utilisant les petites fonction au dessus
    #     ...
    
if __name__ == "__main__":
    chars_grid = "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M"
    test = Substition('message3_chiffre.txt')
    mat = cree_mat(test.fichier, 'CRYPTO')
    for each in mat:
        print(each, len(each))
    dec_grid = construction_grille_dechiffrement(mat, 'CRYPTO')
    # for key,val in dec_grid.items():
    #     print(key,val)
    antigramme = make_antigramme(dec_grid)
    # antigramme = ['AF', 'GG', 'VX', 'FX', 'VA', 'FX', 'XA', 'AA', 'XA', 'FX', 'GF', 'DD', 'FD', 'XX', 'VF', 'GF', 'DG', 'FD']
    # print(dec_grid)
    # print(f"antigramme: {antigramme}")
    cypher_grid = make_ciphering_grid()
    clear_msg = decrypt_antigramme(cypher_grid,antigramme)
    print(f"decrypted: {clear_msg}")
    # print(f"GG: {cypher_grid['GG']}")
    # for key,val in cypher_grid.items():
    #     print(key,val)
