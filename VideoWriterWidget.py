"""

ln -s /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/Tk.framework/Versions/8.5/Headers/X11 /usr/local/include/X11

pip3 install mss

from mss import mss
import time

st_time = time.time()
with mss() as sct:
    for i in range(1000):
        sct.shot()
        print("mss.screenshot() time taken: ", (time.time()-st_time)/(i+1))

"""

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
        self.frame = self.grab_screen()
        self.frame_queue = Queue(maxsize = 20)

    def grab_screen(self):
        st_time = time.time()
        frame = self.stream.read()
        # print("pyautogui.screenshot() time taken: ", time.time()-st_time)
        # img = pyautogui.screenshot()
        # frame = np.array(img)
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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

class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False
        self.codec = cv2.VideoWriter_fourcc('M','J','P','G')
        self.video_file_name = "recording.avi"
        self.frame_width = frame.shape[1]
        self.frame_height = frame.shape[0]
        print(self.frame_width, self.frame_height)
        self.output_video = cv2.VideoWriter(self.video_file_name, self.codec, 30, (self.frame_width, self.frame_height))
        self.counter = 0
    def start(self):
        Thread(target=self.show, args=()).start()
        return self

    def show(self):
        print("inside show")
        while not self.stopped:
            # cv2.imshow("Video", self.frame)
            print("saving_video")
            st_time = time.time()
            self.output_video.write(self.frame)
            print("save time taken: ", time.time()-st_time)
            self.counter += 1
            print("write counter: ",self.counter)
            if cv2.waitKey(1) == ord("q"):
                self.stopped = True

    def stop(self):
        self.stopped = True
        print("stopping")
        time.sleep(1)
        self.output_video.release()

from datetime import datetime

class CountsPerSec:
    """
    Class that tracks the number of occurrences ("counts") of an
    arbitrary event and returns the frequency in occurrences
    (counts) per second. The caller must increment the count.
    """

    def __init__(self):
        self._start_time = None
        self._num_occurrences = 0

    def start(self):
        self._start_time = datetime.now()
        return self

    def increment(self):
        self._num_occurrences += 1

    def countsPerSec(self):
        elapsed_time = (datetime.now() - self._start_time).total_seconds()
        return self._num_occurrences / elapsed_time if elapsed_time > 0 else 0

def putIterationsPerSec(frame, iterations_per_sec):
    """
    Add iterations per second text to lower-left corner of a frame.
    """

    cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
        (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255))
    return frame

def threadBoth():
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = VideoGet().start()
    video_shower = VideoShow(video_getter.frame).start()
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped or video_shower.counter > 100:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame
        frame = putIterationsPerSec(frame, cps.countsPerSec())
        video_shower.frame = frame
        cps.increment()
        # print("cps._num_occurrences: ",cps._num_occurrences)

if __name__ == "__main__":
    threadBoth()
