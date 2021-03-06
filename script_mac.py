import pandas as pd
import pyautogui as auto
import utils
def main():
    ## every line corresponds to a command ##
    df = pd.read_csv('saved_snips_for_cliks/combined_commands.csv')
    SCREEN_WIDTH,SCREEN_HEIGHT = auto.size()
    print(df)
    file1 = open("script_csv.py","w")
    file1.write("import numpy as np \n")
    file1.write("import pyautogui as auto \n")
    file1.write("import keyboard \n")
    file1.write("import os \n")
    file1.write("from pynput.mouse import Button, Controller \n")
    file1.write("import utils \n")
    file1.write("import time \n")
    # file1.write("import mouse \n")
    # file1.write("import mouse \n")
    file1.write("def main(): \n")
    file1.write("    def endProgram(): \n")
    file1.write("        keyboard.unhook_all_hotkeys() \n")
    file1.write("        print('Ending program in between') \n")
    # file1.write("        raise SystemExit(0) \n")
    file1.write("        os._exit(0) \n")

    file1.write("    keyboard.add_hotkey('Esc+q', endProgram,suppress=True) \n")
    file1.write("    mouse = Controller() \n")
    # print("-------- .py file --------")
    threshold = 1.0
    waitForImageTime = 2
    waitForAppNameTime = 5
    index_to_skip = []
    prev_hold_time = None
    for index, row in df.iterrows():
        if index in index_to_skip:
            continue

        duration = 2
        if index!=0:
            duration = row.time - df.iloc[index-1].time
            #initialize first command
        if index==0 :
            if row.button == "Button.left" or row.button == "Button.right":
                file1.write("""    auto.moveTo( x={}, y={},duration={}) \n""".format(df.iloc[0].x*SCREEN_WIDTH,df.iloc[0].y*SCREEN_HEIGHT,threshold))
                file1.write("""    auto.sleep({}) \n""".format(threshold))

    #double clicks 4 values remain same!
        if row.button == "Button.left" or row.button == "Button.right":
            if index+3<df.shape[0]:
                if not df.iloc[index+1].isnull().x and not df.iloc[index+2].isnull().x and not df.iloc[index+3].isnull().x:
                    if df.iloc[index+1].button == df.iloc[index+2].button == df.iloc[index+3].button == "Button.left":
                        if df.iloc[index].x==df.iloc[index+1].x==df.iloc[index+2].x==df.iloc[index+3].x and df.iloc[index].y==df.iloc[index+1].y==df.iloc[index+2].y==df.iloc[index+3].y:
                            # file1.write("""    time.sleep(1) \n""")
                            file1.write("""    x,y = utils.searchAppNameForNSeconds("{}","{}",{},{},{},{}) \n""".format(row.active_software_name,row.active_window_name,row.active_window_bbox,row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT,waitForAppNameTime))
                            file1.write("""    x,y = utils.searchImageFromScreenshotForNSeconds("{}",x=x, y=y, N={}) \n""".format("saved_snips_for_cliks/" + str(row.time).split(".")[0] + "_" + str(row.time).split(".")[1][:3] + ".png", waitForImageTime))
                            file1.write("""    auto.moveTo( x=x, y=y,duration={}) \n""".format(2))
                            file1.write("""    auto.mouseDown(button='{}', x=x, y=y, duration = {}) \n""".format('left',0.1))
                            file1.write("""    auto.mouseUp(button='{}', x=x, y=y, duration = {}) \n""".format('left',0.1))
                            file1.write("""    auto.click(clicks=2) \n""")
                            index_to_skip.append(index+1)
                            index_to_skip.append(index+2)
                            index_to_skip.append(index+3)
                            continue

    #move to actual coordinates
        if row.button == "Button.left" or row.button == "Button.right":
            print(type(row.active_window_bbox))
            print(eval(row.active_window_bbox))
            print(type(eval(row.active_window_bbox)))

            button_name = row.button.split('.')[1]            
            if row.pressed == "pressed":            
                file1.write("""    x,y = utils.searchAppNameForNSeconds("{}","{}",{},{},{},{}) \n""".format(row.active_software_name,row.active_window_name,row.active_window_bbox,row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT,waitForAppNameTime))   
                file1.write("""    x,y = utils.searchImageFromScreenshotForNSeconds("{}",x=x, y=y, N={}) \n""".format("saved_snips_for_cliks/" + str(row.time).split(".")[0] + "_" + str(row.time).split(".")[1][:3] + ".png", waitForImageTime))
                file1.write("""    auto.moveTo( x=x, y=y,duration={}) \n""".format(5))

                # if (index+1!=df.shape[0])  and (df.iloc[index+1].button=="moveTo"):
                #     file1.write("""    auto.click(clicks=1) \n""")
                #     continue

                # file1.write("""    auto.mouseDown(button='{}', x=x, y=y, duration = {}) \n""".format(button_name,0.1)) # duration
                file1.write("""    auto.click(clicks=1,button='{}') \n""".format(button_name))
            
            elif row.pressed == "released":
                if (index-1!=0)  and (df.iloc[index-1].button=="moveTo"):
                    file1.write("""    x,y = utils.searchAppNameForNSeconds("{}","{}",{},{},{},{}) \n""".format(row.active_software_name,row.active_window_name,row.active_window_bbox,row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT,waitForAppNameTime))
                    file1.write("""    auto.dragTo( x=x, y=y,button='left') \n""")
                    # file1.write("""    auto.dragTo( x={}, y={},button='left') \n""".format(row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT))
                    continue
                # file1.write("""    auto.mouseUp(button='{}', x={}, y={}, duration = {}) \n""".format(button_name,row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT,0.1))
            else:
                raise utils.CustomException("recordingButton has undefined text")

    #scroll commands
        elif row.button=="hscroll" or row.button=="vscroll":
            dx = 0
            dy = 0
            if row.button=="hscroll":
                dx = int(eval(row.pressed))
            if row.button=="vscroll":
                dy = 5*int(eval(row.pressed))

            if (index-1==0) or (df.iloc[index-1].button!="hscroll" and df.iloc[index-1].button!="vscroll"):
                file1.write("""    x,y = utils.searchAppNameForNSeconds("{}","{}",{},{},{},{}) \n""".format(row.active_software_name,row.active_window_name,row.active_window_bbox,row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT,waitForAppNameTime))
                file1.write("""    auto.moveTo( x=x, y=y,duration={}) \n""".format(5))

            if dx!=0:
                for _ in range(abs(dx)):
                    if dx > 0:
                        sign = 1
                    else:
                        sign = -1
                    file1.write("""    mouse.scroll(dx={}, dy={}) \n""".format(sign,0))
            print(dy,type(dy))
            if dy!=0:
                for _ in range(abs(dy)):
                    if dy > 0:
                        sign = 1
                    else:
                        sign = -1
                    file1.write("""    mouse.scroll(dx={}, dy={}) \n""".format(0,sign))

        # elif row.button=="moveTo":
            # auto.moveTo( x=57.43359375, y=116.6015625,duration=0.01) 
            # file1.write("""    auto.dragTo( x={}, y={},button='left') \n""".format(row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT))
            # file1.write("""    auto.moveTo( x={}, y={},duration={}) \n""".format(row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT,0.01))#duration

    #keyboard commands
        elif row.pressed in ["down","up"]:
            file1.write("""    auto.sleep({}) \n""".format(0.5))
            if row.pressed == "down":
                if row.button in ["down","up","right","left"] and index-1>=0 and df.iloc[index-1].button==row.button:
                    continue

                file1.write("""    keyboard.press("{}") \n""".format(row.button))
                # file1.write("""    auto.keyDown("{}") \n""".format(row.button))
                prev_hold_time = row.time

            elif row.pressed == "up":
                if (row.button in ["down","up","right","left"]) and (prev_hold_time is not None):
                    file1.write("""    utils.hold_key("{}",{}) \n""".format(row.button,row.time - prev_hold_time))
                else:
                    file1.write("""    keyboard.release("{}") \n""".format(row.button))
                    # file1.write("""    auto.keyUp("{}") \n""".format(row.button))
                

        if (index!=df.shape[0]-1) and (not df.iloc[index+1].isnull().x) and (not df.iloc[index+1].isnull().y) and row.button!="moveTo":
            if (df.iloc[index+1].button=="vscroll" and df.iloc[index].button=="vscroll") or (df.iloc[index+1].button=="hscroll" and df.iloc[index].button=="hscroll"):
                threshold = 0.0
            # file1.write("""    auto.moveTo( x={}, y={},duration={}) \n""".format(df.iloc[index+1].x*SCREEN_WIDTH,df.iloc[index+1].y*SCREEN_HEIGHT,df.iloc[index+1].time-row.time+threshold))

    file1.write("""    utils.speakText("Task completed sucessfully") \n""")
    file1.write("""if __name__ == '__main__': \n""")
    file1.write("""    main() \n""")
    file1.close()


if __name__ == '__main__':
    main()