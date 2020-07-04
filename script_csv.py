import numpy as np
import pyautogui as auto
import keyboard
import os
from pynput.mouse import Button, Controller
from vidgear.gears import ScreenGear
import utils
import time

def main():
    print("main")
    stream = ScreenGear().start()
    def endProgram():
        keyboard.unhook_all_hotkeys()
        print('Ending program in between')
        stream.stop()
        os._exit(0)


    keyboard.add_hotkey('Esc+q', endProgram,suppress=True)
    mouse = Controller()
    auto.sleep(1.0)
    x,y = utils.searchImageFromScreenshot(stream,"saved_snips_for_cliks/0.png")
    print(x,y)
    auto.moveTo( x=x, y=y, duration = 2)

    auto.mouseDown(button='left', x=x, y=y, duration = 1)
    time.sleep(5)
    auto.mouseUp(button='left', x=x, y=y, duration = 1)
    stream.stop()


if __name__ == "__main__":
    main()
