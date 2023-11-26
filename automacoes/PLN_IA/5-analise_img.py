from PIL import Image, ImageEnhance, ImageFilter

# 1 - Importando a imagem e transformando-a em Gray Scale 
img = Image.open('automacoes/PLN_IA/data/dk.png')
print(img)
img.show()

# gray_img = img.convert('L')
# gray_img.show()
# 2 - Utilizando Operações em Imagem I
rotated_img = img.rotate(180)
# rotated_img.show()

transpose_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# transpose_img.show()

resize_img_small = img.resize((300, 200))
# resize_img_small.show()

resize_img_big = img.resize((1500, 1000))
# resize_img_big.show()

dim = (200, 200, 250, 300)
crop_img = img.crop(dim)
# crop_img.show()

# 3 - Utilizando Operações em Imagem II
enhancer = ImageEnhance.Brightness(img)
bright_img = enhancer.enhance(3)
# bright_img.show()

enhancer = ImageEnhance.Contrast(img)
contrast_img = enhancer.enhance(3)
# contrast_img.show()

# 4 - Utilizando Filtros
filtro_blur = img.filter(ImageFilter.SMOOTH)
filtro_blur.show()