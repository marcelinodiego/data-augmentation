import os
import cv2
from skimage import io


# -------------------------------------------------------------------------------
#                       Padronização do formato das imagens.
# -------------------------------------------------------------------------------

def main():
    origem = 'ImagensOriginais/'
    destino = 'ImagensPadronizadas/'
    # criação de uma lista onde cada posição de índice indica
    # o nome de uma imagem presente no diretorio "ImagensOriginais/"
    imagens = [os.path.join(origem, f) for f in os.listdir(origem) if
               os.path.isfile(os.path.join(origem, f))]

    for i in range(len(imagens)):
        image_path = (imagens[i])

        # leitura de imagem na pasta 'ImagensOriginais'
        dado = cv2.imread(image_path)

        # Salvando imagem com formato convertido para JPG na pasta de destino 'ImagensPadronizadas'
        path = '%s/padrao_%s.jpg' % (destino, i)
        io.imsave(path, dado)


main()
