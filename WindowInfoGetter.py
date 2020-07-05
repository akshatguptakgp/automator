from threading import Thread
import time
import numpy as np
from queue import Queue
import utils

class WindowInfoGetter:
    """
    Class that give the active information of the running app.
    """


    def __init__(self):
        self.stopped = False
        self.info = utils.getActiveWindow()
        self.info_list = []

    def start(self):
        Thread(target=self.get, args=(), daemon=True).start()
        return self

    def get(self):
        while not self.stopped:
            st_time = time.time()
            self.info = utils.getActiveWindow()
            self.info_list.append([time.time(), self.info])
            time.sleep(0.01)
            if len(self.info_list)%200:
                print("grab time taken: ", time.time()-st_time)

    def stop(self):
        self.stopped = True
        
#windowInfoGetter = WindowInfoGetter()
#windowInfoGetter.start()
#time.sleep(10)
#windowInfoGetter.stop()



