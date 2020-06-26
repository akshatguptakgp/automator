import pyautogui
import time

# starting safari browser
time.sleep(1)
pyautogui.hotkey('command', 'space')  # ctrl-c to copy ,The full list of key names is in pyautogui.KEYBOARD_KEYS
pyautogui.typewrite('safari', interval=0.1)  # useful for entering text, newline is Enter
pyautogui.hotkey('enter')
time.sleep(5)

# opening colab website
pyautogui.typewrite('https://colab.research.google.com/drive/1Gr9oWRvH5QnJi23sHIUMsZqRGokGv6nW \n', interval=0.0001)  # useful for entering text, newline is Enter
# pyautogui.hotkey('enter')
# opening colab file
time.sleep(10)
# bbox = pyautogui.locateOnScreen('connect-button.png')  # returns (bbox.left, bbox.top, bbox.width, bbox.height) of first place it is found
# print(bbox)
# pyautogui.click(x=bbox.left, y=bbox.top, clicks=1, interval=1, button='left')
# pyautogui.click(x=1706, y=173, clicks=1, interval=1, button='left')
# time.sleep(5)
pyautogui.click(x=381, y=238, clicks=1, interval=1, button='left') # run mount cell
time.sleep(5)
pyautogui.click(x=834, y=607, clicks=1, interval=1, button='left') # click captcha
time.sleep(40)
pyautogui.click(x=734, y=293, clicks=1, interval=1, button='left')
time.sleep(5)
pyautogui.click(x=861, y=554, clicks=1, interval=1, button='left')
time.sleep(5)
pyautogui.click(x=1098, y=943, clicks=1, interval=1, button='left')
time.sleep(5)
pyautogui.click(x=1158, y=521, clicks=1, interval=1, button='left')
time.sleep(5)
pyautogui.click(x=531, y=73, clicks=1, interval=1, button='left')
time.sleep(5)
pyautogui.click(x=511, y=370, clicks=1, interval=1, button='left')
time.sleep(5)
pyautogui.hotkey('command', 'v')
time.sleep(5)
pyautogui.hotkey('enter')