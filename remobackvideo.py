import cv2
import numpy as np

cap = cv2.VideoCapture('video2.mp4')

# Criar um subtrator
subtrator = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50, detectShadows=True)

while True:
    # frame do video para uma variavel frame
    _, frame = cap.read()

    # blur no frame
    blur = cv2.GaussianBlur(frame, (5, 5), 0)

    #   criando mascara
    mask = subtrator.apply(blur)

    # removendo sombras
    ret, mask = cv2.threshold(mask, 220, 255, cv2.THRESH_BINARY)

    #   Criando Kernel
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

    # encontrando os contornos
    contornos, hierarquia = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # FOR nos contornos
    for cnt in contornos:
        # seta area do contorno em uma variavel
        area = cv2.contourArea(cnt)

        # verifica se a area > 200 px
        if area > 350:
            x, y, w, h = cv2.boundingRect(cnt)  # tamanho do retangulo
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # aplicar retangulo em cada veiculo

    cv2.imshow('frame', frame)
    cv2.imshow('opening', opening)

    if cv2.waitKey(10) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
