from scapy import all as scapy
import constantes as const
import SAE_IMAGE_API as IAPI

def open(file:str = "../gr_17/trace_1.pcap"):
    try:
        return scapy.rdpcap(file)
    except Exception as e:
        return e
    
file  = open()
file.stats
# print(file)
print(file[74].show())
# udpPacket = [pac for pac in file if pac.haslayer(scapy.UDP)]
# for pac in udpPacket:
#     print(pac.show())

# def traslate_string_binary(text: str):
#     return ''.join(format(ord(char), '08b') for char in text)

# def traslate_binary_string(binary: str):
#     return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

# def traslate_binary_hex(binary: str):
#     return ''.join(hex(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

# def match_key_length_with_data(key: str, data: str):
#     key_length = len(key)
#     data_length = len(data)
#     if key_length < data_length:
#         key = (key * (data_length // key_length)) + key[:data_length % key_length]
#     else:
#         key = key[:data_length]
    
#     return key



# def xor_strings(s, t):
#     print(len(s))
#     print(len(t))

#     print(s)
#     print(t)
#     return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s,t))

# def xor_strings(s: str, t: str) -> str:
#     # Assurez-vous que les deux chaînes sont de même longueur
#     if len(s) != len(t):
#         raise ValueError("Les chaînes doivent être de même longueur")

#     # Effectuer le XOR bit à bit
#     xor_result = ''.join('1' if a != b else '0' for a, b in zip(s, t))
    
#     return xor_result

# s = "1101"
# t = "1011"
# print(xor_strings(s, t))

# print(const.FIRST_PAQUET_DATA)
# print(const.SECOND_PAQUET_DATA)
# print(const.FIRD_PAQUET_DATA)    

# mes_bin = traslate_binary_string(const.FIRST_PAQUET_DATA)
# hex_img = traslate_binary_hex(const.FIRST_PAQUET_DATA)
# print(hex_img)
# others =  hex_img.split("0x")
# others = ''.join(w for w in others)
# print(others)
# print("message",mes_bin)
# key = match_key_length_with_data(const.FIRST_PAQUET_DATA, mes_bin)
# print("longueur cle:", len(key))
# test = xor_strings(key, mes_bin)
# print(test)
# print(traslate_string_binary(const.SECOND_PAQUET_DATA))
# def separation_octets(bits):
#     max = len(bits)
#     res = ""
#     octet = ""
#     for x in range(0, max):
#         octet += bits[x]
#         if len(octet) == 4 :
#             res += octet
#             res += " "
#             octet = ""
#     return res
# print(separation_octets(const.FIRST_PAQUET_DATA).split(" "))

# IAPI.trouver_logo("../image/rossignol.bmp", "../image/test.bmp", separation_octets(const.FIRST_PAQUET_DATA).split(" "))