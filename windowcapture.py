import numpy as np
import win32gui, win32ui, win32con


class WindowCapture:

    # properties
    w = 0
    h = 0
    hwnd = None
    offset_x = 0
    offset_y = 0

    # constructor
    def __init__(self, window_name):

        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        # get the window size
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]


    def get_screenshot(self):

        # https://stackoverflow.com/questions/3586046/fastest-way-to-take-a-screenshot-with-python-on-windows
        wDC = win32gui.GetWindowDC(self.hwnd) # returns a handle
        dcObj = win32ui.CreateDCFromHandle(wDC) # create new device context object
        cDC = dcObj.CreateCompatibleDC()

        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.offset_x, self.offset_y), win32con.SRCCOPY)

        # convert into a format opencv can read
        dataBitMap.SaveBitmapFile(cDC, 'result.png')
        bitsArray = dataBitMap.GetBitmapBits(True)

        # faster to create an array from a string than from a tuple
        img = np.fromstring(bitsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # idk
        img = img[...,:3]

        img = np.ascontiguousarray(img)

        return img
