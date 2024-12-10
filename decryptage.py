
import constantes as const
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers.algorithms import AES
import binascii
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
# from cryptography.hazmat.primitives.padding import unpad

#CHARGEMENT DE L'IMAGE
def load_image_to_bytes(path: str) -> bytearray:
    try:
        with open(path, "rb") as img:
            return bytearray(img.read())
    except Exception as e:
        return str(e)
    
def bytesarray_to_str(bytesarray):
    return ''.join(format(byte, '08b') for byte in bytesarray)

def hex_to_bytesarray(hex_str):
    return  bytearray.fromhex(hex_str)

#EXTRACTION DE LA CLE ET DE L'IV
def extract_iv_and_key(image_bytes, nb_keys=1):
    aes_key_length = 16
    start_index = 53
    iv = image_bytes[start_index:start_index + 16]
    keys = {}
    for i in range(1, nb_keys + 1):
        start_index += aes_key_length
        end_index = start_index + aes_key_length
        keys[f"key{i}"] = image_bytes[start_index:end_index]

    return iv, keys

#DECRYPTAGE
def decrypt_aes_cbc(ciphertext, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_data.decode('utf-8')  

def decrypt_aes_cbc2(message, iv, key):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    try:
        decrypted_data = unpad(cipher.decrypt(message), AES.block_size)
        return decrypted_data
    except ValueError as e:
        print("Erreur lors du decryptage ou du padding:", e)
        return None
    
def decrypt_aes_cbc_hazmat(ciphertext, iv, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor() 
    try:
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()  
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data  
    except ValueError as e:
        print("Erreur lors du decryptage ou du padding:", e)
        return None

####Executable
bytes_img = load_image_to_bytes("key_difference.bmp")
bytes_C2 = hex_to_bytesarray(const.C2)
# bytes_C1 = bytearray(b'\x11G\xf2\x88P\x0b\x1d\xd4v\x05\xcd\x84\xc1\xafJ\'cR\xab\x9a>\'\xdeXh\xb9\xdf\xc1\xd5\xa0D\xd9(\x08:/\xaf\xc0O<\'\xbeQ\xfdd6\xaa\xc6')
bytes_C1 = hex_to_bytesarray(const.C1)
# bytes_C2 = bytearray(b'C\x11y\x9b$\xe1\to\xbf\xb6hz\xf8vI\xf5\xe0\x10\x84z\x10L\xac\x93\xdd\xe2\xc7\x99\\RC\xff(\x08:/\xaf\xc0O<\'\xbeQ\xfdd6\xaa\xc6')
iv, keys = extract_iv_and_key(bytes_img, 2)
print(f"IV : {iv}")
print(f"Keys : {keys}")
print(f"IV en string : {bytesarray_to_str(iv)}")
print(f"Key1 en string : {bytesarray_to_str(keys['key1'])}")
print(f"Key2 en string : {bytesarray_to_str(keys['key2'])}")
print(f"Bytes C1 : {bytes_C1}")
print(f"Bytes C1 : {bytes_C2}")
decrypted_data = decrypt_aes_cbc_hazmat(bytes_C2, iv, keys['key2'])



