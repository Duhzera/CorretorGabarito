import cv2
import numpy as np





# Carregue a imagem
img = cv2.imread(r'C:\Users\madu_\Documents\ProjetoGabarito\img\GabaritoBase.png')

# Converta a imagem para tons de cinza
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplique a adaptação de limiar
imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)

# Aplique a dilatação para melhorar as características
kernel = np.ones((2, 2), np.uint8)
imgDil = cv2.dilate(imgTh, kernel)

# Encontre os contornos na imagem dilatada
contours, _ = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# Encontre o maior contorno com base na área
maiorCtn = max(contours, key=cv2.contourArea)

# Obtenha as coordenadas da caixa delimitadora do maior contorno
x, y, w, h = cv2.boundingRect(maiorCtn)

# Recorte a região de interesse (ROI)
recorte = img[y:y + h, x:x + w]

# Redimensione o recorte para exibição
recorte = cv2.resize(recorte, (400, 500))


cv2.rectangle(img,(10,130),(250,100), (0,255,0),3 )

# Exiba a imagem dilatada
cv2.imshow('video', img)





# Aguarde até que uma tecla seja pressionada e, em seguida, feche a janela
cv2.waitKey(0)
cv2.destroyAllWindows()
