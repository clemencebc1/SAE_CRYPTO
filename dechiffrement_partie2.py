
from scapy.all import *
import bitarray

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
    
def dechiffrement_cbc():
    pass


packets = open_trace("gr_17/trace_1.pcap")




from PIL import Image
import numpy as np
FIRST_PAQUET_DATA = "0010101100010010011111100101001001111011101111110001100100101101110000101001000101100011000110010110110010010010110100000110000100100111011101101100011001001101011010111000110111110111000000000000010000011101101010111101100111111100010011100101110110100011000111110000111110000101100010110110011000000111010011001111011110101111100101001111000111101011101000011011001111000000110010110000011100100011111001100000101101011111000101011000000000001111000111100101111010100001000100010001001111010011011001100101100110110110100001001101000110001110000000011101111100000100101010011101101110010100101000000011001001010000011010100100011000100101111110000000001000100000110001100110000011111011001011101011000000011111000010010101000001110000000110101110101001000000110110011001001110000100100111000111100100010011001100100110111101000010111000010010001110101011101101000110001000110000101100010110010000001010101100110111111111001100100001010011010101011110011001111000100001010011101101011111100111101101000101111001010010001000"


binary_data = FIRST_PAQUET_DATA

pixels = [int(bit) for bit in binary_data]


pixel_matrix = np.array(pixels).reshape(32, 32)

image = Image.fromarray((pixel_matrix * 255).astype('uint8'))
# image.save("output_image.png")

"1147f288500b1dd47605cd84c1af4a276352ab9a3e27de5868b9dfc1d5a044d928083a2fafc04f3c27be51fd6436aac6"
"43 11 79 9b 24 e1 09 6f bf b6 68 7a f8 76 49 f5 e0 10 84 7a 10 4c ac 93 dd e2 c7 99 5c 52 43 ff 28 08 3a 2f af c0 4f 3c 27 be 51 fd 64 36 aa c6"

i1 = Image.open('gr_17/rossignol.bmp')


sortie = i1.copy()
for y in range(i1.size[1]):
    for x in range(i1.size[0]):
        c = i1.getpixel((x,y))
        if cacher.trouver(c[2]) == 1:
            sortie.putpixel((x,y), (255, 255, 255))
        else:
            sortie.putpixel((x,y), (0,0,0))
        sortie.save('Imageout4.bmp')