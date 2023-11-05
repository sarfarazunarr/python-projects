import cv2
import numpy as np 
import pyautogui

import win32gui
import win32con
import time
from os import mkdir

try:
    mkdir('recordings')

except FileExistsError:
    pass

def minimizedWindow():
    window = win32gui.FindWindow(None, 'Screen Recorder')
    win32gui.ShowWindow(window, win32con.SW_MINIMIZE)

SCREEN_SIZE= (1366, 768)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('recordings/'+"Screen Recording"+ time.strftime("%H-%M-%S %d-$m-$y") + ".mp4", fourcc, 20.0, (SCREEN_SIZE))
print('Recording Started... \nwindow minimized in taskbar. \npress q to exit')

minimized = False
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    cv2.imshow('Screen Recorder', frame)
    if minimized == True:
        pass
    else:
        minimized = True
        minimizedWindow()
        
    output.write(frame)

    if cv2.waitKey(1) == ord('q'):
        print('\r Finished Recording')
        break
output.release()
cv2.destroyAllWindows()
