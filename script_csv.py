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
    keyboard.press("left windows") 
    auto.sleep(1.0) 
    keyboard.press("d") 
    auto.sleep(1.0) 
    keyboard.release("d") 
    auto.sleep(1.0) 
    keyboard.release("left windows") 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("explorer.exe","nan",(0, 0, 1366, 768),46.0,219.0,5) 
    x,y = utils.searchImageFromScreenshotForNSeconds("saved_snips_for_cliks/1596366063_598.png",x=x, y=y, N=2) 
    auto.moveTo( x=x, y=y,duration=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 0.1) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.1) 
    auto.click(clicks=2) 
    x,y = utils.searchAppNameForNSeconds("explorer.exe","hacking",(-8, -8, 1374, 736),423.0,161.0,5) 
    x,y = utils.searchImageFromScreenshotForNSeconds("saved_snips_for_cliks/1596366065_965.png",x=x, y=y, N=2) 
    auto.moveTo( x=x, y=y,duration=5) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2.1479570865631104) 
    auto.mouseUp(button='left', x=423.0, y=161.0, duration = 0.06404471397399902) 
    keyboard.press("ctrl") 
    auto.sleep(1.0) 
    keyboard.press("v") 
    auto.sleep(1.0) 
    keyboard.release("v") 
    auto.sleep(1.0) 
    keyboard.release("ctrl") 
    auto.sleep(1.0) 
    keyboard.press("enter") 
    auto.sleep(1.0) 
    keyboard.release("enter") 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("explorer.exe","Documents",(-8, -8, 1374, 736),341.0,374.0,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    mouse.scroll(dx=0, dy=-18) 
    x,y = utils.searchAppNameForNSeconds("explorer.exe","Documents",(-8, -8, 1374, 736),296.0,611.0,5) 
    x,y = utils.searchImageFromScreenshotForNSeconds("saved_snips_for_cliks/1596366078_262.png",x=x, y=y, N=2) 
    auto.moveTo( x=x, y=y,duration=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 0.1) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.1) 
    auto.click(clicks=2) 
    keyboard.press("esc") 
    auto.sleep(0.0) 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
