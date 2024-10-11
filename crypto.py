def cesar_chiffre(phrase: str, cle: int) -> str:
    """
    Chiffre une phrase en utilisant le chiffrement César.
    
    :param phrase: La phrase à chiffrer.
    :param cle: La clé du chiffrement (un entier qui représente le décalage).
    :return: La phrase chiffrée.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    phrase = phrase.lower()  # Pour s'assurer que tout soit en minuscule
    phrase_chiffree = ''

    for caractere in phrase:
        if caractere in alphabet:
            index_initial = alphabet.index(caractere)
            nouvel_index = (index_initial + cle) % len(alphabet)
            phrase_chiffree += alphabet[nouvel_index]
        else:
            # Conserve les espaces et autres caractères non alphabétiques
            phrase_chiffree += caractere

    return phrase_chiffree

phrase = "Bonjour TOUT le monde, ça va bien ?"
cle = 1
phrase_chiffree = cesar_chiffre(phrase, cle)
print(phrase_chiffree)  
