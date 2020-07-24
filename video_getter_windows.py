import time
import sys
if 'win' in sys.platform:
    print("using windows platform")
    from screen_recorder_sdk import screen_recorder
#%%


def retrieveVideoInWindows(save_path):
    screen_recorder.enable_dev_log ()
    screen_recorder.init_resources ()
    screen_recorder.start_video_recording (save_path)
    time.sleep (5)
    screen_recorder.stop_video_recording ()
    screen_recorder.start_video_recording ('dummy_video.mp4')
    time.sleep (1)
    screen_recorder.stop_video_recording ()
    screen_recorder.free_resources ()
    
    
    
#%%
retrieveVideoInWindows('C:/Users/win/Desktop/vid_test/init_video.mp4')

