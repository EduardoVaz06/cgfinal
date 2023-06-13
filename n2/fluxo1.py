import cv2
import numpy as np
import matplotlib.pyplot as plt

pathfluxo2 = r'C:\Users\eduar\Pictures\yodaluz.jpg'
imgfluxo2 = cv2.imread(pathfluxo2)

hist = cv2.calcHist([imgfluxo2], [0], None, [256], [0, 256])
hist_norm = hist / (imgfluxo2.shape[0] * imgfluxo2.shape[1])
cdf = hist_norm.cumsum()

mapeamento = (cdf * 256).astype("uint8")

imagem_equalizada = cv2.LUT(imgfluxo2, mapeamento)

cv2.imshow("Original", imgfluxo2)
cv2.imshow("Equalizado", imagem_equalizada)


gray_image1 = cv2.cvtColor(imgfluxo2, cv2.COLOR_BGR2GRAY)

dst = cv2.calcHist(gray_image1, [0], None, [256], [0, 256])

plt.hist(gray_image1.ravel(), 256, [0, 256])
plt.title('Histograma Yoda com muita luz')
plt.show()

gray_image2 = cv2.cvtColor(imagem_equalizada, cv2.COLOR_BGR2GRAY)
cv2.imshow("Cinza", gray_image2)

dst2 = cv2.calcHist(imagem_equalizada, [0], None, [256], [0, 256])

plt.hist(imagem_equalizada.ravel(), 256, [0, 256])
plt.title('Histogram Yoda equalizado')
plt.show()

cv2.waitKey()