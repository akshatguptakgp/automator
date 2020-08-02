#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:13:46 2020

@author: sumityadav
"""
import pyautogui as auto
from pynput import mouse
from pynput import keyboard
import mouse as mp
import time
import pandas as pd
import cv2
import os
import keyboard
import utils
from WindowInfoGetter import WindowInfoGetter
from ScreenRecorder import ScreenRecorder
import sys
import numpy as np
import functools
import copy
import asyncio
from threading import Thread
from ScreenGrab import VideoGet
from PyQt5.QtCore import QThread, pyqtSignal

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

class EventRecord():
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

    change_value = pyqtSignal(str)

    @catch_exception
    def __init__(self):
        super().__init__()
        self.time_completed = None
        print("starting time: ", time.time())
        self.window_getter = WindowInfoGetter().start()
        # self.screen_recorder = ScreenRecorder().start()
        self.video_getter = VideoGet().start()
        self.df = pd.DataFrame()
        self.listener_mouse = mouse.Listener(on_move=self.on_move,on_click=self.on_click,on_scroll=self.on_scroll, suppress=False)
        self.listener_mouse.start()
        self.LEFT_KEY_PRESSED_FLAG = False
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = auto.size()

        try:
            recorded_events_queue, hooked = keyboard._recording
            keyboard.unhook(hooked)
            keyboard.unhook_all_hotkeys()
        except:
            pass

        try:
            keyboard.add_hotkey('Esc+q', self.endProgram,suppress=True)
            keyboard.start_recording() # Don't put anythiing below this line
        except:
            recorded_events_queue, hooked = keyboard._recording
            try:
                keyboard.unhook(hooked)
                print("unhooked")
            except:
                print("unable to call keyboard.unhook")
                pass

            self.stop_event_recording(exceptionFlag=True)

        self.MAIN_PROCESS_RUNNING_FLAG = True
        # variables related to frameExtractor
        self.frameExtractorStopped = False
        self.frameExtractorDfIndexSeen = 0
        Thread(target=self.frameExtractor, args=(), daemon=True).start()
        print("completed init")
    def frameExtractor(self):
        while not self.frameExtractorStopped:
            df_commands = self.df
            if self.frameExtractorDfIndexSeen <= df_commands.shape[0]-1:
                for idx in range(self.frameExtractorDfIndexSeen,df_commands.shape[0]):
                    currentTime = df_commands.time[idx]
                    self.frameExtractorDfIndexSeen+=1
                    if self.time_completed is not None and self.time_completed < currentTime:
                        continue

                    if (df_commands.button[idx]=="Button.left" or df_commands.button[idx]=="Button.right") and (df_commands.pressed[idx]=="pressed"):
                        frame_queue = self.video_getter.frame_queue.queue
                        queue = np.array(frame_queue)
                        timePreviousSec = 0.01
                        closest_index = np.argmin(np.abs(currentTime-queue[:,0]-timePreviousSec))
                        print(idx)
                        print(type(np.array(queue[closest_index][1])))
                        frame = np.array(queue[closest_index][1])
                        utils.cropAroundPoint(np.array(frame), df_commands.x[idx]*self.SCREEN_WIDTH,df_commands.y[idx]*self.SCREEN_HEIGHT,40,"saved_snips_for_cliks/" + str(currentTime).split(".")[0] + "_" + str(currentTime).split(".")[1][:3] + ".png")
                        # cv2.imwrite("saved_snips_for_cliks/" + str(idx) + "_full.png", frame)
            else:
                time.sleep(1)

    def endProgram(self):
        self.time_completed = time.time()
        # keyboard.unhook_all_hotkeys()
        print('Ending program in between')
        if self.MAIN_PROCESS_RUNNING_FLAG:
            self.stop_event_recording()

    def stop_event_recording(self,exceptionFlag=False):
        self.video_getter.stop()
        # print("stopped screen_recorder")

        while self.frameExtractorDfIndexSeen != self.df.shape[0]-1:
            time.sleep(0.1)

        self.frameExtractorStopped = True

        self.window_getter.stop()
        print("stopped window_getter")

        self.listener_mouse.stop()

        try:
            recorded_events_queue, hooked = keyboard._recording
            # print(recorded_events_queue, hooked)
            try:
                keyboard.unhook(hooked)
            except:
                # print("unable to call keyboard.unhook")
                pass

            rk = list(recorded_events_queue.queue)
            if not exceptionFlag:
                self.save_keyboard_events_to_df(rk)
        except:
            raise
        try:
            self.df = self.df.sort_values(by=["time"])
            print(self.df)
        except:
            pass

        if self.time_completed is not None:
            self.df = self.df[self.df.time < self.time_completed]
        self.df.to_csv("saved_snips_for_cliks/commands.csv")
        utils.add_windoInfo_and_save_image_from_timer_csv()
        print("STOPPED THE PROCESS")
        print("SUCCESSFULLY")
        self.MAIN_PROCESS_RUNNING_FLAG = False

    @catch_exception
    def on_move(self, x, y):
        currentTime = time.time()
        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT

        if self.LEFT_KEY_PRESSED_FLAG:
            self.df = self.df.append({"button": "moveTo", "x": x, "y": y, "time": currentTime, "pressed": "None"}, ignore_index=True)

    @catch_exception
    def on_click(self, x, y, button, pressed):
        currentTime = time.time()
        # print(x,y,pressed)

        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT
        if str(button)=="Button.left":
            if pressed:
                self.LEFT_KEY_PRESSED_FLAG=True
            else:
                self.LEFT_KEY_PRESSED_FLAG=False

        self.df = self.df.append({"button": str(button), "x": x, "y": y, "time": currentTime, "pressed": 'pressed' if pressed else 'released'}, ignore_index=True)
        return

    @catch_exception
    def on_scroll(self,x, y, dx, dy):
        currentTime = time.time()
        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT

        if dy!=0:
            self.df = self.df.append({"button": "vscroll", "x": x, "y": y, "time": currentTime, "pressed": dy}, ignore_index=True)
        if dx!=0:
            self.df = self.df.append({"button": "hscroll", "x": x, "y": y, "time": currentTime, "pressed": dx}, ignore_index=True)

    @catch_exception
    def save_keyboard_events_to_df(self,rk):
        for i in range(len(rk)):
            if self.time_completed is not None and self.time_completed < rk[i].time:
                continue
            self.df = self.df.append({"button": rk[i].name, "x": None, "y": None, "time":rk[i].time, "pressed": rk[i].event_type}, ignore_index=True)
