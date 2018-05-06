# we are going to learn how to do basic controls of a game.
# I don't know what game yet, so that is a problem. but I
# will find one with easy controls.

# import pyautogui to control mouse and keyboard

import pyautogui
import sys
from PIL import Image 
# sets pause to 0 for instant action, and failsafe to true so
# you can exit the loop by moving the mouse to the top corner
# later I'll make an easy way to break the loop manually

pyautogui.PAUSE = .05
pyautogui.FAILSAFE = True
choice = ""
time = ""

# find the image based off a picture you took, and match it to
# something on the screen

while(True):
    print ("what do you want me to do?")
    print ("1: click the cookie a few times")
    print ("2: buy upgrades")
    print ("3: buy buildings")
    print ("4: click the cookie for a period of time")
    print ("5: exit the program")
    choice = input('>')

    if choice == "1":
        print ('How many times do you want to click the cookie?')
        clicks = input('>')
        pyautogui.click(130, 465)

        for counter in range(1, int(clicks)):
            pyautogui.click()
        pyautogui.click(1301,1004)

    if choice == "2":
        for upgrades in range(1, 20):
            pyautogui.click(685, 224)
        pyautogui.click(1301,1004)

    if choice == "3":
        print("this is atempt to buy the highest tier building")
        print("and then work down the list from there.")

        for buildings in range(1, 10):
            pyautogui.click(813, 666)
            pyautogui.click(813, 591)
            pyautogui.click(813, 520)
            pyautogui.click(813, 463)            
            pyautogui.click(813, 394)
            pyautogui.click(813, 356)
        pyautogui.click(1301,1004)

    if choice == "4":
        print ("how long do you want to click the cookie for?")
        print ("input time in seconds")
        time = input(">")
        time = int(time) * 20
        print (time)
        for durration in range(1, int(time)):
            pyautogui.click(130, 465)
        pyautogui.click(1301,1004)
        
    if choice == "5":
        sys.exit()