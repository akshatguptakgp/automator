import numpy as np 
import pyautogui as auto 
import keyboard 
import os 
from pynput.mouse import Button, Controller 
def main(): 
    def endProgram(): 
        keyboard.unhook_all_hotkeys() 
        print('Ending program in between') 
        os._exit(0) 
    keyboard.add_hotkey('Esc+q', endProgram,suppress=True) 
    mouse = Controller() 
    auto.moveTo( x=1789.8958333333333, y=7.964062500000001,duration=1.0) 
    auto.sleep(1.0) 
    auto.mouseDown(button='left', x=1789.8958333333333, y=7.964062500000001, duration = 2) 
    auto.moveTo( x=1789.8958333333333, y=7.964062500000001,duration=1.2261939048767099) 
    auto.mouseUp(button='left', x=1789.8958333333333, y=7.964062500000001, duration = 0.22619390487670987) 
