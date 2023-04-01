import cv2 as cv
import numpy as np
from math import *

import time
import win32api, win32con


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def moove(actu_x,actu_y,new_x,new_y):
    if(actu_x > new_x and actu_y == new_y):   #guauche
        click(318,495)
    elif (actu_x < new_x and actu_y == new_y): #droit
        click(1588,503)
    elif (actu_y < new_y and actu_x == new_x): #bas
        click(1072,920)
    elif(actu_y > new_y and actu_x == new_x): #haut
        click(820,32)



def find_ressource():
    liste = []
    img_rgb = cv.imread('map_screen.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('demi_blanc_pied_mandragore.png', 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    threshold = 0.76
    loc = np.where(res >= threshold)
    print(loc)

    for pt in zip(*loc[::-1]):
        print(pt)
        x = [0, 0]
        x[0] = round(pt[0] + w / 2)
        x[1] = round(pt[1] + h / 2)
        liste.append(x)

    return liste
