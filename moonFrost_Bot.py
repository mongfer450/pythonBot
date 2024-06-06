import pyautogui
import pydirectinput
import time 

#countdown timer
print("Start", "end")
for i in range(0, 3):
    print(".", end="")
    time.sleep(0.5)
print("Go")

#functions 
def plantUp(): 
    time.sleep(0.5)
    pyautogui.click(1342, 686)
    pyautogui.click(button='right')
def plantDown(): 
    time.sleep(0.5)
    pyautogui.click(1196, 754)
    pyautogui.click(button='right')
def farming():
    for i in range(1,11):
        print(i, ": plantUp")
        plantUp()
        i+=1
    pydirectinput.press('w')
    pydirectinput.press('w')
    pydirectinput.press('d')
    pydirectinput.press('d')
    pydirectinput.press('d')
    for i in range(1,11):
        print(i, ": plantDown")
        plantDown()
        i+=1
    pydirectinput.press('a')
    pydirectinput.press('a')
    pydirectinput.press('s')
    pydirectinput.press('s')
    pydirectinput.press('s')
def buySeed():
    time.sleep(1)
    for i in range(1,101):
        print(i, ": Buy")
        pyautogui.click(2089, 1235)
        i+=1
def buyItem():
    time.sleep(1)
    pyautogui.click(1347, 710)
    for i in range(1,1001):
        print(i, ": Buy")
        pyautogui.click(2072, 1193)
        i+=1
#run function    
for i in range(1,3):
        print("--", i, ": Farming --")
        farming()
        # buySeed()
        # buyItem()
        i+=1     


#finish
print('Done')

