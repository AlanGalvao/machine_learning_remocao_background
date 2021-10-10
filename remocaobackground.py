import cv2
import numpy as np

#   função para evitar erros
def nothing(x):
    pass


#   execução da camera
cap = cv2.VideoCapture(0)

#   Criação de janela
cv2.namedWindow('trackbars')

#Criando trackbars
cv2.createTrackbar('l-h', 'trackbars', 0, 179, nothing)
cv2.createTrackbar('l-s', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('l-v', 'trackbars', 0, 255, nothing)
cv2.createTrackbar('u-h', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('u-s', 'trackbars', 255, 255, nothing)
cv2.createTrackbar('u-v', 'trackbars', 255, 255, nothing)

#   laço
while True:
    #   leitura do frame
    ret, frame = cap.read()

    #   pega os valores das trackbars
    l_h = cv2.getTrackbarPos('l-h', 'trackbars')
    l_s = cv2.getTrackbarPos('l-s', 'trackbars')
    l_v = cv2.getTrackbarPos('l-v', 'trackbars')
    u_h = cv2.getTrackbarPos('u-h', 'trackbars')
    u_s = cv2.getTrackbarPos('u-s', 'trackbars')
    u_v = cv2.getTrackbarPos('u-v', 'trackbars')

    #   Array numpy lower upper
    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    #   Criando HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #   Criando máscara
    mask = cv2.inRange(hsv, lower, upper)

    # Encontrar os contornos
    contornos, hierarquia = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contornos, -1, (0, 150, 150), 3)
    cv2.imshow('contornos', frame)

    '''
    #   Criar resultado
    resultado = cv2.bitwise_and(frame, frame, mask=mask)
    #   Exibindo resultado
    cv2.imshow('resultado', resultado)
    '''

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

#   finalização
cap.release()
cv2.destroyAllWindows()
