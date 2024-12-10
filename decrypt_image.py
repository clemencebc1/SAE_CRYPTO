from PIL import Image
import numpy as np

"""
Ce script transforme le paquet de bit afin d'obtenir une image visuelle

Il prend une chaîne binaire de données (chaque bit représente un pixel de l'image).
Chaque bit est converti en une valeur binaire (0 ou 1).
L'image est générée avec les valeurs de pixel converties en intensités en noir ou en blanc.
L'image est enregistrée en tant que fichier PNG.

Finalement cet tentative est un echec car ce n'est pas la bonne piste..
"""

FIRST_PAQUET_DATA = "0010101100010010011111100101001001111011101111110001100100101101110000101001000101100011000110010110110010010010110100000110000100100111011101101100011001001101011010111000110111110111000000000000010000011101101010111101100111111100010011100101110110100011000111110000111110000101100010110110011000000111010011001111011110101111100101001111000111101011101000011011001111000000110010110000011100100011111001100000101101011111000101011000000000001111000111100101111010100001000100010001001111010011011001100101100110110110100001001101000110001110000000011101111100000100101010011101101110010100101000000011001001010000011010100100011000100101111110000000001000100000110001100110000011111011001011101011000000011111000010010101000001110000000110101110101001000000110110011001001110000100100111000111100100010011001100100110111101000010111000010010001110101011101101000110001000110000101100010110010000001010101100110111111111001100100001010011010101011110011001111000100001010011101101011111100111101101000101111001010010001000"

binary_data = FIRST_PAQUET_DATA
pixels = [int(bit) for bit in binary_data]
pixel_matrix = np.array(pixels).reshape(32, 32)
image = Image.fromarray((pixel_matrix * 255).astype('uint8'))
image.save("output_image.png")
image.show()