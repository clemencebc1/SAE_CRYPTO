#!/usr/bin/python3

from constantes import *
from dechiffrement import *

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
    
    def dechiffrement_cesar(self, message: str=None, indice: int=1):
        """dechiffre un message

        Args:
            message (str): le message a dechiffre
            indice (int, optional): indice de decalage
            Defaults to 1.

        Returns:
            str: le message dechiffre
        """
        if message is None:
            message = self.fichier
        mess = message.rstrip("\n").lower()
        print(mess)
        dechiffrement_cesar = ""
        for carac in mess:
            code = ord(carac)
            new_carac = carac
            if code > 96:
                new_carac = chr(code+indice)
            dechiffrement_cesar += new_carac
        print(dechiffrement_cesar)
        if check_french_message(dechiffrement_cesar) or indice > 25:
            return dechiffrement_cesar
        indice += 1
        return self.dechiffrement_cesar(message, indice)

    def ascii_caractere(self, carac, indice):
        code = ord(carac)
        if code+indice>123:
            code += (122-code)