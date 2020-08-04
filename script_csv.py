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
    auto.moveTo( x=277.0234375, y=134.3828125,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("python3","b'AUTOMATOR'",[974.0, 510.0, 1586.0, 932.0],277.0234375,134.3828125,5) 
    x,y = utils.searchImageFromScreenshotForNSeconds("saved_snips_for_cliks/1596566087_494.png",x=x, y=y, N=2) 
    auto.moveTo( x=x, y=y,duration=5) 
    auto.dragTo( x=1028.4023437499998, y=153.4140625,button='left') 
    keyboard.press("esc") 
    auto.sleep(1.0) 
    keyboard.press("esc") 
    auto.sleep(1.0) 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
