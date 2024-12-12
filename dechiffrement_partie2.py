
from scapy.all import *
import bitarray
from PIL import Image
import numpy as np
import binascii
import io

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
    # si impair alors bit cle a 1
    # si pair alors bit cle a 0
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
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    image1_array = np.array(image1)
    image2_array = np.array(image2)

    pixel_differences = np.abs(image1_array - image2_array) # différence entre pixels

    # Isoler les pixels non nuls comme la clé (seuil de 1)
    key_pixels = (pixel_differences > 0).astype(np.uint8) * 255

    key_image = Image.fromarray(key_pixels)
    key_image.save(output_path)


packets = open_trace("gr_17/trace_1.pcap")

CLES = premiere_cle()