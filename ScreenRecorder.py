import time
import sys
import os
from threading import Thread
import cv2
import numpy as np
from queue import Queue
from vidgear.gears import ScreenGear
import utils

if sys.platform in ['Windows', 'win32', 'cygwin']:
    print("using windows platform for screen recording")
    from screen_recorder_sdk import screen_recorder

def mac_start_screencapture():
    os.system("screencapture -v saved_snips_for_cliks/recording.mp4")
    return

def mac_stop_screencapture():
    os.system("^C")
    return

class ScreenRecorder:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self):
        print("ScreenRecorder initialized")

    def start(self):
        try:
            os.system("rm saved_snips_for_cliks/recording.mp4")
        except:
            pass

        if sys.platform in ['Windows', 'win32', 'cygwin']:
            screen_recorder.enable_dev_log ()
            screen_recorder.init_resources ()
            screen_recorder.start_video_recording("saved_snips_for_cliks/recording.mp4")
            print("started video recording")

        elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
            Thread(target=mac_start_screencapture, args=(), daemon=True).start()
            print("started video recording")
        else:
            utils.CustomException("sys.platform={platform} is unknown. Please report.".format(platform=sys.platform))

        return self
    def stop(self):
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            screen_recorder.stop_video_recording()
            screen_recorder.start_video_recording(".dummy_video.mp4")
            time.sleep(1)
            screen_recorder.stop_video_recording()
            screen_recorder.free_resources()
            print("stopped video recording")
        elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
            Thread(target=mac_stop_screencapture, args=(), daemon=True).start()
            print("stopped video recording")
        else:
            utils.CustomException("sys.platform={platform} is unknown. Please report.".format(platform=sys.platform))

if __name__ == "__main__":
    screenRecorder = ScreenRecorder()
    screenRecorder.start()
    time.sleep(5)
    screenRecorder.stop()
