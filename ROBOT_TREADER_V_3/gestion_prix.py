import keyboard
import time
import win32gui

import fonction.take_screen as take_screen
import fonction.annalyse_picture as annalyse_picture
import fonction.update_price as update_price
import fonction.moove as moove
import fonction.color as couleur
import fonction.find_line as find_line
import math

def gestion_prix(resource):

    # écrire nom ressource
    #print(resource)
    moove.click(430, 200)
    keyboard.write("")
    keyboard.write(resource)

    time.sleep(1)
    # ==============================================
    # ===verif ouverture ressource
    # ==============================================
    while True:
        color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 870, 230)
        color_list = couleur.RGB(color)
        time.sleep(0.5)

        if (math.sqrt((color_list[0] - 78) ** 2) < 35 and math.sqrt((color_list[1] - 85) ** 2) < 35 and math.sqrt((color_list[2] - 83) ** 2) <35):
            break
    # ==============================================
    # ===on regard si il n'y a pas plusieur résultat afficher
    # ==============================================
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 1181, 272)
    color_list = couleur.RGB(color)
    time.sleep(0.5)

    if (math.sqrt((color_list[0]-36)**2)<10 and math.sqrt((color_list[1]-216)**2)<10 and math.sqrt((color_list[2]-246)**2)<10):
        good_line = find_line.find_line(resource)
        if good_line:
            moove.click(good_line['x'], good_line['y'])
    else:
    # affichier les prix des reources 3
        good_line = {'x':621, 'y':206}
        moove.click(good_line['x'], good_line['y'])

    # ==============================================
    # ===verif ouverture prix ressource ==========
    # ==============================================

    while True and good_line :
        color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), good_line['x']+279, good_line['y']+66)
        color_list = couleur.RGB(color)
        time.sleep(0.5)

        #if (math.sqrt((color_list[0]-35))**2<100 and math.sqrt((color_list[1]-39)**2)<100 and math.sqrt((color_list[2]-39)**2) <100 ):

        # ==============================================
        # prendre screen du prix
        # ==============================================
        take_screen.take_screen('prix100', good_line['x']+279, good_line['y']+148, good_line['x']+400, good_line['y']+167)

        # ==============================================
        # annalyser prix ressource
        # ==============================================

        prix100 = annalyse_picture.annalyse_picture('prix100')

        take_screen.take_screen('prix10', good_line['x']+279, good_line['y']+96, good_line['x']+400, good_line['y']+141)

        # ==============================================
        # annalyser prix ressource
        # ==============================================
        prix10 = annalyse_picture.annalyse_picture('prix10')

        take_screen.take_screen('prix1', good_line['x']+279, good_line['y']+51, good_line['x']+400, good_line['y']+86)

        # ==============================================
        # annalyser prix ressource
        # ==============================================
        prix1 = annalyse_picture.annalyse_picture('prix1')

        # ==============================================
        # stocker les prix
        # ==============================================
        update_price.update_price(resource, prix100, prix10, prix1)

        break
    # ==============================================
    # suprimer le nom de la resource
    # ==============================================
    moove.click(570, 200)

   # keyboard.press_and_release('suppr')

    keyboard.write("")

    time.sleep(1)