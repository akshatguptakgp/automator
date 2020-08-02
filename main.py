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
import importlib
import time

parser = argparse.ArgumentParser()
parser.add_argument("-log", "--log", default="info",help=("Provide logging level. "    "Example --log debug', default='warning'"),)
log = utils.setupLogger(parser)


class MainWindow(QtWidgets.QMainWindow):
  def __init__(self, *args, **kwargs):
    super(MainWindow, self).__init__(*args, **kwargs)

    # Load the UI Page
    uic.loadUi('ui.ui', self)
    print(self.__dict__.keys())
    self.recordingButton.clicked.connect(self.recordingButtonPressed)
    self.runButton.clicked.connect(self.runButtonPressed)

  def recordingButtonPressed(self):
    log.debug("recordingButtonPressed clicked")

    # toggling start and stop buttons
    if self.recordingButton.text() == "Start":
        if not os.path.isdir("saved_snips_for_cliks"):
            os.mkdir("saved_snips_for_cliks")
        utils.deleteAllFilesInsideFolder("saved_snips_for_cliks")
        self.recordingButton.setText("Stop")
        self.recordingButton.repaint()
        eventRecord = EventRecord()

    elif self.recordingButton.text() == "Stop":
        self.recordingButton.setText("Start")
        self.recordingButton.repaint()
    else:
        utils.CustomException("recordingButton has undefined text")

  def runButtonPressed(self):
    log.debug("runButtonPressed clicked")
    script.main() # creating script_csv.py fille
    import script_csv
    importlib.reload(script_csv)
    script_csv.main() #calling script_csv fille


if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  main = MainWindow()
  main.show()
  sys.exit(app.exec_())
