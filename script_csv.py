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
    auto.moveTo( x=1745.55859375, y=5.4765625,duration=1.0) 
    auto.sleep(1.0) 
    auto.mouseDown(button='left', x=1745.55859375, y=5.4765625, duration = 2) 
    auto.moveTo( x=1745.55859375, y=5.4765625,duration=1.613156795501709) 
    auto.mouseUp(button='left', x=1745.55859375, y=5.4765625, duration = 0.613156795501709) 
