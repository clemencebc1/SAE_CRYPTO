
from constantes import *

class Substition:

    def __init__ (self) :
        fic = open("message1_chiffre.txt", "r", encoding="utf-8")
        self.fichier = []
        for line in fic.readlines():
            line.rstrip('\n')
            self.fichier.append(line)

    def passage_pourcentage(self, dictionnaire_apparation, 
                            longueur) -> dict :
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
            
    def frequence_lettres(self) -> dict:
        """ Détermine la fréquence d'apparition d'une lettre dans le message

        Returns:
            dict: le dictionnaire d'occurence
        """        
        dico_apparition = {}
        for line in self.fichier :
            for char in line :
                # Est une lettre de l'alphabet
                if char.isalpha():
                    if char not in dico_apparition.keys():
                        dico_apparition[char] = 1
                    else :
                        dico_apparition[char] += 1
        return dico_apparition
    
    
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

                index = ALPHABET.index(char.lower()) # index de la lettre dans l'alphabet
                nv_char = ALPHABET[(index - cle) % ALPHABET_SIZE] # nouveau caractère (index - clé modulo 26) 

                res += nv_char
        return res
    

    # décryptage temporaire sans l'utilisation des fréquences
    def decryptage_naif(self):
        """ Déchiffre un message par substitution jusqu'à trouver un message cohérent (version naive)

        Returns:
            str: le message déchiffré correct
        """
        for cle in range(1, ALPHABET_SIZE):
            message = self.decrypt(cle)
            print(message)
            # appeler la fonction qui vérifie la cohérence du message
            # if correct :
            # return message
