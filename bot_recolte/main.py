import numpy as np

import pandas as pd
import numpy as np
import keyboard
import win32gui
from math import *
import win32api, win32con
import time
import fonction.moove as moove
import fonction.screen as screen
import fonction.find_resource as find_resource

def rgbint2rgbtyup(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red,green,blue)

df = pd.read_csv("mandragore.csv", sep=';')

#print(df)
time.sleep(2)
while True:
    for label , x in enumerate(df["x"]):

        #====================================================================
        #============= ON PREND LA MAP EN SCREEN
        #====================================================================

        print("prend screen")
        screen.takescreen()
        #====================================================================
        #============= ON CHERCHER LES RESSOURCES SUR LA MAP
        liste = find_resource.find_ressource()
        print("clic sur les ressources")
        print("nombre de ressouces",range(len(liste)))
        #====================================================================
        #============= ON RECOLTE LES RESSOURCES
        #====================================================================

        for x in range(len(liste)):
            if ( x == 0):
                moove.click(liste[x][0],liste[x][1])
                time.sleep(7)
            elif (( sqrt((liste[x][0]) - liste[x-1][0]))**2 > 10 or ( sqrt((liste[x][1]) - liste[x-1][1]))**2 > 10):
                moove.click(liste[x][0], liste[x][1])
                time.sleep(7)
        #====================================================================
        #============= ON CHANGE DE MAP
        #====================================================================

        print("change de map")
        if (label != len(df["x"]) - 1):
            moove.moove(df["x"].iloc[label], df["y"].iloc[label], df["x"].iloc[label + 1], df["y"].iloc[label + 1])
        else:
            moove.moove(df["x"].iloc[label], df["y"].iloc[label], df["x"].iloc[0], df["y"].iloc[0])

        #====================================================================
        #============= ON REGARD SI L'ON A BIEN DE CHANGE DE MAP
        #====================================================================

        time.sleep(1)

        print(df["x"].iloc[label],df["y"].iloc[label])