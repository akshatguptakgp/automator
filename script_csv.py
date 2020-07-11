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
    auto.moveTo( x=2471.421875, y=8.851562500000002,duration=1.0) 
    auto.sleep(1.0) 
    utils.searchAppNameForNSeconds("python3",5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/0.png",10) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2) 
    keyboard.press("c") 
    auto.sleep(1.0) 
    keyboard.release("c") 
    auto.sleep(1.0) 
    keyboard.press("h") 
    auto.sleep(1.0) 
    keyboard.release("h") 
    auto.sleep(1.0) 
    auto.moveTo( x=2471.421875, y=8.851562500000002,duration=1.6414787769317636) 
    utils.searchAppNameForNSeconds("python3",5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/1.png",10) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.6414787769317636) 
    keyboard.press("r") 
    auto.sleep(1.0) 
    keyboard.release("r") 
    auto.sleep(1.0) 
    keyboard.press("o") 
    auto.sleep(1.0) 
    keyboard.release("o") 
    auto.sleep(1.0) 
    keyboard.press("m") 
    auto.sleep(1.0) 
    keyboard.release("m") 
    auto.sleep(1.0) 
    keyboard.press("e") 
    auto.sleep(1.0) 
    keyboard.release("e") 
    auto.sleep(1.0) 
    keyboard.press("enter") 
    auto.sleep(1.0) 
    keyboard.release("enter") 
    auto.sleep(1.0) 
    keyboard.press("command") 
    auto.sleep(1.0) 
    keyboard.press("n") 
    auto.sleep(1.0) 
    keyboard.release("n") 
    auto.sleep(1.0) 
    keyboard.release("command") 
    auto.sleep(1.0) 
    stream.stop() 
if __name__ == '__main__': 
    main() 
