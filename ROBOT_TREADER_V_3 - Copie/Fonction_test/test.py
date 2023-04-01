from ctypes import windll, Structure, c_long, byref
import time
import win32gui

def RGB(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red, green, blue)

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    time.sleep(1)
    return { "x": pt.x, "y": pt.y}


while True :
    pos = queryMousePosition()
    print(pos)
    #print(pos['x'], pos['y'])
    color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), pos['x'], pos['y'])
    color_list = RGB(color)
    print(color_list)
