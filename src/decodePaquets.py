# from pcapfile import savefile
# testcap = open('./gr_17/trace_1.pcap', 'rb')
# capfile = savefile.load_savefile(testcap, verbose=True)
# print(capfile)

# import libpcap
# libpcap.config(LIBPCAP=None)       # system's libpcap library will be used
# libpcap.config(LIBPCAP="npcap")
# libpcap.config(LIBPCAP="wpcap")    # included wpcap library will be used
# libpcap.config(LIBPCAP="tcpdump")
from scapy import all as scapy

def open(file:str = "./gr_17/trace_1.pcap"):
    try:
        return scapy.rdpcap(file)
    except Exception as e:
        return e
    
file  = open()
file.stats
# file.getlayer(scapy.IP).show()
print(file)
# print(file.stats)
# print(file[1].show())
# fstPacket = file[1]
# ndPacket = file[2]
# rdPaquets = file[19]
# print(fstPacket.show())
# print(ndPacket.show())
# print(rdPaquets.show())
# print(file[2].layers())
udpPacket = [pac for pac in file if pac.haslayer(scapy.UDP)]
for pac in udpPacket:
    print(pac.show())

# # print(file[0])
# encoded_str = "zd\\xe1\x10\x19\\xcb\\xe0|\\x83\\xdb\\xd7\\xc7\x11\\Mī\x1f=\\x98=\\xb3\\xe1@1ިE\x1e\\xf0\x1f\\xfb1{\\xed.(<\\xa2\\x8a^\x15o\x18l\\xb40d"
# encoded_str2 = "\\xfcFc\\xb0j*=\t\\xa6\\xd2n%#\x15q\\x83\\x86\\xc7)-(\\xffe7\\x9c79\x0cƀ\\xe8I1{\\xed.(<\\xa2\\x8a^\x15o\x18l\\xb40d"
# cleaned_str = encoded_str2.replace("\\", "")
# decoded_bytes = bytes.fromhex(encoded_str2.encode('utf-8').hex())
# print(decoded_bytes)
# print(bytes.fromhex("\xe1".encode('utf-8').hex()))


# def decode_string(encoded_str):
#     # Remplacer les doubles barres obliques inverses par des simples
#     cleaned_str = encoded_str.replace("\\\\", "\\")
    
#     # Décoder les séquences hexadécimales
#     decoded_bytes = bytes.fromhex(cleaned_str.encode('utf-8').hex())
    
#     return decoded_bytes


# print(decode_string(encoded_str).decode('utf-8'))

# raw_key = r"zd\xe1\x10\x19\xcb\xe0|\x83\xdb\xd7\xc7\x11\M\u012b\x1f=\x98=\xb3\xe1@1\u06a8E\x1e\xf0\x1f\xfb1{\xed.(<\xa2\x8a^\x15o\x18l\xb40d"

# Décodage en interprétant les séquences d'échappement
# decoded_bytes = bytes(raw_key, "utf-8").decode("unicode_escape").encode("latin1")

# Afficher le résultat
# print(decoded_bytes)
# hex = "\xe1".encode('utf-8').hex()
# hex = "\xe1".encode('utf-8').hex()
# ascii_hex = hex.encode('latin1').hex()
# test = bytes.fromhex(hex)

# print("\xe1".encode('utf-8').hex())
# print(test.decode("utf-8"))
# print(test.decode("latin1"))

# print(encoded_str2.split("\\x"))
# encoded_str2 = r"\\xfcFc\\xb0j*=\t\\xa6\\xd2n%#\x15q\\x83\\x86\\xc7)-(\\xffe7\\x9c79\x0cƀ\\xe8I1{\\xed.(<\\xa2\\x8a^\x15o\x18l\\xb40"
# array = encoded_str2.split("\\")
# for i in range(1, len(array)):
#     print(array[i])
#     chr = array[i].encode('utf-8').hex()
#     bytes_value = bytes.fromhex(chr).decode('utf-8')
#     print(bytes.fromhex(bytes_value).decode())

# decoded_bytes = bytes(encoded_str2, "utf-8").decode("unicode_escape").encode("latin1")

# # Étape 2 : Décoder les octets en chaîne lisible (si possible)
# try:
#     readable_string = decoded_bytes.decode("utf-8")  # Tentative en UTF-8
# except UnicodeDecodeError:
#     readable_string = decoded_bytes.decode("latin1")  # Alternative en Latin-1

# # Afficher les résultats
# print("Bytes décodés :", decoded_bytes)
# print("Chaîne lisible :", readable_string)

# readable_ascii = "".join(chr(b) if 32 <= b <= 126 else "." for b in decoded_bytes)
# print("Parties lisibles (ASCII uniquement) :", readable_ascii)

# raw_data = r"\\xfcFc\\xb0j*=\t\\xa6\\xd2n%#\x15q\\x83\\x86\\xc7)-(\\xffe7\\x9c79\x0cƀ\\xe8I1{\\xed.(<\\xa2\\x8a^\x15o\x18l\\xb40"

# # Décoder la chaîne pour interpréter les séquences d'échappement
# decoded_bytes = bytes(raw_data, "utf-8").decode("unicode_escape").encode("latin1")

# # Convertir les données en binaire (chaîne binaire)
# binary_representation = ''.join(format(byte, '08b') for byte in decoded_bytes)

# print(binary_representation)