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
    auto.moveTo( x=1300.2734375, y=517.86328125,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/0.png",10) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2) 
    auto.moveTo( x=1300.2734375, y=518.1484375,duration=1.0970680713653564) 
    auto.moveTo( x=1300.2734375, y=518.1484375,duration=0.01) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/2.png",10) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.049428939819335715) 
    auto.moveTo( x=2468.2460937499995, y=9.050781249999998,duration=2.6055779457092285) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/3.png",10) 
    auto.mouseDown(button='left', x=x, y=y, duration = 1.6055779457092287) 
    auto.moveTo( x=2468.2460937499995, y=9.050781249999998,duration=1.1460092067718506) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/4.png",10) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.14600920677185059) 
    stream.stop() 
if __name__ == '__main__': 
    main() 
