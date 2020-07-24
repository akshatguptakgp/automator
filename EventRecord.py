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
from WindowInfoGetter import WindowInfoGetter
from ScreenRecorder import ScreenRecorder
import sys
import numpy as np
import functools
import copy
import asyncio
from threading import Thread

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
        print("starting time: ", time.time())
        self.df = pd.DataFrame()
        keyboard.add_hotkey('Esc+q', self.endProgram,suppress=True)
        self.listener_mouse = mouse.Listener(on_move=self.on_move,on_click=self.on_click,on_scroll=self.on_scroll, suppress=False)
        self.listener_mouse.start()
        self.ui = ui
        self.LEFT_KEY_PRESSED_FLAG = False
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = auto.size()
        self.window_getter = WindowInfoGetter().start()
        self.screen_recorder = ScreenRecorder().start()
        keyboard.start_recording() # Don't put anythiing below this line
        self.MAIN_PROCESS_RUNNING_FLAG = True

    def endProgram(self):
        # keyboard.unhook_all_hotkeys()
        print('Ending program in between')
        if self.MAIN_PROCESS_RUNNING_FLAG:
            self.stop_event_recording()


    def stop_event_recording(self,exceptionFlag=False):
        self.screen_recorder.stop()
        print("stopped screen_recorder")

        self.window_getter.stop()
        print("stopped window_getter")

        self.listener_mouse.stop()

        try:
            # rk = keyboard.stop_recording()
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

        self.df.to_csv("saved_snips_for_cliks/commands.csv")
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
            self.df = self.df.append({"button": rk[i].name, "x": None, "y": None, "time":rk[i].time, "pressed": rk[i].event_type}, ignore_index=True)
