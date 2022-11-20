import cv2
import numpy
import pyautogui
from time import time
from PIL import ImageGrab

res = pyautogui.locateCenterOnScreen("global.png")
print(res)

while(True):
    ss = ImageGrab.grab()
    ss = numpy.array(ss)
    ss = cv2.cvtColor(ss, cv2.COLOR_RGB2BGR)
    cv2.imshow('Snippet', ss)
    if cv2.waitKey(1) == ord('q'):
    	cv2.destroyAllWindows()
print('Done')