import cv2
import numpy as np


pathfluxo2 = r'C:\Users\eduar\Pictures\cubo.jpg'
imgfluxo2 = cv2.imread(pathfluxo2)
cv2.imshow("Cubo", imgfluxo2)

alpha = 1.1
beta = -100
img_ajuste = cv2.convertScaleAbs(imgfluxo2, alpha=alpha, beta=beta)

cv2.imshow("Ajustado", img_ajuste)

# Exemplo de aplicação do filtro de desfoque gaussiano
gaussian_blurred_image = cv2.GaussianBlur(img_ajuste, (5, 5), 0)
cv2.imshow("Gauss Blur", gaussian_blurred_image)


# Exemplo de aplicação do filtro de detecção de bordas (Canny)
edges = cv2.Canny(gaussian_blurred_image, 50, 240)
cv2.imshow("Edges", edges)

kernel = np.ones((2,2), np.uint8)
dilated_edges = cv2.dilate(edges, kernel, iterations=1)

cv2.imshow("Bordas dilatadas", dilated_edges)


cv2.waitKey()
