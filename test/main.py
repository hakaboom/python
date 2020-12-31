import logging
import uiautomator2 as u2
import numpy as np
import cv2
from base.script import *
'''
pip3.8 install opencv-contrib-python -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
'''

# img = cv2.imread('img_bmp.bmp',0)
# edges = cv2.Canny(img, 30, 70)
# cv2.imshow('canny', np.hstack((img, edges)))
# cv2.waitKey(0)
'''
    imgData范围截取
    imgData[100:720-200, 100:1280-100]
    imgData[y:y+长, x:x+宽
    print(imgData[:200+1,100+1:200+1])
    
    imgData = np.fromfile('script.raw', dtype=np.uint8)
    imgData = imgData[slice(12,len(imgData))]
    imgData = imgData.reshape(720, 1280, 4)
    imgData = imgData[:,:,::-1][:,:,1:4] #imgData中rgbA转为Abgr,并截取bgr
    cv2.imwrite('img_bmp.bmp',imgData)
'''



# _DEVICE_ID = "emulator-5562"
# #_DEVICE_ID = "127.0.0.1:5555"
# driver = u2.connect(_DEVICE_ID)
#
# print(driver.screen.getRGB(100, 150))
# time.sleep(2)
#
# print(driver.screen.getRGB(100, 150))