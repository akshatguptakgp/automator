# 31 May 20:
"""
mainui button √
read the mouse and keyboard events √
save events in csv √
read csv and convert to python script
execute python script at command by UI

"""
from PyQt5 import QtWidgets, uic
import os
import sys
import argparse
import utils
import cv2
import pynput
from EventRecord import EventRecord
import script
import script_csv

#testing functionality of screenshot searchImageFromScreenshot
#import pyautogui as auto
#template = cv2.imread("template.jpg",0)
#cordx,cordy = searchImageFromScreenshot(template)
#auto.moveTo(cordx,cordy,duration=5)

#testing functionality of taking snip from cursor location
##%%
#import pyautogui as auto
#import win32api
#import time
#from utils import takeSnapshot
##%%
#count=0
#pixel_size = 100
#state_left = win32api.GetKeyState(0x01)
#while True:
#    a = win32api.GetKeyState(0x01)
#    if a!=state_left: #button changed
#        state_left = a
#        if a<0:
#            takeSnapshot(pixel_size)
#            print('mouse event')
#    time.sleep(0.001)
#    #%%
#


parser = argparse.ArgumentParser()
parser.add_argument("-log", "--log", default="info",help=("Provide logging level. "    "Example --log debug', default='warning'"),)
log = utils.setupLogger(parser)

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    # Load the UI Page
    self.ui = uic.loadUi('ui.ui', self)
    self.ui.recordingButton.clicked.connect(self.recordingButtonPressed)
    self.ui.runButton.clicked.connect(self.runButtonPressed)

  def recordingButtonPressed(self):
    log.debug("recordingButtonPressed clicked")

    # toggling start and stop buttons
    if self.ui.recordingButton.text() == "Start":
#        os.system("rm saved_snips_for_cliks/*")
        self.ui.recordingButton.setText("Stop")
        self.ui.recordingButton.repaint()
        eventRecord = EventRecord(self.ui)
    elif self.ui.recordingButton.text() == "Stop":
        self.ui.recordingButton.setText("Start")
        self.ui.recordingButton.repaint()
    else:
        raise utils.CustomException("recordingButton has undefined text")

  def runButtonPressed(self):
    log.debug("runButtonPressed clicked")
    script.main() # creating script_csv.py fille
    script_csv.main() #calling script_csv fille

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  main = MainWindow()
  main.show()
  sys.exit(app.exec_())
