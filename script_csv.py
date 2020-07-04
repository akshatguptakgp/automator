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
    auto.moveTo( x=2227.1875, y=14.49609375,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/0.png",10) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2) 
    auto.moveTo( x=2227.1875, y=14.49609375,duration=1.1224260330200195) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/1.png",10) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.12242603302001953) 
    auto.moveTo( x=2467.859375, y=16.300781250000004,duration=3.149348258972168) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/2.png",10) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2.149348258972168) 
    auto.moveTo( x=2467.859375, y=16.300781250000004,duration=1.1902048587799072) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/3.png",10) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.19020485877990723) 
    stream.stop() 
