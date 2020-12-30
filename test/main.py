import uiautomator2 as u2
import time
import timeit

'''
pip3.8 install opencv-contrib-python -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
'''

import numpy as np
import cv2
#

imgData = np.fromfile('script.raw', dtype=np.uint8)
imgData = imgData[slice(12,len(imgData))]
imgData = imgData.reshape(720, 1280, 4)

'''
    imgData范围截取
    imgData[100:720-200, 100:1280-100]
    imgData[y:y+长, x:x+宽
'''
print(imgData[:200+1,100+1:200+1])

# _DEVICE_ID = "emulator-5562"
# #_DEVICE_ID = "127.0.0.1:5555"
# driver = u2.connect(_DEVICE_ID)
#
# print(driver.screen.getRGB(100, 150))
# time.sleep(2)
#
# print(driver.screen.getRGB(100, 150))