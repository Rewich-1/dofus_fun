import cv2
import win32api, win32con
import numpy as np
import pandas as pd
#import imutils
import os
from PIL import Image
import pyscreenshot as ImageGrab
import keyboard
import time
import pandas as pd
import datetime
import win32gui
import fonction.take_screen as take_screen
import fonction.annalyse_picture as annalyse_picture
import fonction.update_price as update_price
import fonction.moove as moove
import gestion_prix
import psycopg2


#aller chercher les donnes (csv)
#ressouces = pd.read_csv("ressouces.csv", sep=';')
ressouces = pd.read_csv("ressouces_V2.csv", sep=';')
consommables = pd.read_csv("consommables.csv", sep=';')




while True :

    #clicler sur le marcher des consomables
    moove.click(1486, 440)
    time.sleep(3)
    z = 0
    z = 0
    for i in list(ressouces.columns):
        while str(ressouces[i].iloc[z]) not in ['nan', 'NaN', 'NAN', 'NULL'] and z < len(ressouces) - 1:

            gestion_prix.gestion_prix(ressouces[i].iloc[z])
            z = z + 1
        z = 0

    # quitter le marcher
    moove.click(1205, 84)
    time.sleep(2)

    #changer de map
    moove.moove(-30, -54, -31, -54)
    time.sleep(5)
    # changer de map
    moove.moove(-31, -54, -31, -53)
    time.sleep(5)

    # rentrer dans le marcher de consommable
    moove.click(1142, 472)
    time.sleep(2)

    for label, consommable in enumerate(consommables["consommables"]):
        gestion_prix.gestion_prix(consommable)

    # quitter le marcher
    moove.click(1205, 84)
    time.sleep(2)

    # changer de map
    moove.moove(-31, -53,-31, -54)
    time.sleep(5)

    # changer de map
    moove.moove( -31, -54,-30, -54)
    time.sleep(5)

    time.sleep(10000)



#annaliser les prix