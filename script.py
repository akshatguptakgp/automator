import pandas as pd
import cv2
import numpy as np
import time
import pyautogui as auto
import utils

def main():
    ## every line corresponds to a command ##
    df = pd.read_csv('commands.csv')
    print(df)
    file1 = open("script_csv.py","w")
    file1.write("import numpy as np \n")
    file1.write("import pyautogui as auto \n")
    file1.write("import keyboard \n")
    file1.write("import os \n")
    file1.write("from pynput.mouse import Button, Controller \n")
    file1.write("def main(): \n")
    file1.write("    def endProgram(): \n")
    file1.write("        keyboard.unhook_all_hotkeys() \n")
    file1.write("        print('Ending program in between') \n")
    # file1.write("        raise SystemExit(0) \n")
    file1.write("        os._exit(0) \n")
    file1.write("    keyboard.add_hotkey('Esc+q', endProgram,suppress=True) \n")
    file1.write("    mouse = Controller() \n")
    print("-------- .py file --------")
    time_when_pressed = None
    threshold = 1.0
    for index, row in df.iterrows():
        duration = 2
        if index!=0:
            duration = row.time - df.iloc[index-1].time
            #initialize first command
        if index==0 :
            if row.button == "Button.left" or row.button == "Button.right":
                file1.write("""    auto.moveTo( x={}, y={},duration={}) \n""".format(df.iloc[0].x,df.iloc[0].y,threshold))
                file1.write("""    auto.sleep({}) \n""".format(threshold))

    #double clicks 4 values remain same!
        if row.button == "Button.left" or row.button == "Button.right":
            if index+3<df.shape[0]:
                if not df.iloc[index+1].isnull().x and not df.iloc[index+2].isnull().x and not df.iloc[index+3].isnull().x:
                    if df.iloc[index].x==df.iloc[index+1].x==df.iloc[index+2].x==df.iloc[index+3].x and df.iloc[index].y==df.iloc[index+1].y==df.iloc[index+2].y==df.iloc[index+3].y:
                        file1.write("""    auto.click(clicks=2) \n""")

    #move to actual coordinates
        if row.button == "Button.left" or row.button == "Button.right":
            button_name = row.button.split('.')[1]
            if row.pressed == "pressed":
                file1.write("""    auto.mouseDown(button='{}', x={}, y={}, duration = {}) \n""".format(button_name,row.x,row.y,duration))
            elif row.pressed == "released":
                file1.write("""    auto.mouseUp(button='{}', x={}, y={}, duration = {}) \n""".format(button_name,row.x,row.y,duration))
            else:
                raise utils.CustomException("recordingButton has undefined text")

    #scroll commands
        # elif row.button=="hscroll" or row.button=="vscroll":
        #     file1.write("""    auto.{}({},{},{}) \n""".format(row.button,row.pressed,row.x,row.y))
        elif row.button=="hscroll" or row.button=="vscroll":
            dx = 0
            dy = 0
            if row.button=="hscroll":
                dx = row.pressed
            if row.button=="vscroll":
                dy = row.pressed
            file1.write("""    mouse.scroll(dx={}, dy={}) \n""".format(dx,dy))

        elif row.button=="moveTo":
            file1.write("""    auto.moveTo( x={}, y={},duration={}) \n""".format(row.x,row.y,0.01))#duration

    #keyboard commands
        else:
            if row.pressed == "down":
                file1.write("""    keyboard.press("{}") \n""".format(row.button))
            elif row.pressed == "up":
                file1.write("""    keyboard.release("{}") \n""".format(row.button))
            file1.write("""    auto.sleep({}) \n""".format(threshold))

        if (index!=df.shape[0]-1) and (not df.iloc[index+1].isnull().x) and (not df.iloc[index+1].isnull().y) and row.button!="moveTo":
            if (df.iloc[index+1].button=="vscroll" and df.iloc[index].button=="vscroll") or (df.iloc[index+1].button=="hscroll" and df.iloc[index].button=="hscroll"):
                threshold = 0.0
            file1.write("""    auto.moveTo( x={}, y={},duration={}) \n""".format(df.iloc[index+1].x,df.iloc[index+1].y,df.iloc[index+1].time-row.time+threshold))
    file1.close()

if __name__ == '__main__':
    main()