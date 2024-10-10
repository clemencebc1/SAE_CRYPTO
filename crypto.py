
from constantes import *

class Substition:
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
            
    def frequence_lettres(self, message):
        dico_apparition = {}
        mes = message.split("\n")
        mes = mes.split(" ")
        for lettre in mes:
            if lettre not in dico_apparition.keys():
                dico_apparition[lettre] = 1
            else :
                dico_apparition[lettre] += 1
        return dico_apparition
        
