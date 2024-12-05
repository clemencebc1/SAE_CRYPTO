import src.constantes as const
def load_image_to_binary_str(path: str) -> str:
    try:
        img = open(path, "rb")
        return ''.join(format(byte, '08b') for byte in img.read())
    except Exception as e:
        return str(e)

def xor_strings(s: str, t: str) -> str:
    # if len(s) != len(t):
    #     raise ValueError("Les chaînes doivent être de même longueur")

    if len(s) > len(t):
        s = s[:len(t)]
    else:
        t = t[:len(s)]
    xor_result = ''.join('1' if a != b else '0' for a, b in zip(s, t))

    return xor_result


def convert_str_to_bin(text: str) -> str:
    return ''.join(format(ord(char), '08b') for char in text)

def convert_bin_to_str(binary: str) -> str:
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
    
key_bin = load_image_to_binary_str("/home/kyotaka/documents/BUT2/SAE/SAE_CRYPTO/key_difference.bmp")
vecteur = load_image_to_binary_str("output_image.png")
print(vecteur)
print(len(vecteur))
c1 = xor_strings(key_bin, vecteur)
# c1 = vecteur
# print(c1)
# print(len(c1))

m1 = convert_str_to_bin(const.FOURTH_PAQUET_DATA)
print(const.FOURTH_PAQUET_DATA)
# print(m1)
# m1_c1 = xor_strings(m1, c1)
# print(m1_c1)
# md1 = convert_bin_to_str(m1_c1)
# print(md1)
