
import os
from PIL import Image
import pyscreenshot as ImageGrab
import keyboard
import time

def takescreen():
    try:
        os.remove("map_screen.png")
    except:
        print('o')

    keyboard.press("y")
    #time.sleep(1)
    im=ImageGrab.grab(bbox=(0,0,1920,1080))
    im.save('map_screen.png')
    keyboard.release("y")
    keyboard.press_and_release('y', False, True)
    im = Image.open("map_screen.png").convert('RGBA')
    im.save("map_screen.png")