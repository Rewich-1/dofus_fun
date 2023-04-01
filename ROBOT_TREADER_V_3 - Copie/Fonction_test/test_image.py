import cv2
#import win32ui
import numpy as np
import pandas as pd
#import imutils
#from __future__ import division
import os
from PIL import Image
import pyscreenshot as ImageGrab
#df = pd.read_csv("localisation.csv")

def takescreen():
    try:
        os.remove("map_screen.png")
    except:
        print('o')
    """
    im = ImageGrab.grab(bbox=(200, 350, 830, 500))
    im.save('map_screen.png')
    im = Image.open("map_screen.png").convert('RGBA')
    im.save("map_screen.png")
"""

    im = ImageGrab.grab(bbox=(900, 345, 1021, 358))
    im.save('map_screen.png')
    im = Image.open("map_screen.png").convert('RGBA')
    im.save("map_screen.png")



takescreen()