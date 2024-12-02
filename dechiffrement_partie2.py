
from scapy.all import *

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
    for packet in packets:
        if (UDP or TCP) in packet:
            print(packet)
            

    
    
    
packets = open_trace("gr_17/trace_1.pcap")
get_udp(packets)


def separation_octets(bits):
    """ sépare les bits en octets

    Args:
        bits (str): une chaine contenant des bits

    Returns:
        str: la chaine avec un espace pour séparer les octets
    """    
    max = len(bits)
    res = ""
    octet = ""
    for x in range(0, max):
        octet += bits[x]
        if len(octet) == 4 :
            res += octet
            res += " "
            octet = ""
    return res