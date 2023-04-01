import win32api
import win32gui

def rgbint2rgbtuple(RGBint):

    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255

    return (red, green, blue)
color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 900, 255)
liste = rgbint2rgbtuple(color)
print (liste[0])