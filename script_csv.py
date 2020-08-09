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
    auto.moveTo( x=402.3203125, y=1014.8007812499999,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("python3","b'AUTOMATOR'",[974.0, 510.0, 1586.0, 932.0],402.3203125,1014.8007812499999,5) 
    x,y = utils.searchImageFromScreenshotForNSeconds("saved_snips_for_cliks/1596992392_772.png",x=x, y=y, N=2) 
    auto.moveTo( x=x, y=y,duration=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 0.1) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.1) 
    auto.click(clicks=2) 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    auto.sleep(0.5) 
    keyboard.press("esc") 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
