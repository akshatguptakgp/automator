import cv2
import pandas as pd
import utils
import numpy as np
import pytesseract
from PIL import Image
import sys
import matplotlib.pyplot as plt
from utils import *
import pyautogui as auto
import math


if sys.platform in ['Windows', 'win32', 'cygwin']:
    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'


def ocr_on_rec_video():
    window_info_file = "saved_snips_for_cliks/WindowInfo.csv"
    screen_recording_file = "saved_snips_for_cliks/recording.mp4"

    df_info = pd.read_csv(window_info_file)
    df_info = df_info[(df_info.time<df_info.time[0]+5) & (df_info.active_window_name==df_info.active_window_name[0])] # improveFlag

    print("df_info.shape: ", df_info.shape)
    print("np.unique(df_info.active_window_bbox): ", np.unique(df_info.active_window_bbox))

    if df_info.shape[0]==0:
        utils.CustomException("Error: df_info size is 0")
    elif np.unique(df_info.active_window_bbox).shape[0]!=1:
        utils.CustomException("Error: Automator app is shifted or scaled in initial 5 seconds")

    # get bbox of timer on screen
    x1,y1,x2,y2 = eval(df_info.active_window_bbox[0])
    heightOffset = y2-y1-400 # w: 612, h: 400,100 X,350 Y,200 W ,16 H
    # frame = frame[int(y1+heightOffset):int(y2),int(x1):int(x2)]
    x1_,y1_,x2_,y2_ = int(x1+90),int(y1+heightOffset+350-10),int(x1+100+350),int(y1+heightOffset+350+25)



    cap = cv2.VideoCapture(screen_recording_file)
    if (cap.isOpened() == False):
      utils.CustomException("Error: screen_recording_file is not present")

    fps = round(cap.get(cv2.CAP_PROP_FPS));
    frame_no = -1
    df_output = pd.DataFrame()
    while True:
        ret, frame = cap.read()
        if ret == False:
            print("not able to read frame")
            break
        if frame_no/fps > 5:
            break
        frame_no += 1
        frame = frame[y1_:y2_,x1_:x2_]
        filename = "saved_snips_for_cliks/timer_" + str(frame_no)+ ".png"
        cv2.imwrite(filename,frame)
#        cv2.rectangle(frame,(x1_,y1_), (x2_,y2_),(0,255,0),3)
#        cv2.imshow('frame',frame)
#        cv2.waitKey()
#        cv2.destroyAllWindows()
        text = pytesseract.image_to_string(Image.open(filename))
        try:
            text_ = ''
            for elem in text:
                if elem in ['0','1','2','3','4','5','6','7','8','9']:
                    text_ += elem
            text = text_
            if len(text)>=10 and type(eval(text))==int:
                print("passed: ", text,eval(text))
                df_output = df_output.append(
                            { "frame_no": frame_no,
                              "time": eval(text)/10000.0
                            },ignore_index=True)
            else:
                print("failed: ", text,eval(text))
                break
        except:
            continue
#        print(df_output)
#        print(df_output.shape)
#
    cap.release()
    df_output.to_csv("saved_snips_for_cliks/timer_video.csv")


def add_windoInfo_and_save_image_from_timer_csv():
    windowInfo_timePreviousSec = 0.05
    frame_timePreviousSec = 0.1

    commands_csv_file = "saved_snips_for_cliks/commands.csv"
    window_info_file = "saved_snips_for_cliks/WindowInfo.csv"
    screen_recording_file = "saved_snips_for_cliks/recording.mp4"
    timer_video_csv_file = "saved_snips_for_cliks/timer_video.csv"
    df_info = pd.read_csv(window_info_file)
    df_commands = pd.read_csv(commands_csv_file)
    df_timer_video = pd.read_csv(timer_video_csv_file)

    SCREEN_WIDTH, SCREEN_HEIGHT = auto.size()

    cap = cv2.VideoCapture(screen_recording_file)
    if (cap.isOpened() == False):
      utils.CustomException("Error: screen_recording_file is not present")
    fps = round(cap.get(cv2.CAP_PROP_FPS));

    x = df_timer_video.time
    y = df_timer_video.frame_no
    m, b = np.polyfit(x[int(len(x)/2.0):], y[int(len(x)/2.0):], 1) # #m = slope, b = intercept
    # plt.plot(x, y, 'o')
    # x = np.arange(0,1000,1)
    # plt.plot(x, m*x + b)
    # plt.show()

    info_list = np.array([ [row.time, (row.active_software_name,row.active_window_name,row.active_window_bbox)]  for index, row in df_info.iterrows()])

    arr_img_path,arr_active_software_name,arr_active_window_bbox,arr_active_window_name = [],[],[],[]
    for index, row in df_commands.iterrows():
        print(index)
        frame_no = int(m*(row.time-frame_timePreviousSec)+b)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = cap.read()
        if ret == False:
            utils.CustomException("Error: frame_no: ",frame_no, "not present")

        img_path = None
        if not math.isnan(row.x) and not math.isnan(row.y):
            img_path = "saved_snips_for_cliks/" + str(index) + ".png"
            utils.cropAroundPoint(np.array(frame), row.x*SCREEN_WIDTH,row.y*SCREEN_HEIGHT,40,img_path)

        t,info = info_list[ info_list[:,0]< row.time-windowInfo_timePreviousSec][-1]
        active_software_name, active_window_name, active_window_bbox = info
        arr_active_software_name.append(active_software_name)
        arr_active_window_name.append(active_window_name)
        arr_active_window_bbox.append(active_window_bbox)
        arr_img_path.append(img_path)

    df_commands["img_path"] = arr_img_path
    df_commands["active_software_name"] = arr_active_software_name
    df_commands["active_window_name"] = arr_active_window_name
    df_commands["active_window_bbox"] = arr_active_window_bbox
    df_commands.to_csv("saved_snips_for_cliks/combined_commands.csv")
    cap.release() # stiens gate,

if __name__ == "__main__":
    # ocr_on_rec_video()
    add_windoInfo_and_save_image_from_timer_csv()
