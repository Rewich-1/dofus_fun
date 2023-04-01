import keyboard
import time
import win32api, win32con, win32gui

x = 0

def rgbint2rgbtyup(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red,green,blue)

time.sleep(1)
#win32api.SetCursorPos((1450,503)) #droit
color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()),820,32)
color_list = rgbint2rgbtyup(color)
for x in range(25):
    win32api.SetCursorPos((805,35)) #droit
    #color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 1588-x,503)
    color_list = rgbint2rgbtyup(color)
    print(color_list)