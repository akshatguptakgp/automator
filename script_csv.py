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
    auto.moveTo( x=2468.3125, y=19.640625000000004,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("Python","b'AUTOMATOR'",[974.0, 510.0, 1586.0, 932.0],2468.3125,19.640625000000004,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/0.png",x=x, y=y, N=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2) 
    auto.moveTo( x=2468.3125, y=19.640625000000004,duration=1.1437706947326665) 
    x,y = utils.searchAppNameForNSeconds("Python","b'AUTOMATOR'",[974.0, 510.0, 1586.0, 932.0],2468.3125,19.640625000000004,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/1.png",x=x, y=y, N=2) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.14377069473266646) 
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
    auto.moveTo( x=1314.93359375, y=537.0234375,duration=1.8493609428405762) 
    x,y = utils.searchAppNameForNSeconds("Dictionary","b'Dictionary'",[1136.0, 523.0, 1536.0, 903.0],1314.93359375,537.0234375,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/2.png",x=x, y=y, N=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 0.8493609428405762) 
    auto.moveTo( x=1314.93359375, y=537.0234375,duration=1.2348678112030038) 
    x,y = utils.searchAppNameForNSeconds("Dictionary","b'Dictionary'",[1136.0, 523.0, 1536.0, 903.0],1314.93359375,537.0234375,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/3.png",x=x, y=y, N=2) 
    auto.mouseUp(button='left', x=x, y=y, duration = 0.23486781120300382) 
    stream.stop() 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
