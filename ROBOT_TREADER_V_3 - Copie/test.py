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

ressouces = pd.read_csv("ressouces_V2.csv", sep=';')
z = 0
for i in list(ressouces.columns):
    while str(ressouces[i].iloc[z]) not in ['nan', 'NaN', 'NAN', 'NULL'] and z < len(ressouces) - 1:
        print(ressouces[i].iloc[z])
        z = z + 1
    z = 0