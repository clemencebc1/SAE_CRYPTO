import src.constantes as const
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

def find_all_keys_from_img(bin_img: str, bin_cipher: str) -> list:
    keys = []
    for i in range(0, len(bin_img), len(bin_cipher)):
        keys.append(xor_strings(bin_img[i:i+len(bin_cipher)], bin_cipher))
    return keys
    
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

C1 = "11 47 f2 88 50 0b 1d d4 76 05 cd 84 c1 af 4a 27 63 52 ab 9a 3e 27 de 58 68 b9 df c1 d5 a0 44 d9 28 08 3a 2f af c0 4f 3c 27 be 51 fd 64 36 aa c6"
C2 = "43 11 79 9b 24 e1 09 6f bf b6 68 7a f8 76 49 f5 e0 10 84 7a 10 4c ac 93 dd e2 c7 99 5c 52 43 ff 28 08 3a 2f af c0 4f 3c 27 be 51 fd 64 36 aa c6" 
C1_bin = convert_hex_to_bin(C1)
C2_bin = convert_hex_to_bin(C2)

print("keys", find_all_keys_from_img(C1_bin, C2_bin))
print("key length", len(find_all_keys_from_img(C1_bin, C2_bin)[0]))
# print(f"C1: {C1}, C2: {C2}, C1 en bin: {C1_bin}, C2 en bin: {C2_bin}, longueur: {len(C1_bin)}")
print(len(C1_bin))
print(len(C2_bin))

#key_difference.bmp contains the initalization vector and all keys used to encrypt/decrypt the message make a function that return allkeys and iv stored in the image
 

############################################vi################################################
iv = load_image_to_binary_str("key_difference.bmp")
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
ci = xor_strings(C1_bin, iv)
#############################################CHIFFRER2#####################################################

i2 = xor_strings(iv, C2_bin)
cdf = xor_strings(i2, iv)
m = convert_bin_to_str(cdf)
# md1 = convert_bin_to_str(c1)
print(m)
############################################e#############################################################
