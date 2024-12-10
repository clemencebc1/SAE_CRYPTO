from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def bitstring_to_bytes(s: str) -> bytes:
    # Convertit une chaîne de '0' et '1' en octets
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def decrypt_cbc(iv: bytes, key: bytes, ciphertext: bytes) -> bytes:
    # Vérification de la longueur de l'IV
    if len(iv) != 16:
        raise ValueError("L'IV doit avoir une longueur de 16 octets (128 bits).")
    if len(ciphertext) % 16 != 0:
        raise ValueError("La longueur du message chiffré doit être un multiple de 16 octets.")
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    return plaintext