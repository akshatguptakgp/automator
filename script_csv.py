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
    auto.moveTo( x=1243.53125, y=522.09375,duration=1.0) 
    auto.sleep(1.0) 
    x,y = utils.searchAppNameForNSeconds("Python","b'AUTOMATOR'",[974.0, 510.0, 1586.0, 932.0],1243.53125,522.09375,5) 
    auto.moveTo( x=x, y=y,duration=5) 
    x,y = utils.searchImageFromScreenshotForNSeconds(stream,"saved_snips_for_cliks/0.png",x=x, y=y, N=2) 
    auto.mouseDown(button='left', x=x, y=y, duration = 2) 
    auto.moveTo( x=1249.828125, y=522.09375,duration=1.2890670299530034) 
    auto.moveTo( x=1249.828125, y=522.09375,duration=0.01) 
    auto.moveTo( x=1254.1289062500002, y=522.09375,duration=0.01) 
    auto.moveTo( x=1255.4726562499998, y=522.09375,duration=0.01) 
    auto.moveTo( x=1261.0898437500002, y=522.09375,duration=0.01) 
    auto.moveTo( x=1261.8398437499998, y=522.09375,duration=0.01) 
    auto.moveTo( x=1264.9960937500002, y=522.09375,duration=0.01) 
    auto.moveTo( x=1268.1523437500002, y=522.09375,duration=0.01) 
    auto.moveTo( x=1271.2109375, y=520.8671875,duration=0.01) 
    auto.moveTo( x=1273.3945312500002, y=520.8671875,duration=0.01) 
    auto.moveTo( x=1274.7734375, y=520.40625,duration=0.01) 
    auto.moveTo( x=1275.0625, y=520.40625,duration=0.01) 
    auto.moveTo( x=1277.2460937500002, y=519.8593750000001,duration=0.01) 
    auto.moveTo( x=1277.53515625, y=519.8593750000001,duration=0.01) 
    auto.moveTo( x=1278.2851562499998, y=519.48046875,duration=0.01) 
    auto.moveTo( x=1278.5664062499998, y=519.48046875,duration=0.01) 
    auto.moveTo( x=1278.8554687500002, y=519.48046875,duration=0.01) 
    keyboard.press("esc") 
    auto.sleep(1.0) 
    auto.moveTo( x=1279.0898437500002, y=519.48046875,duration=1.1702699661254883) 
    auto.moveTo( x=1279.0898437500002, y=519.48046875,duration=0.01) 
    stream.stop() 
    utils.speakText("Task completed sucessfully") 
if __name__ == '__main__': 
    main() 
