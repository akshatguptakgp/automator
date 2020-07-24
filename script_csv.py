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
    keyboard.press("left windows") 
    auto.sleep(1.0) 
    keyboard.press("d") 
    auto.sleep(1.0) 
    keyboard.release("left windows") 
    auto.sleep(1.0) 
    keyboard.release("d") 
    auto.sleep(1.0) 
    auto.moveTo( x=36.0, y=309.0,duration=4.0567121505737305) 
    x,y = utils.searchAppNameForNSeconds("explorer.exe","nan",(0, 0, 1366, 768),36.0,309.0,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/0.png",x=x, y=y, N=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 3.0567121505737305) 
    auto.moveTo( x=36.0, y=309.0,duration=1.1120803356170654) 
    x,y = utils.searchAppNameForNSeconds("explorer.exe","nan",(0, 0, 1366, 768),36.0,309.0,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/1.png",x=x, y=y, N=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 0.11208033561706543) 
    auto.moveTo( x=36.0, y=309.0,duration=1.1030726432800293) 
    x,y = utils.searchAppNameForNSeconds("explorer.exe","nan",(0, 0, 1366, 768),36.0,309.0,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/2.png",x=x, y=y, N=2) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.1030726432800293) 
    keyboard.press("esc") 
    auto.sleep(1.0) 
    stream.stop() 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
