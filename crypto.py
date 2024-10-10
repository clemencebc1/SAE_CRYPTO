lettre_double = ["c","f","l","m","n","p","r","s","t"]
# import fichier 

def dechiffre_mes_1(message) :
    dico_frequence = frequence_lettres(message)



# On récupère les lettres du message
# On note leur fréquence d'apparition
# On récupère la fréquence indicative des lettres concernées
# On remplace selon cette fréquence toute les lettres et on print le message obtenue dans le terminal
# On applique un algo à part qui vérifie si chaque mots obtenus sont français

# Si double lettres : regarder parmis les lettres possibles


    

class Substitution :

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
        
