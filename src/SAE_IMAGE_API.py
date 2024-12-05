from PIL import Image

def read_pixel(picture_path:str):
    i = Image.open(picture_path)
    for y in range(i.size[1]):
        for x in range(i.size[0]):
            c = i.getpixel((x,y))
            print(c)
        print(" ")

        
def write_image_by_image(picture_path1:str, out_name:str):
    i = Image.open(picture_path1)
    sortie = i.copy()
    sortie.save(out_name)

def modify_pixel(image_path:str, pixel:tuple, color:tuple, out_name:str):
    i = Image.open(image_path)
    sortie  = i.copy()
    sortie.putpixel(pixel, color)
    sortie.save(out_name)

def copy_image(image1_path:str, out_name:str, with_palette:bool):
    i = Image.open(image1_path)
    sortie = Image.new(i.mode, i.size)
    if with_palette:
        sortie.putpalette(i.getpalette())
    sortie.putdata(i.getdata())
    sortie.save(out_name)

""" Serie de test """
#./Image_creation/Image0.bmp
#./Image_creation/Image2.bmp
#./Image_creation/Image3.bmp
    
#picture_name_path = "./Image_creation/Image3.bmp"
#pixel = (0,0)
#color = (255,255,255)
#out_name= "ImageOut.bmp"

#read_pixel(picture_name_path)

""" Programme principal """
#B.1 Creation d'un programme qui transpose les image :
def image_transpose(image_path:str, out_name:str):
    image =  Image.open(image_path)
    image_out = Image.new(image.mode, image.size)
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            image_out.putpixel((y,x), image.getpixel((x,y)))
    image_out.save(out_name)

#image_transpose("./Image_creation/Imagetest.bmp","Imageout0.bmp")

#B.2 Inversion mirroir d'image
def inversion_mirroir(image_path:str, out_name:str):
    image =  Image.open(image_path)
    image_out = Image.new(image.mode, image.size)
    #parcourir tous les pixel
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            #remplacer tous les pixel
            image_out.putpixel((image.size[0]-1-x,y), image.getpixel((x,y)))
    image_out.save(out_name)

#inversion_mirroir("./py_script/hall-mod_0.bmp","Imageout1.bmp")
    
#B.3 Passage au niveau de gris

def grey_color(image:object,x:int,y:int) -> tuple:
    color = image.getpixel((x,y))
    # formule : Gris=(R+V+B)/3
    grey = (color[0]+color[1]+color[2])//3
    return grey,grey,grey

def passage_niv_gris(image_path:str, out_name:str):
    image = Image.open(image_path)
    image_out = Image.new(image.mode, image.siz)
    #parcour des pixels
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            #remplacement des pixel avec leur couleur en nuance de gris
            image_out.putpixel((x,y), grey_color(image,x,y))
    image_out.save(out_name)

#passage_niv_gris("./py_script/IUT-Orleans.bmp","Imageout2.bmp")

#B.4 Passage Noir et Blanc
def euclide_test(color:tuple) -> bool: #renvoie un bouléen si la couleur passe le test euclide
    return  color[0]**2 + color[1]**2 + color[2]**2 > 255**2 * 3/2

def change_color(image:object,x:int,y:int) -> tuple:
    color = image.getpixel((x,y))
    if euclide_test(color): return 255,255,255 #renvoie la couleur blanche si la couleur à passsé le test euclide
    else: return 0,0,0 #Noir sinon

def passage_noir_blanc(image_path:str, out_name:str):
    image = Image.open(image_path)
    image_out = Image.new(image.mode, image.size)
    #parcour de chaque pixel de l'image d'origine
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            #ajout des pixel de couleur noir et blanc dans la nouvelle image
            image_out.putpixel((x,y), change_color(image,x,y))
    image_out.save(out_name)

#passage_noir_blanc("./py_script/IUT-Orleans.bmp","Imageout4.bmp")  
    
#B.5 Cacher logo noir et blanc dans une image:
#Steganographie

def cacher(i,b):
    return i-(i%2)+b

def trouver(i, modulo=2):
    return i%modulo

def cacher_logo_image(image_path:str, out_name:str, logo_path:str):
    original_image = Image.open(image_path)
    logo_image = Image.open(logo_path)
    # on peut mettre .convert("L") pour une conversion en noir et blanc
    image_out = Image.new(original_image.mode, original_image.size)
    logo_image = logo_image.resize(original_image.size)
    #parcours des pixel 
    for x in range(original_image.size[0]):
        for y in range(original_image.size[1]):
            #modification de la couleur rouge en fonction des pixels du logo
            couleur_modifie = (cacher(original_image.getpixel((x,y))[0], (logo_image.getpixel((x,y))[0])%2), *original_image.getpixel((x,y))[1:])
            image_out.putpixel((x,y), couleur_modifie)
    image_out.save(out_name)

def binary_to_int(bin:str) -> int:
    return int(bin,2)

def trouver_logo(image_path: str, out_name: str, modulo=2):
    original_image = Image.open(image_path)
    image_out = Image.new(original_image.mode, original_image.size)
    # parcours des pixels
    for x in range(original_image.size[0]):
        for y in range(original_image.size[1]):
            # attribution des pixel, 0,0,0 noir si la valeur de la couleur rouge est impaire 255,255,255 sinon
            # print(original_image.getpixel((x,y)))
            image_out.putpixel((x,y), 128*trouver(original_image.getpixel((x,y)), modulo))
    image_out.save(out_name)

def trouver_cle(original_image_path:str, steg_image_path:str, out_name:str):
    original_image = Image.open(original_image_path)
    steg_image = Image.open(steg_image_path)
    image_out = Image.new(original_image.mode, original_image.size)
    for x in range(original_image.size[0]):
        for y in range(original_image.size[1]):
            original_img_pixel = original_image.getpixel((x,y))
            print(original_img_pixel, 'original')
            steg_img_pixel = steg_image.getpixel((x,y))
            print(steg_img_pixel, 'steg')
            if original_img_pixel != steg_img_pixel:
                print('true')
                image_out.putpixel((x,y), 255)
            else:
                # print('false')
                image_out.putpixel((x,y), 0)
    image_out.save(out_name)

# def trouver_logo(image_path: str, out_name: str, modulo=2):
#     original_image = Image.open(image_path).convert("RGB")
#     image_out = Image.new(original_image.mode, original_image.size)
#     # parcours des pixels
#     for x in range(original_image.size[0]):
#         for y in range(original_image.size[1]):
#             # attribution des pixel, 0,0,0 noir si la valeur de la couleur rouge est impaire 255,255,255 sinon
#             image_out.putpixel((x,y), tuple([255*trouver(original_image.getpixel((x,y))[0], modulo)]*3))
#     image_out.save(out_name)

# def trouver_logo(image_path:str, out_name:str):
#     original_image = Image.open(image_path)
#     image_out = Image.new(original_image.mode, original_image.size)
#     #parcours des pixels
#     for x in range(original_image.size[0]):
#         for y in range(original_image.size[1]):
#             #attribution des pixel, 0,0,0 noir si la valeur de la couleur rouge est impaire 255,255,255 sinon
#             image_out.putpixel((x,y), tuple([255*trouver(original_image.getpixel((x,y))[0])]*3))
#     image_out.save(out_name)

# cacher_logo_image("hall-mod_0.bmp", "Imageout_steg_0.bmp", "Imageout3.bmp")
# trouver_logo("Imageout_steg_0.bmp", "LogoExtracted.bmp")
