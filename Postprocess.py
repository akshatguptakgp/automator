import cv2
import pandas as pd
import utils
import numpy as np
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
if __name__ == "__main__":
    csv_file = "saved_snips_for_cliks/commands.csv"
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
        print(text)

        try:
            print(text)
            if "timer" != text.split()[0]:
                print("breaked", text.split()[0])
                break
            df_output = df_output.append(
                            { "frame_no": frame_no,
                              "time": eval(text.split()[1])
                            },ignore_index=True)
        except:
            continue
#        print(df_output)
#        print(df_output.shape) 
# 
    cap.release()
    df_output.to_csv("saved_snips_for_cliks/timer_video.csv")

def extractTimeFromFrame(frame):
    text = pytesseract.image_to_string(frame)
    return eval(text.split()[1])
