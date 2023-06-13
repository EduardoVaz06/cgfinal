import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r'C:\Users\eduar\Pictures\cubo6.jpg'
img = cv2.imread(path)
cv2.imshow("Cubo", img)

# Exemplo de aplicação do filtro de detecção de bordas (Canny)
preedges = cv2.Canny(img, 100, 240)
cv2.imshow("Edges", preedges)


# Crie uma máscara do fundo
mask = np.zeros(img.shape[:2], dtype=np.uint8)

# Defina a região do fundo como branco na máscara
lower_bound = (251, 251, 251)
upper_bound = (255, 255, 255)
mask = cv2.inRange(img, lower_bound, upper_bound)

# Defina a nova cor do fundo (por exemplo, azul)
new_color = (0, 0, 0)  # Azul

# Crie uma imagem com a nova cor do fundo
new_background = np.full(img.shape, new_color, dtype=np.uint8)

# Combine a imagem original com o novo fundo usando a máscara
result = np.where(mask[:, :, np.newaxis], new_background, img)

# Exiba a imagem resultante
cv2.imshow("Imagem com fundo alterado", result)

gaussian_blurred_image = cv2.GaussianBlur(result, (5, 5), 0)
cv2.imshow("Gauss Blur", gaussian_blurred_image)

edges = cv2.Canny(gaussian_blurred_image, 100, 240)
cv2.imshow("Edges 240", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()

