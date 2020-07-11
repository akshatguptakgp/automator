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
from Parameters import Parameters

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

    # Reload params
    Parameters().getScreensize()


  def recordingButtonPressed(self):
    log.debug("recordingButtonPressed clicked")

    # toggling start and stop buttons
    if self.ui.recordingButton.text() == "Start":
        if not os.path.isdir("saved_snips_for_cliks"):
            os.mkdir("saved_snips_for_cliks")
        utils.deleteAllFilesInsideFolder("saved_snips_for_cliks")
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
#    import script_csv
#    importlib.reload(script_csv)
#    script_csv.main() #calling script_csv fille
    os.system("python script_csv.py")

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  main = MainWindow()
  main.show()
  sys.exit(app.exec_())
