
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
    
#CONVERSIONS
def bytesarray_to_str(bytesarray):
    return ''.join(format(byte, '08b') for byte in bytesarray)

def hex_to_bytesarray(hex_str):
    return  bytearray.fromhex(hex_str)

def binary_to_bytesarray(binary_str):
    return bytearray(int(binary_str[i:i+8], 2) for i in range(0, len(binary_str), 8))

#EXTRACTION DE LA CLE ET DE L'IV
# def extract_iv_and_key(image_bytes, nb_keys=1):
#     aes_key_length = 16
#     start_index = 53
#     iv = image_bytes[start_index:start_index + 16]
#     keys = {}
#     for i in range(1, nb_keys + 1):
#         start_index += aes_key_length
#         end_index = start_index + aes_key_length
#         keys[f"key{i}"] = image_bytes[start_index:end_index]

#     return iv, keys

# def extract_iv_and_keys(bytes_1024: bytearray):
#     iv = bytes_1024[0:16]
#     aes_key_bytes_length = 16
#     start_index = 16
#     keys = {}
#     for i in range(1,len(bytes_1024)//16):
#         start_index += aes_key_bytes_length
#         end_index = start_index + aes_key_bytes_length
#         keys[f"key{i}"] = bytes_1024[start_index:end_index]
#     return iv, keys

def extract_iv_and_keys(binary_data):
    byte_data = binary_to_bytesarray(binary_data)
    iv = byte_data[:16]  # First 16 bytes
    keys = [byte_data[i:i+16] for i in range(16, len(byte_data), 16)]  # Split remaining into keys
    return iv, keys

#DECRYPTAGE
# def decrypt_aes_cbc(ciphertext, iv, key):
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
#     return decrypted_data.decode('utf-8')  

# def decrypt_aes_cbc2(message, iv, key):
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     try:
#         decrypted_data = unpad(cipher.decrypt(message), AES.block_size)
#         return decrypted_data
#     except ValueError as e:
#         print("Erreur lors du decryptage ou du padding:", e)
#         return None
    
def decrypt_aes_cbc_hazmat(ciphertext, iv, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    try:
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        return unpadded_data
    except ValueError as e:
        print(f"Erreur lors du decryptage ou du padding: {e}")
        return None

def decrypt_aes_cbc_raw(ciphertext, iv, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    return decrypted_data


####Executable
# bytes_img = load_image_to_bytes("cletest.bmp")
# iv_and_keys_bytes = binary_to_bytesarray(const.FIRST_PAQUET_DATA)
# print(f"len iv_and_keys_bytes : {len(iv_and_keys_bytes)}")
# iv, keys = extract_iv_and_keys(iv_and_keys_bytes)
# print(f"iv: 1, keys : {len(keys)}")
# print(f"iv: {iv}, keys : {keys}")
# bytes_C2 = hex_to_bytesarray(const.C2)
# # bytes_C1 = bytearray(b'\x11G\xf2\x88P\x0b\x1d\xd4v\x05\xcd\x84\xc1\xafJ\'cR\xab\x9a>\'\xdeXh\xb9\xdf\xc1\xd5\xa0D\xd9(\x08:/\xaf\xc0O<\'\xbeQ\xfdd6\xaa\xc6')
# bytes_C1 = hex_to_bytesarray(const.C1)
# # bytes_C2 = bytearray(b'C\x11y\x9b$\xe1\to\xbf\xb6hz\xf8vI\xf5\xe0\x10\x84z\x10L\xac\x93\xdd\xe2\xc7\x99\\RC\xff(\x08:/\xaf\xc0O<\'\xbeQ\xfdd6\xaa\xc6')
# print(f"IV en string : {bytesarray_to_str(iv)}")
# print(f"Key1 en string : {bytesarray_to_str(keys['key1'])}")
# print(f"Key2 en string : {bytesarray_to_str(keys['key2'])}")
# print(f"Key3 en string : {bytesarray_to_str(keys['key3'])}")
# print(f"Key4 en string : {bytesarray_to_str(keys['key4'])}")
# print(f"Key5 en string : {bytesarray_to_str(keys['key5'])}")
# print(f"Key6 en string : {bytesarray_to_str(keys['key6'])}")
# print(f"Key7 en string : {bytesarray_to_str(keys['key7'])}")
# print(f"Bytes C1 : {bytes_C1}")
# print(f"Bytes C1 : {bytes_C2}")
# decrypted_data = decrypt_aes_cbc_hazmat(bytes_C2, iv, keys['key4'])

#Executable 2
# mise en place des messages
C1 = bytearray(b"\x11G\xf2\x88P\x0b\x1d\xd4v\x05\xcd\x84\xc1\xafJ\'cR\xab\x9a>\'\xdeXh\xb9\xdf\xc1\xd5\xa0D\xd9(\x08:/\xaf\xc0O<\'\xbeQ\xfdd6\xaa\xc6")
C2 = bytearray(b"C\x11y\x9b$\xe1\to\xbf\xb6hz\xf8vI\xf5\xe0\x10\x84z\x10L\xac\x93\xdd\xe2\xc7\x99\\RC\xff(\x08:/\xaf\xc0O<\'\xbeQ\xfdd6\xaa\xc6")

# extraction des clés et de l'IV
iv, keys = extract_iv_and_keys(const.FIRST_PAQUET_DATA)
print(f"Extracted IV: {iv}")
for i, key in enumerate(keys):
    print(f"Key {i+1}: {key}")

#Essai normal
for i, key in enumerate(keys):
    print(f"\nTrying Key {i+1}...")
    decrypted_c1 = decrypt_aes_cbc_hazmat(C1, iv, key)
    decrypted_c2 = decrypt_aes_cbc_hazmat(C2, iv, key)
    
    if decrypted_c1:
        print(f"Decrypted C1 with Key {i+1}: {decrypted_c1}")
    else:
        print(f"Decryption of C1 failed with Key {i+1}")
    
    if decrypted_c2:
        print(f"Decrypted C2 with Key {i+1}: {decrypted_c2}")
    else:
        print(f"Decryption of C2 failed with Key {i+1}")

# Essai sans padding
for i, key in enumerate(keys):
    print(f"\nTrying Key {i+1} without padding...")
    decrypted_c1_raw = decrypt_aes_cbc_raw(C1, iv, key)
    decrypted_c2_raw = decrypt_aes_cbc_raw(C2, iv, key)
    print(f"Decrypted C1 (raw): {decrypted_c1_raw}")
    print(f"Decrypted C2 (raw): {decrypted_c2_raw}")

def decode_or_hex(byte_data):
    """
    Tries to decode byte data as a UTF-8 string. If it fails, returns the hexadecimal representation.
    """
    try:
        return byte_data.decode("utf-8")
    except UnicodeDecodeError:
        return byte_data.hex()

# Process outputs
for i, key in enumerate(keys):
    print(f"\nKey {i+1}:")
    print(f"C1 (decoded): {decode_or_hex(decrypted_c1_raw)}")
    print(f"C2 (decoded): {decode_or_hex(decrypted_c2_raw)}")