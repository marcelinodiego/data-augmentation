# UNIVERDIDADE ESTADUAL DE SANTA CRUZ
# DISCENTE: DIÊGO MARCELINO SANTOS SILVA
# MATRÍCULA: 201711752

import os
import cv2
import tensorflow as tf
from skimage import io


# ---------------------     ----------------------------------------------------------
#                       Métodos de Data Augmentation.
# -------------------------------------------------s------------------------------

translacao_altura = tf.keras.layers.experimental.preprocessing.RandomHeight(
                                                        factor=(0.3, 0.4))

translacao_largura = tf.keras.layers.experimental.preprocessing.RandomWidth(
                                                        factor=(0.3, 0.4))

zoom = tf.keras.layers.experimental.preprocessing.RandomZoom(
                                                height_factor=(-0.2, -0.4))

contraste = tf.keras.layers.experimental.preprocessing.RandomContrast(
                                                factor=(0.1, 1.5))

corte = tf.keras.layers.RandomCrop(400, 400)


def horizontal_flip(imagem):
    return tf.image.flip_left_right(imagem)


def vertical_flip(imagem):
    return tf.image.flip_up_down(imagem)

def rotacao_horario(imagem):
    return tf.image.rot90(imagem)

def rotacao_antihorario(imagem):
    return tf.image.rot90(imagem, k=3)

def RuidoGaussiano(imagem):
    ruido = tf.random.normal(tf.shape(imagem), 0, 25, tf.float32)
    return imagem + ruido

def brilho(imagem):
    return tf.image.random_brightness(
        imagem, 0.5
    )

# -------------------------------------------------------------------------------
#                           FUNÇÃO PRINCIPAL.
# -------------------------------------------------------------------------------

def main():
    origem = 'ImagensPadronizadas/'
    destino = 'aumento_dados/'

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
    result_image9 = []
    result_image10 = []
    result_image11 = []

    # criação de uma lista onde cada posição de índice indica o nome de uma imagem presente no diretorio "imagens/"
    imagens = os.listdir(origem)
    num_files = 0
    for num_files in range(len(imagens)):  # for num_files in range(len(imagens)):
        image_path = origem + (imagens[num_files])

        # leitura de imagem na pasta de origem 'Imagens'
        original = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

        # Salvando imagem original na pasta de destino 'aumento_dados'
        path0 = '%s/original_%s.png' % (destino, num_files)
        io.imsave(path0, original)
        #                           Chamadas dos Métodos.
        # --------------------------------------------------------------------------------

        result_image1 = corte(original)
        result_image2 = contraste(original)
        result_image3 = RuidoGaussiano(original)
        result_image4 = horizontal_flip(original)
        result_image5 = vertical_flip(original)
        result_image6 = brilho(original)
        result_image7 = rotacao_horario(original)
        result_image8 = rotacao_antihorario(original)
        result_image9 = translacao_altura(original)
        result_image10 = translacao_largura(original)
        result_image11 = zoom(original)

        # criação de nome para cada nova imagem salva na pasta de destino.
        path1 = '%s/aumento1_%s.png' % (destino, num_files)
        path2 = '%s/aumento2_%s.png' % (destino, num_files)
        path3 = '%s/aumento3_%s.png' % (destino, num_files)
        path4 = '%s/aumento4_%s.png' % (destino, num_files)
        path5 = '%s/aumento5_%s.png' % (destino, num_files)
        path6 = '%s/aumento6_%s.png' % (destino, num_files)
        path7 = '%s/aumento7_%s.png' % (destino, num_files)
        path8 = '%s/aumento8_%s.png' % (destino, num_files)
        path9 = '%s/aumento9_%s.png' % (destino, num_files)
        path10 = '%s/aumento10_%s.png' % (destino, num_files)
        path11 = '%s/aumento11_%s.png' % (destino, num_files)
        # salvando imagens geradas por cada método na pasta de destino 'aumento_dados'

        tf.keras.utils.save_img(path1, result_image1)
        tf.keras.utils.save_img(path2, result_image2)
        tf.keras.utils.save_img(path3, result_image3)
        tf.keras.utils.save_img(path4, result_image4)
        tf.keras.utils.save_img(path5, result_image5)
        tf.keras.utils.save_img(path6, result_image6)
        tf.keras.utils.save_img(path7, result_image7)
        tf.keras.utils.save_img(path8, result_image8)
        tf.keras.utils.save_img(path9, result_image9)
        tf.keras.utils.save_img(path10, result_image10)
        tf.keras.utils.save_img(path11, result_image11)

        original = None
        result_image1 = None
        result_image2 = None
        result_image3 = None
        result_image4 = None
        result_image5 = None
        result_image6 = None
        result_image7 = None
        result_image8 = None
        result_image9 = None
        result_image10 = None
        result_image11 = None


main()
