#small program to track the mouse

import pyautogui

pyautogui.pause = 1
pyautogui.FAILSAFE = True


while(True):
    print(pyautogui.position())
    