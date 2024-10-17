#!/usr/bin/python3

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
    
    def adfgvx(self, message, grille, mot_clef):
        return None
    
    def make_ciphering_grid(chars_grid: str):
        KEY = "ADFGVX"
        if not len(chars_grid) == 36: return "longueur de grille incorect"
        grid = {}
        for i in range(1,7,1):
            for k in range(1,7,1):
                current_key = KEY[i-1] + KEY[k-1]
                current_char = chars_grid[(i*k)-1]
                grid[current_key] = current_char
        return grid
    
    def construction_grille_dechiffrement(ciphered_block:list[str], key:str):
        if not len(key) == 6: return "Clé incorrect"
        sorted_key = sorted(key)
        unciphering_grid = {}
        for i in range(len(key)):
            letters = []
            for char in ciphered_block[i]:
                letters.append(char)

        return unciphering_grid
                
    # def construction_grille(self, grille, mot_clef):
    #     liste_mots = sorted(list(mot_clef.strip()))
    #     print(liste_mots)

    #     dico_grille = dict()
    #     indice_mot_clef = 0
    #     for i in range(len(grille)):
    #         if i%6==0:
    #             if i != 0:
    #                 indice_mot_clef += 1
    #             dico_grille[liste_mots[indice_mot_clef]]=[]
    #         dico_grille[liste_mots[indice_mot_clef]].append(grille[i])
    #     return dico_grille
    
    def dechiffrement_message_ADFGVX(massage:str, chars_grind:str, public_key:str='CRYPTO'):
        #TODO fonction dechiffrment ADFGX en utilisant les petites fonction au dessus
        ...
    
if __name__ == "__main__":
    ciphered = "UCVLGH YUU BEQEMF TG ORETORI RIVDXQA QLNO82OP9CK1WU0SCY3SWR74SBDUHNB5JT6O KEORBB"
    chars_grid = "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M"
    print(Substition.dechiffrement_vernam(ciphered, "CINQ"))
    print(Substition.make_ciphering_grid(chars_grid))