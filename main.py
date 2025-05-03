import cv2
import numpy as np
import mss
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

template = cv2.imread(r'D:\Projects\Ipl Ad Mute\ipl_logo.jpg',0)
if template is None:
    print("Error Logo not found")
    exit()
w,h = template.shape[::-1]

monitor = {'top':0, 'left': 0, 'width':200, 'height' : 200 }

def is_logo_present(screenshot):
    gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
    res1 = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.65
    loc1 = np.where(res1 >= threshold)
    return len(loc1[0])>0

def mute():
    volume.SetMute(1, None)
    time.sleep(0.5)

def unmute():
    volume.SetMute(0, None)
    time.sleep(0.5)

with mss.mss() as sct:
    while True:
        sct_img = np.array(sct.grab(monitor))
        if is_logo_present(sct_img):
            print('Logo Found - Unmuting')
            unmute()
        else:
            print('Logo missing')
            mute()
        time.sleep(1)

