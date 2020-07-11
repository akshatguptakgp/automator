import numpy as np 
import pyautogui as auto 
import keyboard 
import os 
from pynput.mouse import Button, Controller 
from vidgear.gears import ScreenGear 
import utils 
import time 
def main(): 
    stream = ScreenGear().start() 
    def endProgram(): 
        keyboard.unhook_all_hotkeys() 
        print('Ending program in between') 
        os._exit(0) 
    keyboard.add_hotkey('Esc+q', endProgram,suppress=True) 
    mouse = Controller() 
    auto.moveTo( x=2462.515625, y=9.91015625,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("python3","b'AUTOMATOR'",[974.0, 510.0, 1586.0, 932.0],2462.515625,9.91015625,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2) 
    auto.moveTo( x=2462.79296875, y=9.91015625,duration=1.108688116073608) 
    x,y = utils.searchAppNameForNSeconds("python3","b'AUTOMATOR'",[974.0, 510.0, 1586.0, 932.0],2462.79296875,9.91015625,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.10868811607360795) 
    keyboard.press("d") 
    auto.sleep(1.0) 
    keyboard.release("d") 
    auto.sleep(1.0) 
    keyboard.press("i") 
    auto.sleep(1.0) 
    keyboard.release("i") 
    auto.sleep(1.0) 
    keyboard.press("c") 
    auto.sleep(1.0) 
    keyboard.release("c") 
    auto.sleep(1.0) 
    keyboard.press("enter") 
    auto.sleep(1.0) 
    keyboard.release("enter") 
    auto.sleep(1.0) 
    auto.moveTo( x=2097.79296875, y=524.03515625,duration=2.742003917694092) 
    x,y = utils.searchAppNameForNSeconds("Dictionary","b'Dictionary'",[1836.0, 509.0, 2417.0, 1135.0],2097.79296875,524.03515625,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    auto.mouseDown(button='left', x=x, y=y, duration = 1.7420039176940918) 
    auto.moveTo( x=2097.79296875, y=524.03515625,duration=1.1939671039581299) 
    x,y = utils.searchAppNameForNSeconds("Dictionary","b'Dictionary'",[1836.0, 509.0, 2417.0, 1135.0],2097.79296875,524.03515625,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.19396710395812988) 
    stream.stop() 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
