import src.constantes as const
from PIL import Image

def load_image_to_binary_str(path: str) -> str:
    try:
        img = open(path, "rb")
        return ''.join(format(byte, '08b') for byte in img.read())
    except Exception as e:
        return str(e)

def init_cipher(message: str, iv: str) -> str:
    return xor_strings(message, iv)

def dechiffrement_cbc(cipher: str, key: str) -> str:
    return xor_strings(cipher, key)

def find_all_keys_from_img(bin_img: str, ciphers: list[str]) -> list:
    keys = {}
    index = 0
    k = 1
    keys["iv"] = bin_img[index:len(ciphers[0])]
    index += len(ciphers[0])
    for cipher in ciphers:
        keys[f"key{k}"] = bin_img[index:index+len(cipher)]
        index += len(cipher)
        k+=1
    return keys

def dechiffrement(ciphered_data: str, key: str, iv: str) -> str:
    return xor_strings(xor_strings(ciphered_data, key), iv)

def xor_strings(s: str, t: str) -> str:
    # if len(s) != len(t):
    #     raise ValueError("Les chaînes doivent être de même longueur")

    if len(s) > len(t):
        t = t + t[:len(s) - len(t)]
    else:
        s = s + s[:len(t) - len(s)]
    xor_result = ''.join('1' if a != b else '0' for a, b in zip(s, t))

    return xor_result

def convert_str_to_bin(text: str) -> str:
    return ''.join(format(ord(char), '08b') for char in text)

def convert_bin_to_str(binary: str) -> str:
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    
def convert_hex_to_bin(hex_str: str) -> str:
    return ''.join(format(int(char, 16), '04b') for char in hex_str.split())

def convert_hex_to_str(hex_str: str) -> str:
    return ''.join(chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2))

def convert_bin_to_hex(bin_str: str) -> str:
    return ' '.join(hex(int(bin_str[i:i+8], 2))[2:] for i in range(0, len(bin_str), 8))

def export_bin_to_hex_list(bin_str: str) -> str:
    return ' '.join(format(int(bin_str[i:i+8], 2), '02x') for i in range(0, len(bin_str), 8))

def msg_bits_counter(msg: str) -> int:
    return len(msg) * 8

def export_bin_tobytes_list(bin_str: str) -> list:
    return [int(bin_str[i:i+8], 2) for i in range(0, len(bin_str), 8)]


## fonction de chatgpt
def hex_string_to_bytes(hex_string):
    """
    Convertit une chaîne de caractères hexadécimale (avec des espaces) en un tableau de bytes.

    :param hex_string: Une chaîne comme "11 47 f2 88 50 ..."
    :return: Un objet `bytes`
    """
    # Supprime les espaces, puis convertit en bytes
    return bytes.fromhex(hex_string.replace(" ", ""))

def hex_string_to_list(hex_string):
    """
    Convertit une chaîne de caractères hexadécimale (avec espaces) 
    en une liste d'entiers sous format hexadécimal.

    :param hex_string: Une chaîne comme "11 47 f2 88 50 ..."
    :return: Une liste d'entiers en hexadécimal (0x...)
    """
    # Supprime les espaces, convertit en bytes, puis transforme en liste
    byte_array = bytes.fromhex(hex_string.replace(" ", ""))
    return [f"0x{byte:02x}" for byte in byte_array]

def export_bytes_list_to_file(bytes_list, file_path):
    """
    Exporte une liste de bytes dans un fichier texte.

    :param bytes_list: Une liste d'entiers entre 0 et 255
    :param file_path: Le chemin du fichier de destination
    """
    # Ensure bytes_list contains integers
    bytes_list = [int(byte, 16) if isinstance(byte, str) else byte for byte in bytes_list]
    
    with open(file_path, "w") as file:
        hex_string = ' '.join(f'0x{byte:02x}' for byte in bytes_list)
        file.write(hex_string)

def load_image_to_bytes_list():
    img = Image.open("key_difference.bmp")
    return list(img.tobytes())

########################################################################################################################################################################################
# Exemple d'utilisation
# hex_string = "11 47 f2 88 50 0b 1d d4 76 05 cd 84 c1 af 4a 27 63 52 ab 9a 3e 27 de 58 68 b9 df c1 d5 a0 44 d9 28 08 3a 2f af c0 4f 3c 27 be 51 fd 64 36 aa c6"
# hex_list = hex_string_to_list(hex_string)
# print(hex_list)  # Affiche la liste sous forme de 0x...

C1 = "11 47 f2 88 50 0b 1d d4 76 05 cd 84 c1 af 4a 27 63 52 ab 9a 3e 27 de 58 68 b9 df c1 d5 a0 44 d9 28 08 3a 2f af c0 4f 3c 27 be 51 fd 64 36 aa c6"
C2 = "43 11 79 9b 24 e1 09 6f bf b6 68 7a f8 76 49 f5 e0 10 84 7a 10 4c ac 93 dd e2 c7 99 5c 52 43 ff 28 08 3a 2f af c0 4f 3c 27 be 51 fd 64 36 aa c6" 

# bin_img = load_image_to_binary_str("key_difference.bmp")
# hex_img = export_bin_to_hex_list(bin_img)
# bytes_img = hex_string_to_list(hex_img)
bytes_img = load_image_to_bytes_list()
# export_bytes_list_to_file(bytes_img, "img.txt")
# print(bytes_img)
# C1_bin = convert_hex_to_bin(C1)
# C2_bin = convert_hex_to_bin(C2)

# print("C1 bytes:" , hex_string_to_bytes(C1))
# print("longer C1 en bits:", msg_bits_counter(C1))
# print(msg_bits_counter(C1)//256)

# print("C2 bytes:" , hex_string_to_list(C2))
# print("longer C2 en bits:", msg_bits_counter(C2))
# print(msg_bits_counter(C2)//256)
# img = load_image_to_binary_str("key_difference.bmp")
# nb_octets = 32
# img_data_bin =  img[nb_octets*8:]
# keys = find_all_keys_from_img(img_data_bin, [C1_bin, C2_bin])
# print(f"keys: {keys}, number of keys: {len(keys)}")

# print("first 1000 bytes",img_data_bin[:1000])
# print("keys", find_all_keys_from_img(C1_bin, C2_bin))
# print("key length", len(find_all_keys_from_img(C1_bin, C2_bin)[0]))
# print(f"C1: {C1}, C2: {C2}, C1 en bin: {C1_bin}, C2 en bin: {C2_bin}, longueur: {len(C1_bin)}")
# print(len(C1_bin))
# print(len(C2_bin))

# c1 = dechiffrement(C2_bin, keys["key2"], keys["iv"])
# clear_text = convert_bin_to_str(c1)
# print(clear_text)


#key_difference.bmp contains the initalization vector and all keys used to encrypt/decrypt the message make a function that return allkeys and iv stored in the image
 ############################################################################################
# test1 = load_image_to_binary_str("key_difference.bmp")
# test2 = load_image_to_binary_str("rossignol.bmp")
# newimg = xor_strings(test1, test2)
# PImage = Image.frombytes("1", (32, 32), newimg)

############################################vi################################################
# iv = load_image_to_binary_str("key_difference.bmp")
# convert_bin_to_str(iv)
# print(convert_bin_to_str(iv))
# print(iv)
# bin_vi = convert_str_to_bin(vi)
# print(f"msg en str: {vi}, iv en bin brute: {vi}, longueur: {len(vi)}")
############################################IV#####################################################
# iv = const.FIRST_PAQUET_DATA
# print(f"iv en str: (pas de print), iv en bin brute: {iv}, longueur: {len(iv)}")
############################################Chiffrer1####################################################
# i1 = xor_strings(C1, iv)
# print(f"i: {i1}, longueur: {len(i1)}")
# c1 = xor_strings(i1, iv)
# print(f"c1: {c1}, longueur: {len(c1)}")
# ci = xor_strings(C1_bin, iv)
#############################################CHIFFRER2#####################################################

# i2 = xor_strings(iv, C2_bin)
# cdf = xor_strings(i2, iv)
# m = convert_bin_to_str(cdf)
# md1 = convert_bin_to_str(c1)
# print(m)

############################################e#############################################################
