import time
import sys
import logging
from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui as auto
import pynput
import pandas as pd
from Parameters import Parameters
from pynput.mouse import Button, Controller
import os, shutil
if sys.platform in ['Windows', 'win32', 'cygwin']:
    import wmi
    import pywintypes

def setupLogger(parser):
    options = parser.parse_args()
    levels = {'critical': logging.CRITICAL,'error': logging.ERROR,'warn': logging.WARNING,'warning': logging.WARNING,'info': logging.INFO,'debug': logging.DEBUG}
    level = levels.get(options.log.lower())
    log = logging.getLogger() # 'root' Logger
    console = logging.StreamHandler()
    format_str = '%(asctime)s\t%(levelname)s -- %(processName)s %(filename)s:%(lineno)s -- %(message)s'
    console.setFormatter(logging.Formatter(format_str))
    log.addHandler(console) # prints to console.
    log.setLevel(level)
    return log

def deleteAllFilesInsideFolder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def CustomException(error_string):
    # importing the pyttsx library
    import pyttsx3

    # initialisation
    engine = pyttsx3.init()

    # testing
    engine.say("Hi, Error occured in automator app")
    engine.say(error_string)
    engine.runAndWait()
    NewException(error_string)
class NewException(Exception):
    pass


def searchImageFromScreenshot(stream, img_path):
    """
    returns me the coordinates of the the centre of the found image

    (3149, 16)
    3174.0 41.0
    """
    print("insdie searchImageFromScreenshot")
    threshold = 0.8
    template = cv2.imread(img_path,0)
    im_color = stream.read()
    print(im_color.shape)
    im = cv2.cvtColor(im_color,cv2.COLOR_BGR2GRAY)
    im  = im.astype(np.uint8)
    w,h = template.shape[:2]

    res = cv2.matchTemplate(im,template,cv2.TM_CCOEFF_NORMED)
    if np.max(res)>threshold:
        loc = np.where(res == np.max(res))
    else:
        return None,None

    for pt in zip(*loc[::-1]):
        point = pt

    screenshot_h,screenshot_w,_ = im_color.shape
    mouse_screen_w,mouse_screen_h = auto.size()
    x= point[0]+w/2
    y = point[1]+h/2
    # 3173.5 25.0
    x = int(x*mouse_screen_w/screenshot_w)
    y = int(y*mouse_screen_h/screenshot_h)
    return x,y


def checkIfPointInside(point,bbox):
    """
    point: (x,y)
    bbox: [x1,y1,x2,y2]
    return if point is inisde bbox
    """
    xin,yin = point
    x1,y1,x2,y2 = bbox
    if x>x1 and x<x2 and y>y1 and y<y2:
        return True
    return False

def cropAroundPoint(screenshot, w, h, pixel_size,SAVE_PATH):
    """
    returns the image of pixel_size*pixel_size  surrounding the cursor
    w = x coordinates
    h = y coordinates
    """
    half_length = int(pixel_size/2)
    screenshot_h,screenshot_w,_ = screenshot.shape
    mouse_screen_w,mouse_screen_h = auto.size()
    print(w,h)
    # mouse = Controller()
    # w,h = mouse.position #  position of mouse
    w = int(w*screenshot_w/mouse_screen_w)
    h = int(h*screenshot_h/mouse_screen_h)
    heightup = h-half_length
    heightdown = h+half_length
    wleft = w-half_length
    wright = w+half_length
    if(heightup<0):
        heightup=0
    if(heightdown>screenshot_h):
        heightdown = screenshot_h
    if(wleft<0):
        wleft=0
    if(wright>screenshot_w):
        wright = screenshot_w
    print("wleft,wright,heightup,heightdown",wleft,"",wright,"",heightup,"",heightdown)
    print(w,h)
    cv2.imwrite(SAVE_PATH, screenshot[heightup:heightdown, wleft:wright])
    return

def getActiveWindow(sleep_time=0):
    """
    Get the currently active window.

    Arguments:
    sleep_time: int:- initial sleep time of function
    Returns
    -------
    active_software_name: String-: Name of the currently active software.
    active_window_name: String-: Name of the currently active window.
    active_window_bbox: [x1,y1,x2,y2]-:  (x1,y2) ->top left point, (x2,y2)-> bottom right point of active window.
    """
    time.sleep(sleep_time)
    active_software_name = None
    active_window_name = None
    active_window_bbox = None

    if sys.platform in ['linux', 'linux2']:
        raise CustomException("sys.platform={platform} is unknown. Please report.".format(platform=sys.platform))

        # Alternatives: http://unix.stackexchange.com/q/38867/4784
        try:
            import wnck
        except ImportError:
            wnck = None
        if wnck is not None:
            screen = wnck.screen_get_default()
            screen.force_update()
            window = screen.get_active_window()
            if window is not None:
                pid = window.get_pid()
                with open("/proc/{pid}/cmdline".format(pid=pid)) as f:
                    active_window_name = f.read()
        else:
            try:
                from gi.repository import Gtk, Wnck
                gi = "Installed"
            except ImportError:
                logging.info("gi.repository not installed")
                gi = None
            if gi is not None:
                Gtk.init([])  # necessary if not using a Gtk.main() loop
                screen = Wnck.Screen.get_default()
                screen.force_update()  # recommended per Wnck documentation
                active_window = screen.get_active_window()
                pid = active_window.get_pid()
                with open("/proc/{pid}/cmdline".format(pid=pid)) as f:
                    active_window_name = f.read()

    elif sys.platform in ['Windows', 'win32', 'cygwin']:
        # http://stackoverflow.com/a/608814/562769,https://stackoverflow.com/questions/14394513/win32gui-get-the-current-active-application-name
        import win32gui
        import win32process
         # pip install wmi
        import pythoncom
        pythoncom.CoInitialize()

        def get_app_name(hwnd):
            c = wmi.WMI()
            """Get applicatin filename given hwnd."""
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                for p in c.query('SELECT Name FROM Win32_Process WHERE ProcessId = %s' % str(pid)):
                    exe = p.Name
                    break
                return exe

            except:
                return None



        window = win32gui.GetForegroundWindow()
        active_software_name = get_app_name(window)

        try:
           active_window_bbox = win32gui.GetWindowRect(window)
        except pywintypes.error:
            print("1400, invalid window handle")
            active_window_bbox = None
        active_window_name = win32gui.GetWindowText(window)
#        window = win32gui.GetForegroundWindow()
#        active_software_name = get_app_name(window)
#        active_window_bbox = win32gui.GetWindowRect(window)
#        active_window_name = win32gui.GetWindowText(window)

    elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
        # http://stackoverflow.com/a/373310/562769
        from AppKit import NSWorkspace
        from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

        curr_app = NSWorkspace.sharedWorkspace().frontmostApplication()
        curr_pid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']
        curr_app_name = curr_app.localizedName()
        options = kCGWindowListOptionOnScreenOnly
        windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
        for window in windowList:
            pid = window['kCGWindowOwnerPID']
            windowNumber = window['kCGWindowNumber']
            ownerName = window['kCGWindowOwnerName']
            geometry = window['kCGWindowBounds']
            windowTitle = window.get('kCGWindowName', u'Unknown')
            if curr_pid == pid:
                # print("%s - %s (PID: %d, WID: %d): %s" % (ownerName, windowTitle.encode('ascii','ignore'), pid, windowNumber, geometry))
                active_software_name = ownerName
                active_window_name = windowTitle.encode('ascii','ignore')
                active_window_bbox   = [geometry['X'], geometry['Y'], geometry['X']+geometry['Width'], geometry['Y']+geometry['Height']]

    else:
        raise CustomException("sys.platform={platform} is unknown. Please report.".format(platform=sys.platform))

    print("Active software name: %s" % str(active_software_name))
    print("Active window name: %s" % str(active_window_name))
    print("Active window bbox: ", active_window_bbox)

    return active_software_name, active_window_name, active_window_bbox

def searchImageFromScreenshotForNSeconds(stream,img_path,N) :
    time_start = time.time()
    count=0
    while True:
        print(count)
        count+=1
        if(time.time()-time_start>N):
            break
        x,y = searchImageFromScreenshot(stream,img_path)
        if x is None and y is None:
            continue
        else:
            print(x,y)
            return x,y
    raise CustomException("Error: Image: ", img_path, " not found")

def searchAppNameForNSeconds(active_software_name_csv, N):
    print("inside searchAppNameForNSeconds")
    time_start = time.time()
    count=0
    while True:
        print(count)
        count+=1
        if(time.time()-time_start>N):
            break
        active_software_name, active_window_name, active_window_bbox = getActiveWindow(sleep_time = 0.2)
        if active_software_name!=active_software_name_csv:
            continue
        else:
            return
    raise CustomException("Error: actual: " + str(active_software_name_csv) + " but getting " + str(active_software_name) )
