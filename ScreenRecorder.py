import time
import sys
if 'win' in sys.platform:
    print("using windows platform for screen recording")
    from screen_recorder_sdk import screen_recorder

class ScreenRecorder:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """
    
    def __init__(self):
        self.stopped = False

    def start(self):
        screen_recorder.enable_dev_log ()
        screen_recorder.init_resources ()
        screen_recorder.start_video_recording("screen_video.mp4")
        print("started video recording")
    def stop(self):
        screen_recorder.stop_video_recording()
        screen_recorder.start_video_recording(".dummy_video.mp4")
        time.sleep(1)
        screen_recorder.stop_video_recording()
        screen_recorder.free_resources()
        print("stopped video recording")

if __name__ == "__main__":
    screenRecorder = ScreenRecorder()
    screenRecorder.start()
    time.sleep(5)
    screenRecorder.stop()
