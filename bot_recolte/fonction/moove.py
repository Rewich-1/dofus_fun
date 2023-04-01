import win32api, win32con, win32gui

def rgbint2rgbtyup(RGBint):
    blue = RGBint & 255
    green = (RGBint >> 8) & 255
    red = (RGBint >> 16) & 255
    return (red,green,blue)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)


def moove(actu_x,actu_y,new_x,new_y):
    if(actu_x > new_x and actu_y == new_y):   #guauche
        click(350,505)
    elif (actu_x < new_x and actu_y == new_y): #droit
        click(1570,510)
    elif (actu_y < new_y and actu_x == new_x): #bas
        click(1070,905)
    elif(actu_y > new_y and actu_x == new_x): #haut
        click(805,35)

    while True:
        #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,100,100,0,0)
        color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()),900,270)
        color_list = rgbint2rgbtyup(color)
        #time.sleep(0.25)
        if (color_list[0] == 0 and color_list[1] == 0 and color_list[2] == 0):
            break