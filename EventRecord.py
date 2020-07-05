#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:13:46 2020

@author: sumityadav
"""
import pyautogui as auto
from pynput import mouse
from pynput import keyboard
import time
import pandas as pd
import cv2
import os
import keyboard
import utils
from VideoWriterWidget import VideoGet
from WindowInfoGetter import WindowInfoGetter
import sys
import numpy as np
import functools
import copy

def catch_exception(f):
    @functools.wraps(f)
    def func(self, *args, **kwargs):
        try:
            return f(self,*args, **kwargs)
        except Exception as e:
            print(" *********************************************************************")
            self.stop_event_recording(exceptionFlag=True)
            print('Caught an exception in', f.__name__)
            raise
    return func

class EventRecord:
    """
    This class represents a bounding box detection in a single image.

    Parameters
    ----------
    tlwh : array_like
        Bounding box in format `(x, y, w, h)`

    Attributes
    ----------
    tlwh : ndarray
        Bounding box in format `(top left x, top left y, width, height)`.

    """

    @catch_exception
    def __init__(self,ui):
        self.df = pd.DataFrame()
        self.frame_timePreviousSec = 1
        self.windowInfo_timePreviousSec = 0.05
        self.start_time = time.time()
        # Collect events until released
        self.listener_mouse = mouse.Listener(on_move=self.on_move,on_click=self.on_click,on_scroll=self.on_scroll, suppress=False)
        self.listener_mouse.start()
        self.ui = ui
        self.LEFT_KEY_PRESSED_FLAG = False
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = auto.size()
        # src1 = '/Users/sumityadav/Drive/PROJECTS/rajesh_project/PYTHON/PYQT/Re-id_videoplayer/data/skivideo.mp4'
        # video_writer_widget1 = VideoWriterWidget('Camera 1', src1)
        self.window_getter = WindowInfoGetter().start()
        self.video_getter = VideoGet().start()
        keyboard.start_recording() # Don't put anythiing below this line

    def stop_event_recording(self,exceptionFlag=False):
        self.video_getter.stop()
        print("stopped video_getter")

        self.window_getter.stop()
        print("stopped window_getter")

        self.listener_mouse.stop()

        try:
            rk = keyboard.stop_recording()
            if not exceptionFlag:
                self.save_keyboard_events_to_df(rk)
        except:
            raise

        try:
            self.df = self.df.sort_values(by=["time"])
            print(self.df)
        except:
            pass

        self.df.to_csv("commands.csv")
        print("STOPPED THE PROCESS")
        print("SUCCESSFULLY")
        # sys.exit()

    @catch_exception
    def on_press(self, key):
        info_list = self.window_getter.info_list
        info_list = copy.deepcopy(info_list)
        info_list = np.array(info_list)
        t,info = info_list[ info_list[:,0]< time.time()-self.windowInfo_timePreviousSec][-1]
        active_software_name, active_window_name, active_window_bbox = info
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            self.df = self.df.append({"button": key.char, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "pressed","active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            self.df = self.df.append({"button": key, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "pressed","active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)
        finally:
            print(self.df)

    @catch_exception
    def on_release(self, key):
        info_list = self.window_getter.info_list
        info_list = copy.deepcopy(info_list)
        info_list = np.array(info_list)
        t,info = info_list[ info_list[:,0]< time.time()-self.windowInfo_timePreviousSec][-1]
        active_software_name, active_window_name, active_window_bbox = info
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            self.df = self.df.append({"button": key.char, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "released","active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            self.df = self.df.append({"button": key, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "released","active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)
        finally:
            print(self.df)

    @catch_exception
    def on_move(self, x, y):
        # print('Pointer moved to {0}'.format(
        #     (x, y)))

        if x==0 and y==0:
            self.stop_event_recording()

        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT

        if self.LEFT_KEY_PRESSED_FLAG:
            info_list = self.window_getter.info_list
            info_list = copy.deepcopy(info_list)
            info_list = np.array(info_list)
            t,info = info_list[ info_list[:,0]< time.time()-self.windowInfo_timePreviousSec][-1]
            active_software_name, active_window_name, active_window_bbox = info
            self.df = self.df.append({"button": "moveTo", "x": x, "y": y, "time": time.time()-self.start_time, "pressed": "None","active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)

            # self.ui.recordingButton.setText("Start")
            # self.ui.recordingButton.repaint()

    @catch_exception
    def on_click(self, x, y, button, pressed):
        # utils.takeSnapshotAroundCursor(200,"saved_snips_for_cliks/" + str(self.df.shape[0]) + ".png")
        currentTime = time.time()
        queue = np.array(self.video_getter.frame_queue.queue)
        info_list = self.window_getter.info_list
        info_list = copy.deepcopy(info_list)
        info_list = np.array(info_list)

        # imageFetch
        # print("queue[:,0]: ", queue[:,0])
        # print("currentTime-queue[:,0]: ", currentTime-queue[:,0])
        # closest_index = np.argmin(np.abs(currentTime-queue[:,0]-self.frame_timePreviousSec))
        # utils.cropAroundPoint(np.array(queue[closest_index][1]), x,y,40,img_path)
        if(queue.shape[0]==0 or info_list.shape[0]==0):
            print(queue.shape,info_list.shape)
            self.stop_event_recording(exceptionFlag = True)
        t,frame = queue[ queue[:,0]< currentTime-self.frame_timePreviousSec][-1]
        img_path = "saved_snips_for_cliks/" + str(self.df.shape[0]) + ".png"
        utils.cropAroundPoint(np.array(frame), x,y,40,img_path)
        print("frame fetch: ", "t: ", t, " currentTime: ", currentTime, queue[:,0])
        # App Info Fetch
        print(info_list)
        info_list = info_list[ info_list[:,0]< currentTime-self.windowInfo_timePreviousSec]
        
        t,info = info_list[-1]
        print("info fetch: ", "t: ", t, " currentTime: ", currentTime, info_list[:,0])

        # print("closest_index: ",closest_index)
        # print('{0} at {1}'.format( 'Pressed' if pressed else 'Released', (x, y)))
        # print("self.SCREEN_WIDTH,self.SCREEN_HEIGHT: ",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT
        if str(button)=="Button.left":
            if pressed:
                self.LEFT_KEY_PRESSED_FLAG=True
            else:
                self.LEFT_KEY_PRESSED_FLAG=False

        active_software_name, active_window_name, active_window_bbox = info
        self.df = self.df.append({"button": str(button), "x": x, "y": y, "time": time.time()-self.start_time, "pressed": 'pressed' if pressed else 'released', "img_path": img_path,"active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox }, ignore_index=True)
        print(self.df)


        # #-- Event unsupress
        # print("#-- Event unsupress \n ")
        # button_name = str(button).split('.')[1]
        # SCREEN_WIDTH,SCREEN_HEIGHT = auto.size()
        # if pressed:
        #     auto.mouseDown(button=button_name, x=x*SCREEN_WIDTH, y=y*SCREEN_HEIGHT, duration = 0)
        #     print("Event unsupress pressed")
        # else:
        #     auto.mouseUp(button=button_name, x=x*SCREEN_WIDTH, y=y*SCREEN_HEIGHT, duration = 0)
        #     print("Event unsupress released")

    @catch_exception
    def on_scroll(self,x, y, dx, dy):
        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT
        # dx = dx/self.SCREEN_WIDTH
        # dy = dy/self.SCREEN_HEIGHT

        # print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

        info_list = self.window_getter.info_list
        info_list = copy.deepcopy(info_list)
        info_list = np.array(info_list)
        t,info = info_list[ info_list[:,0]< time.time()-self.windowInfo_timePreviousSec][-1]
        active_software_name, active_window_name, active_window_bbox = info

        if dy!=0:
            self.df = self.df.append({"button": "vscroll", "x": x, "y": y, "time": time.time()-self.start_time, "pressed": dy,"active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)
        if dx!=0:
            self.df = self.df.append({"button": "hscroll", "x": x, "y": y, "time": time.time()-self.start_time, "pressed": dx,"active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)

    @catch_exception
    def save_keyboard_events_to_df(self,rk):
        info_list = self.window_getter.info_list
        info_list = copy.deepcopy(info_list)
        info_list = np.array(info_list)
        for i in range(len(rk)):
            t,info = info_list[ info_list[:,0]< rk[i].time-self.windowInfo_timePreviousSec][-1]
            active_software_name, active_window_name, active_window_bbox = info
            self.df = self.df.append({"button": rk[i].name, "x": None, "y": None, "time":rk[i].time-self.start_time, "pressed": rk[i].event_type, "active_software_name":active_software_name, "active_window_name":active_window_name, "active_window_bbox":active_window_bbox}, ignore_index=True)
