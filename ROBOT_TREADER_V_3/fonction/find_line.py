import win32gui

import math
 #import take_screen
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\jb\AppData\Local\Programs\Tesseract-OCR\tesseract'
import os
import pyscreenshot as ImageGrab
from PIL import Image


def RGB(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red, green, blue)

def take_screen(name,x1,y1, x2,y2):
    try:
        os.remove("Screen/"+name+".png")
    except:
        print('pas de screen')

    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im.save("Screen/"+name+".png")
    im = Image.open("Screen/"+name+".png").convert('RGBA')
    im.save("Screen/"+name+".png")

def find_line(name_ressource):
    nb_ligne = 0
    x = 1181
    y = 227

    # regarder combien de ressources sont afficher
    while True:
        try:
            color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), x, y)
            color_list = RGB(color)
            y = y + 46
            nb_ligne = nb_ligne + 1
            print(color_list)
            if (math.sqrt((color_list[0] - 36) ** 2) > 100 or math.sqrt((color_list[1] - 216) ** 2) > 100 or math.sqrt((color_list[2] - 246) ** 2) > 100):
                break
        except:
            print("mort")


    x1 = 663
    y1 = 206
    x2 = 850
    y2 = 251
    liste_name = []
    for i in range(nb_ligne):
        name = 'ligne_'+str(i)
        take_screen(name, x1, y1, x2, y2)
        y1 = y1 + 46
        y2 = y2 + 46
        #print(tess.image_to_string('../screen/'+name+'.png'))
        name_test = tess.image_to_string(r"Screen/"+name+".png").replace("\n", "").replace("\r", "").rstrip().replace("’", "'").replace("‘", "").replace("é","e")

        #print("'" + name_ressource.replace("é", "e") + "'")
        #print("'"+name_test+"'")

        print("nom de la ressource sur image : " + name_test)
        print("nom de la ressource  : " + name_ressource.replace("é", "e").replace("ê", "e"))

        if name_test.lower() == name_ressource.replace("é", "e").replace("ê", "e").lower():
            #print('trouve!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

            liste_coordonner = {'x': 621, 'y': 206 +(i)*46}
            return (liste_coordonner)
