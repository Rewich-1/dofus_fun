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
import pandas.io.sql as sqlio

#aller chercher les donnes (csv)
#ressouces = pd.read_csv("ressouces.csv", sep=';')
ressouces = pd.read_csv("ressouces_V2.csv", sep=';')
consommables = pd.read_csv("consommables.csv", sep=';')

conn = psycopg2.connect(
        host="90.3.11.174",
        database="postgres",
        user="postgres",
        password="postgres")

sql1 = "select name_game from info_table where id_ressource  not in ( select  id_ressource from info_prix_ressource where (date > now() - interval '1 day') group by id_ressource)
ORDER BY RANDOM () limit(20);"
ressouces = sqlio.read_sql_query(sql1, conn)

sql2 = "select name_game from info_table where  hotel_vente = 'consommables' ORDER BY RANDOM ();"
consommables = sqlio.read_sql_query(sql2, conn)

print(ressouces)



while True :

    #clicler sur le marcher des consomables
    moove.click(1486, 440)
    time.sleep(3)

    z = 0
    for index,row in ressouces.iterrows():
        gestion_prix.gestion_prix(row['name_game'])


    # quitter le marcher
    #moove.click(1205, 84)
    #time.sleep(2)

    #changer de map
    #moove.moove(-30, -54, -31, -54)
    #time.sleep(5)
    # changer de map
    # moove.moove(-31, -54, -31, -53)
    #time.sleep(5)

    # rentrer dans le marcher de consommable
    #moove.click(1142, 472)
    #time.sleep(2)



    #for index,row in consommables.iterrows():
    #    gestion_prix.gestion_prix(row['name_game'])

    # quitter le marcher
    #moove.click(1205, 84)
    #time.sleep(2)

    # changer de map
    #moove.moove(-31, -53,-31, -54)
    #time.sleep(5)

    # changer de map
    #moove.moove( -31, -54,-30, -54)
    #time.sleep(5)

    time.sleep(600)



#annaliser les prix