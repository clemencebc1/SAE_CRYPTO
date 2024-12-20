
from scapy.all import *
from PIL import Image
import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

FIRST_PAQUET_DATA = "0010101100010010011111100101001001111011101111110001100100101101110000101001000101100011000110010110110010010010110100000110000100100111011101101100011001001101011010111000110111110111000000000000010000011101101010111101100111111100010011100101110110100011000111110000111110000101100010110110011000000111010011001111011110101111100101001111000111101011101000011011001111000000110010110000011100100011111001100000101101011111000101011000000000001111000111100101111010100001000100010001001111010011011001100101100110110110100001001101000110001110000000011101111100000100101010011101101110010100101000000011001001010000011010100100011000100101111110000000001000100000110001100110000011111011001011101011000000011111000010010101000001110000000110101110101001000000110110011001001110000100100111000111100100010011001100100110111101000010111000010010001110101011101101000110001000110000101100010110010000001010101100110111111111001100100001010011010101011110011001111000100001010011101101011111100111101101000101111001010010001000"

def open_trace(fichier):
    """ ouvre une trace pcap
    Args:
    fichier (str): fichier pcap"""
    try:
        packets = rdpcap(fichier)
        return packets
    except:
        print("Erreur ouverture fichier")
    
def get_udp(packets):
    """Recupere l'ensemble donnees des packets UDP

    Args:
        packets (PacketList): liste de packets

    Returns:
        dict: dictionnaire contenant les donnees udp
    """
    dico_packets_data = dict()
    for i in range(len(packets)):
        if UDP in packets[i]:
            dico_packets_data[i] = bytes(packets[i][UDP].payload)
    return dico_packets_data

def get_tcp(packets):
    """Recupere l'ensemble donnees des packets TCP

    Args:
        packets (PacketList): liste de packets

    Returns:
        dict: dictionnaire contenant les donnees TCP
    """
    dico_packets_data = dict()
    for i in range(len(packets)):
        if TCP in packets[i]:
            dico_packets_data[i] = bytes(packets[i][TCP].payload)
    return dico_packets_data
    
def dechiffrement_cbc(mot_a_chiffrer):
    """
    Déchiffre un message en mode CBC (Cipher Block Chaining).

    Args:
        mot_a_chiffrer (str): Chemin de l'image à déchiffrer.

    Returns:
        None: Cette fonction doit encore être implémentée.
    """
    mot_a_chiffrer = Image.open(mot_a_chiffrer)
    sortie = mot_a_chiffrer.copy()
    for i in range(mot_a_chiffrer.size[1]):
        for j in range(mot_a_chiffrer.size[0]):
            pixel = mot_a_chiffrer.getpixel((j,i))
            
    pass

def chiffrement_cbc(mot_a_chiffrer, cle=None):
    """chiffrement d'un message en CBC

    Args:
        mot_a_chiffrer (str): image à chiffrer
        cle (str, optional): cle (img precedente). Defaults to None.
    """
    cpt = 0 # compteur de parcours du vecteur initialisation
    mot_a_chiffrer = Image.open(mot_a_chiffrer)
    sortie = mot_a_chiffrer.copy()
    for i in range(mot_a_chiffrer.size[1]):
        for j in range(mot_a_chiffrer.size[0]):
            if cpt >= len(cle):
                cpt = 0
            pixel = mot_a_chiffrer.getpixel((j,i))
            if pixel%2 != 0 and cle[cpt] == 1:
                sortie.putpixel((j,i), pixel+1)
            elif pixel%2 == 0 and cle[cpt] != 1:
                sortie.putpixel((j,i), pixel+1)
            else: 
                sortie.putpixel((j,i), pixel)
        cpt += 1
    sortie.save("./img/cle.bmp")

def premiere_cle():
    """
    Génère une liste de sous-clés basées sur une chaîne binaire prédéfinie.

    Returns:
        list: Liste contenant des sous-clés binaires.
    """
    binary_data = FIRST_PAQUET_DATA
    liste_cles = []
    for i in range(255, len(FIRST_PAQUET_DATA), 255):
        liste_cles.append(FIRST_PAQUET_DATA[:i])
    return liste_cles

def img_to_list(img):
    """converti une image en une liste de valuers

    Args:
        img (str): lien img
    """
    image = Image.open(img)
    liste = []
    for i in range(image.size[1]):
        for j in range(image.size[0]):
            liste.append(image.getpixel((i,j)))
    return liste


def extract_key(image1_path, image2_path, output_path):
    """
    Extrait une clé basée sur les différences de pixels entre deux images.

    Args:
        image1_path (str): Chemin de la première image.
        image2_path (str): Chemin de la deuxième image.
        output_path (str): Chemin pour sauvegarder l'image contenant la clé.

    Returns:
        None: Sauvegarde une image contenant les pixels représentant la clé.
    """
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    image1_array = np.array(image1)
    image2_array = np.array(image2)

    pixel_differences = np.abs(image1_array - image2_array) # différence entre pixels

    # Isoler les pixels non nuls comme la clé (seuil de 1)
    key_pixels = (pixel_differences > 0).astype(np.uint8) * 255

    key_image = Image.fromarray(key_pixels)
    key_image.save(output_path)

def bitstring_to_bytes(s: str) -> bytes:
    """
    Convertit une chaîne binaire ('0' et '1') en un objet bytes.

    Args:
        s (str): Chaîne binaire à convertir.

    Returns:
        bytes: Chaîne convertie en objet bytes.
    """
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def decrypt_cbc(iv: bytes, key: bytes, ciphertext: bytes) -> bytes:
    """
    Déchiffre un message chiffré en mode CBC avec une clé donnée.

    Args:
        iv (bytes): Vecteur d'initialisation (16 octets).
        key (bytes): Clé de chiffrement/déchiffrement.
        ciphertext (bytes): Texte chiffré à déchiffrer.

    Returns:
        bytes: Texte clair après déchiffrement.
    """
    if len(iv) != 16:
        raise ValueError("L'IV doit avoir une longueur de 16 octets (128 bits).")
    if len(ciphertext) % 16 != 0:
        raise ValueError("La longueur du message chiffré doit être un multiple de 16 octets.")
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext

if __name__ == "__main__":
    keys_str = "0100000000110010100010000001000000111000010011001001111000101110111110010011000101100011111011100110001000110010000111011010101110110100101000001111011100011000100111011010010000010001111111011000110110001011000110111011101111110110001000111011110111010111011000101001011101011011110001010011011011000100101011001000110001000111011001110010110101110011111100110100110100111100101000101101111011111100110000000101011000011100100010101110100110001111011000110011000100110000111110010100011011110001100011000100111011001011001100011011100001001000100010001100100001111100100100111000100110100100110011110110101100100010110100100101011011011101110001100101101000010001101101110111110100100011101111010000110110000101001100100110000110001010100111101011010001010101011111100110010110111011111101110000110100111111100111011110010111000101100001001111110010001110010110001000100100111100011110111000100010111000011000101011000111000110110010110100110100000010001001101000010001000011001100000101001110111000000111000110110101100110"
    key = keys_str[:256]
    key_bytes = bitstring_to_bytes(key)  # Conversion correcte ici

    # Premier message
    message1 = bytes.fromhex("4311799b24e1096fbfb6687af87649f5e010847a104cac93dde2c7995c5243ff28083a2fafc04f3c27be51fd6436aac6")
    IV1 = message1[:16]
    texte1 = message1[16:]
    
    print("Premier message déchiffré :")
    print(decrypt_cbc(IV1, key_bytes, texte1))
    
    # Second message
    message2 = bytes.fromhex("1147f288500b1dd47605cd84c1af4a276352ab9a3e27de5868b9dfc1d5a044d928083a2fafc04f3c27be51fd6436aac6")
    IV2 = message2[:16]
    texte2 = message2[16:]
    
    print("\nSecond message déchiffré :")
    print(decrypt_cbc(IV2, key_bytes, texte2))

    message3 = ""
    
    message6 = bytes.fromhex("fc4663b06a2a3d09a6d26e252315718386c7292d28ff65379c37390cc680e849317bed2e283ca28a5e156f186cb43064")
    message7 = bytes.fromhex("7a64e11019cbe07c83dbd7c7115c4dc4ab1f3d983db3e14031dea8451ef01ffb317bed2e283ca28a5e156f186cb43064")

    keys_str_2 = "0010101100010010011111100101001001111011101111110001100100101101110000101001000101100011000110010110110010010010110100000110000100100111011101101100011001001101011010111000110111110111000000000000010000011101101010111101100111111100010011100101110110100011000111110000111110000101100010110110011000000111010011001111011110101111100101001111000111101011101000011011001111000000110010110000011100100011111001100000101101011111000101011000000000001111000111100101111010100001000100010001001111010011011001100101100110110110100001001101000110001110000000011101111100000100101010011101101110010100101000000011001001010000011010100100011000100101111110000000001000100000110001100110000011111011001011101011000000011111000010010101000001110000000110101110101001000000110110011001001110000100100111000111100100010011001100100110111101000010111000010010001110101011101101000110001000110000101100010110010000001010101100110111111111001100100001010011010101011110011001111000100001010011101101011111100111101101000101111001010010001000"
    key2 = keys_str_2[:256]
    keys_bytes_2 = bitstring_to_bytes(key2)

    IV6 = message6[:16]
    texte6 = message6[16:]
    print("Troisieme message dechifre : ")
    print(decrypt_cbc(IV6, keys_bytes_2, texte6))

    IV7 = message7[:16]
    texte7 = message7[16:]
    print("Quatrieme message dechiffre : ")
    print(decrypt_cbc(IV7, keys_bytes_2, texte7))

