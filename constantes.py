from string import ascii_lowercase
# tiré de https://fr.wikipedia.org/wiki/Fr%C3%A9quence_d%27apparition_des_lettres
import dechiffrement 

# Fréquences d'apparition des lettres tirées de Wikipedia
ALPHABET_FREQ = {
    'e': 0.121, 'a': 0.0711, 'i': 0.0659, 's': 0.0651, 'n': 0.0639,
    'r': 0.0607, 't': 0.0592, 'o': 0.0502, 'l': 0.0496, 'u': 0.0449,
    'd': 0.0367, 'c': 0.0318, 'm': 0.0262, 'p': 0.0249, 'é': 0.0194,
    'g': 0.0123, 'b': 0.0114, 'v': 0.0111, 'h': 0.0111, 'f': 0.0111,
    'q': 0.0065, 'y': 0.0046, 'x': 0.0038, 'j': 0.0034, 'è': 0.0031,
    'à': 0.0031, 'k': 0.0029, 'w': 0.0017, 'z': 0.0015, 'ê': 0.0008,
    'ç': 0.0006, 'ô': 0.0004, 'â': 0.0003, 'î': 0.0003, 'û': 0.0002,
    'ù': 0.0002, 'ï': 0.0001, 'á': 0.0001, 'ü': 0.0001, 'ë': 0.0001,
    'ö': 0.0001, 'í': 0.0001
}

# Alphabet anglais minuscule
ALPHABET = ascii_lowercase

# Liste des mots du dictionnaire français
DICO = dechiffrement.open_world_list("french")

# Taille de l'alphabet
ALPHABET_SIZE = 26