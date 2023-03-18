# UNIVERDIDADE ESTADUAL DE SANTA CRUZ
# DISCENTE: DIÊGO MARCELINO SANTOS SILVA
# MATRÍCULA: 201711752

import os
import cv2
import tensorflow as tf
from skimage import io
from skimage import img_as_ubyte


# -------------------------------------------------------------------------------
#                       Métodos de Data Augmentation.
# -------------------------------------------------------------------------------

horizontal_flip = tf.keras.layers.experimental.preprocessing.RandomFlip(
                                                        mode="horizontal")

vertical_flip = tf.keras.layers.experimental.preprocessing.RandomFlip(
                                                        mode="vertical")


translacao_altura = tf.keras.Sequential(
                                        [tf.keras.layers.experimental.preprocessing.RandomHeight(factor=(0.3, 0.4))]
                                        )

translacao_largura = tf.keras.Sequential(
                                        [tf.keras.layers.experimental.preprocessing.RandomWidth(factor=(0.3, 0.4))]
                                        )

zoom = tf.keras.layers.experimental.preprocessing.RandomZoom(
                                            height_factor=(-0.2, -0.4)
                                            )


def rotacao_horario(imagem):
    return tf.image.rot90(imagem)


def rotacao_antihorario(imagem):
    return tf.image.rot90(imagem, k=3)


def brilho(imagem):
    return tf.image.random_brightness(
              imagem, 0.5
            )


# -------------------------------------------------------------------------------
#                           FUNÇÃO PRINCIPAL.
# -------------------------------------------------------------------------------


def main():
    diretorio = 'ImagensPadronizadas/'
    aumento = 'aumento_dados/'

    # contador auxiliar para salvar dados aumentados
    num_files = 0

    # variavel para salvar as imagens originais na mesma pasta onde foi salvo o aumento de dados.
    original = []

    # variaveis para salvar as imagens resultantes de cada método
    result_image1 = []
    result_image2 = []
    result_image3 = []
    result_image4 = []
    result_image5 = []
    result_image6 = []
    result_image7 = []
    result_image8 = []

    # criação de uma lista onde cada posição de índice indica o nome de uma imagem presente no diretorio "imagens/"
    images = [os.path.join(diretorio, f) for f in os.listdir(diretorio) if
              os.path.isfile(os.path.join(diretorio, f))]

    for num_files in range(len(images)):
        image_path = (images[num_files])

        # leitura de imagem na pasta de origem 'Imagens'
        original = cv2.imread(image_path)

        # Salvando imagem original na pasta de destino 'aumento_dados'
        path0 = '%s/original_%s.jpg' % (aumento, num_files)
        io.imsave(path0, original)

        # -------------------------------------------------------------------------------
        #                           Chamadas dos Métodos.
        # --------------------------------------------------------------------------------
        result_image8 = brilho(original)

        original = tf.expand_dims(original, 0)

        result_image1 = horizontal_flip(original)
        result_image2 = vertical_flip(original)

        result_image3 = rotacao_horario(original)
        result_image4 = rotacao_antihorario(original)

        result_image5 = translacao_altura(original)
        result_image6 = translacao_largura(original)
        result_image7 = zoom(original)

        # criação de nome para cada nova imagem salva na pasta de destino.
        path1 = '%s/aumento1_%s.jpg' % (aumento, num_files)
        path2 = '%s/aumento2_%s.jpg' % (aumento, num_files)
        path3 = '%s/aumento3_%s.jpg' % (aumento, num_files)
        path4 = '%s/aumento4_%s.jpg' % (aumento, num_files)
        path5 = '%s/aumento5_%s.jpg' % (aumento, num_files)
        path6 = '%s/aumento6_%s.jpg' % (aumento, num_files)
        path7 = '%s/aumento7_%s.jpg' % (aumento, num_files)
        path8 = '%s/aumento8_%s.jpg' % (aumento, num_files)

        # salvando imagens geradas por cada método na pasta de destino 'aumento_dados'
        io.imsave(path1, img_as_ubyte(result_image1[0]))
        io.imsave(path2, img_as_ubyte(result_image2[0]))
        io.imsave(path3, img_as_ubyte(result_image3[0]))
        io.imsave(path4, img_as_ubyte(result_image4[0]))
        io.imsave(path5, result_image5[0])
        io.imsave(path6, result_image6[0])
        io.imsave(path7, img_as_ubyte(result_image7[0]))
        io.imsave(path8, result_image8, check_contrast=False)
        original = None
        result_image1 = None
        result_image2 = None
        result_image3 = None
        result_image4 = None
        result_image5 = None
        result_image6 = None
        result_image7 = None
        result_image8 = None


main()
