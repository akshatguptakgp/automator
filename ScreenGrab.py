from threading import Thread
import cv2
import time
import numpy as np
from queue import Queue
from vidgear.gears import ScreenGear

class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self):
        self.stopped = False
        self.stream = ScreenGear().start()
        self.frame_queue = Queue(maxsize = 200)

    def grab_screen(self):
        st_time = time.time()
        frame = self.stream.read()
        return frame

    def start(self):
        Thread(target=self.get, args=(), daemon=True).start()
        return self

    def get(self):
        while not self.stopped:
            st_time = time.time()
            self.frame = self.grab_screen()
            if self.frame_queue.full():
                self.frame_queue.get()
            self.frame_queue.put([time.time(), self.frame])
            # print("grab time taken: ", time.time()-st_time)
            time.sleep(0.05)

    def stop(self):
        self.stream.stop()
        self.stopped = True

if __name__ == "__main__":
    video_getter = VideoGet().start()
    time.sleep(5)
    video_getter.stop()
    print(frame_queue)
