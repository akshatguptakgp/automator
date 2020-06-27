#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:13:46 2020

@author: sumityadav
"""
import pyautogui
from pynput import mouse
from pynput import keyboard
import time
import pandas as pd
import cv2
import os
import keyboard

def sum(x,y):
    return x+y

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

    def __init__(self,ui):
        self.df = pd.DataFrame()
        self.start_time = time.time()
        # Collect events until released
        self.listener_mouse = mouse.Listener(on_move=self.on_move,on_click=self.on_click,on_scroll=self.on_scroll)
        self.listener_mouse.start()
        self.ui = ui
        self.LEFT_KEY_PRESSED_FLAG = False
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = pyautogui.size()

        keyboard.start_recording() # Don't put anythiing below this line

    def on_press(self, key):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            self.df = self.df.append({"button": key.char, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "pressed"}, ignore_index=True)
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            self.df = self.df.append({"button": key, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "pressed"}, ignore_index=True)
        finally:
            print(self.df)

    def on_release(self, key):
        try:
            # print('alphanumeric key {0} pressed'.format(key.char))
            self.df = self.df.append({"button": key.char, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "released"}, ignore_index=True)
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            self.df = self.df.append({"button": key, "x": None, "y": None, "time": time.time()-self.start_time, "pressed": "released"}, ignore_index=True)
        finally:
            print(self.df)

    def on_move(self, x, y):
        # print('Pointer moved to {0}'.format(
        #     (x, y)))

        if x==0 and y==0:
            rk = keyboard.stop_recording()
            self.save_keyboard_events_to_df(rk)
            self.df = self.df.sort_values(by=["time"])
            self.df.to_csv("commands.csv")
            self.listener_mouse.stop()
            print("STOPPED THE PROCESS")
            print("SUCCESSFULLY")

        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT

        if self.LEFT_KEY_PRESSED_FLAG:
            self.df = self.df.append({"button": "moveTo", "x": x, "y": y, "time": time.time()-self.start_time, "pressed": "None"}, ignore_index=True)

            # self.ui.recordingButton.setText("Start")
            # self.ui.recordingButton.repaint()

    def on_click(self, x, y, button, pressed):
        # print(button)
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        print("self.SCREEN_WIDTH,self.SCREEN_HEIGHT: ",self.SCREEN_WIDTH,self.SCREEN_HEIGHT)
        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT
        if str(button)=="Button.left":
            if pressed:
                self.LEFT_KEY_PRESSED_FLAG=True
            else:
                self.LEFT_KEY_PRESSED_FLAG=False

        self.df = self.df.append({"button": str(button), "x": x, "y": y, "time": time.time()-self.start_time, "pressed": 'pressed' if pressed else 'released'}, ignore_index=True)
        # snip  = takeSnapshot(200)
        # print(snip.shape)
        # cv2.imwrite(os.path.join(os.getcwd(), "saved_snips_for_cliks",str(x) + "_" + str(y)+ ".jpg"),snip)
        print(self.df)

    def on_scroll(self,x, y, dx, dy):
        x = x/self.SCREEN_WIDTH
        y = y/self.SCREEN_HEIGHT
        # dx = dx/self.SCREEN_WIDTH
        # dy = dy/self.SCREEN_HEIGHT

        # print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
        if dy!=0:
            self.df = self.df.append({"button": "vscroll", "x": x, "y": y, "time": time.time()-self.start_time, "pressed": dy}, ignore_index=True)
        if dx!=0:
            self.df = self.df.append({"button": "hscroll", "x": x, "y": y, "time": time.time()-self.start_time, "pressed": dx}, ignore_index=True)

    def save_keyboard_events_to_df(self,rk):
        for i in range(len(rk)):
            self.df = self.df.append({"button": rk[i].name, "x": None, "y": None, "time":rk[i].time-self.start_time, "pressed": rk[i].event_type}, ignore_index=True)
