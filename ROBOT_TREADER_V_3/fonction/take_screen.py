import os
import pyscreenshot as ImageGrab
from PIL import Image

def take_screen(name,x1,y1, x2,y2):
    try:
        os.remove("../screen/"+name+".png")
    except:
        print('')

    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im.save("Screen/"+name+".png")
    im = Image.open("Screen/"+name+".png").convert('RGBA')
    im.save("Screen/"+name+".png")


