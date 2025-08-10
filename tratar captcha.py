import cv2
import os
import glob
from PIL import Image


def tratar_imagens(pasta_origem, pasta_destino='AJEITADAS'):
    arquivos = glob.glob(f"{pasta_origem}/*")
    for arquivo in arquivos:
        imagem = cv2.imread(arquivo)

        # Transformar a imagem em escala de cinza
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)


        _, imagem_tratada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_TRUNC | cv2.THRESH_OTSU)
        nome_arquivo = os.path.basename(arquivo)
        cv2.imwrite(f'{pasta_destino}/{nome_arquivo}', imagem_tratada)

    arquivos = glob.glob(f"{pasta_destino}/*")
    for arquivo in arquivos:
        imagem = Image.open(arquivo)
        imagem = imagem.convert("L")
        imagem2 = Image.new("L", imagem.size, 255)

        for y in range(imagem.size[1]):
            for x in range(imagem.size[0]):
                cor_do_pixel = imagem.getpixel((x, y))
                if cor_do_pixel < 115:
                    imagem2.putpixel((x, y), 0)
        nome_arquivo = os.path.splitext(os.path.basename(arquivo))[0]
        imagem2.save(f'{pasta_destino}/{nome_arquivo}.png')

if __name__ == "__main__":
    tratar_imagens('imgs_para_tratamento')