import numpy as np 
import pyautogui as auto 
import keyboard 
import os 
from pynput.mouse import Button, Controller 
import utils 
import time 
def main(): 
    def endProgram(): 
        keyboard.unhook_all_hotkeys() 
        print('Ending program in between') 
        os._exit(0) 
    keyboard.add_hotkey('Esc+q', endProgram,suppress=True) 
    mouse = Controller() 
    auto.moveTo( x=565.80078125, y=1074.69140625,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("python3","b'AUTOMATOR'",[1152.0, 668.0, 1764.0, 1090.0],565.80078125,1074.69140625,5) 
    x,y = utils.searchImageFromScreenshotForNSeconds("saved_snips_for_cliks/1596910328_700.png",x=x, y=y, N=2) 
    auto.moveTo( x=x, y=y,duration=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 0.1) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.1) 
    auto.click(clicks=2) 
    auto.sleep(0.5) 
    keyboard.press("command") 
    auto.sleep(0.5) 
    keyboard.press("q") 
    auto.sleep(0.5) 
    keyboard.release("command") 
    auto.sleep(0.5) 
    keyboard.release("q") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
