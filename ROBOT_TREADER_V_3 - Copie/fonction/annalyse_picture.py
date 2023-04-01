import cv2
import numpy as np
import pandas as pd

def annalyse_picture(name_picture):
    SCALE = 2
    THICK = 2
    WHITE = (255, 255, 255)
    digits = []
    for digit in map(str, range(10)):
        (width, height), bline = cv2.getTextSize(digit, cv2.FONT_HERSHEY_SIMPLEX,
                                                 SCALE, THICK)
        digits.append(np.zeros((height + bline, width), np.uint8))
        cv2.putText(digits[-1], digit, (0, height), cv2.FONT_HERSHEY_SIMPLEX,
                    SCALE, WHITE, THICK)
        x0, y0, w, h = cv2.boundingRect(digits[-1])
        digits[-1] = digits[-1][y0:y0+h, x0:x0+w]


    def detect(img):
        # chiffre extrait, on le compare avec notre base
        percent_white_pix = 0
        digit = -1
        for i, d in enumerate(digits):
            scaled_img = cv2.resize(img, d.shape[:2][::-1])
            # d AND (scaled_img XOR d)

            bitwise = cv2.bitwise_and(d, cv2.bitwise_xor(scaled_img, d))

            # le resultat est donné par la plus grosse perte de pixel blanc
            before = np.sum(d == 255)
            matching = 100 - (np.sum(bitwise == 255) / before * 100)
            # cv2.imshow('digit_%d' % (9-i), bitwise)
            if percent_white_pix < matching:
                percent_white_pix = matching
                digit = i
        return digit

    color_test_image = cv2.imread('screen/'+name_picture+'.png', cv2.IMREAD_COLOR)
    gray_test_image = cv2.cvtColor(color_test_image, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray_test_image,110, 200, cv2.THRESH_BINARY)


    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    liste = []

    for cnt in contours:
        # on vérifie la taille du contour pour éviter de traiter un 'défaut'

        if cv2.contourArea(cnt) > 1:
            # on récupère le rectangle encadrant le chiffre
            brect = cv2.boundingRect(cnt)
            x, y, w, h = brect
            # extraction de notre "region of interest"
            # notre roi correspond à un chiffre sur notre feuille
            roi = thresh[y:y + h, x:x + w]

            # detection
            digit = detect(roi)
            liste.append(digit)

            #cv2.rectangle(color_test_image, brect, (0, 255, 0), 1)
            #cv2.putText(color_test_image, str(digit), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (190, 123, 68), 2)

    x = 0
    for count, value in enumerate(liste):
        x += value * 10**count

    return x