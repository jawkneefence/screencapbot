import cv2
import numpy
from windowcapture import WindowCapture

wincap = WindowCapture('PokeMMO')

ss = wincap.get_screenshot()

cv2.imshow('Computer Vision', ss)
cv2.waitKey()
print('Done.')