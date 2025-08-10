import cv2
from PIL import Image
metodos = [
    cv2.THRESH_BINARY,
    cv2.THRESH_TOZERO,
    cv2.THRESH_TRUNC,
    cv2.THRESH_TOZERO_INV,
    cv2.THRESH_BINARY_INV
]

imagem = cv2.imread("imgs_para_tratamento/captcha_04.png")

#Transformar a imagem em escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)

i = 0
for metodo in metodos:
    i +=1
    _,imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, metodo | cv2.THRESH_OTSU)
    cv2.imwrite(f'testesmetodo/imagem_tratada_{i}.png', imagem_tratada)

imagem = Image.open("testesmetodo/imagem_tratada_3.png")
imagem = imagem.convert("L")
imagem2 = Image.new("L", imagem.size, 255)

for y in range(imagem.size[1]):
    for x in range(imagem.size[0]):
        cor_do_pixel = imagem.getpixel((x,y))
        if cor_do_pixel < 115:
            imagem2.putpixel((x,y),0)
imagem2.save('testesmetodo/imagemfinal.png')