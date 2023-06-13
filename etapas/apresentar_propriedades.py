import cv2
import numpy as np

# Carregar a imagem
#path = r'C:\Users\eduar\Pictures\drak.png'
path = r'C:\Users\eduar\Pictures\cubo.jpg'
imagem = cv2.imread(path)


def apresentar_propriedades_imagem(imagem):
    # Obter as dimensões da imagem
    altura, largura, canais = imagem.shape
    print("Dimensões da imagem: {}x{}x{}".format(largura, altura, canais))

    # Converter a imagem para escala de cinza
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Exibir alguns valores de cinza da imagem
    valores_cinza = np.unique(imagem_gray)
    print("Valores de cinza presentes na imagem:", valores_cinza)

    # Calcular a contagem de ocorrências de cada valor de cinza
    contagem_ocorrencias = np.zeros(256, dtype=int)
    for valor in np.nditer(imagem_gray):
        contagem_ocorrencias[valor] += 1

    # Calcular a porcentagem de ocorrência para cada valor de cinza
    total_pixels = altura * largura
    porcentagens_ocorrencias = contagem_ocorrencias / total_pixels * 100

    # Imprimir as porcentagens de ocorrência para cada valor de cinza
    for valor, porcentagem in enumerate(porcentagens_ocorrencias):
        print("Porcentagem de ocorrência do valor {}: {:.2f}%".format(valor, porcentagem))

    # Exibir a imagem
    cv2.imshow('Imagem', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Chamar a função para apresentar as propriedades da imagem
apresentar_propriedades_imagem(imagem)