
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
        if UDP in packet:
            print(packet)
            

    
    
    
packets = open_trace("gr_17/trace_1.pcap")
get_udp(packets)
