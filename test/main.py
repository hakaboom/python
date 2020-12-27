import uiautomator2 as u2
import re
import time
from pyminitouch import MNTDevice
from pyminitouch import safe_connection
from pyminitouch import CommandBuilder

_DEVICE_ID = "emulator-5554"
_DEVICE_ID = "127.0.0.1:5555"
driver = u2.connect(_DEVICE_ID)
driver.touch1.down(520,230,1)
driver.touch1.down(800,230,2)
time.sleep(1)
# driver.touch1.up(520,230,1)
# driver.touch1.up(650,230,2)
class system:
    def __init__(self):
        global driver
        self.driver = driver

    def runApp(self,appPackage,appActivity=None):
        self.driver.app_start(appPackage,appActivity)

    def isAppRunning(self,appPackage):
        try:
            return self.driver.app_list_running().index(appPackage) != None
        except:
            print('App is not running')
            return False

    def getForegroundApp(self):
        return driver.app_current()['package']

    def killApp(self,appPackage):
        self.driver.app_stop(appPackage)

    def setClipboard(self,text):
        self.driver.set_clipboard(text)

    def getClipboard(self):
        return self.driver.clipboard

    def getSystemInfo(self):
        return self.driver.info

class touch:
    def __init__(self):
        global driver
        self.driver = driver


    def click(self,x,y,index=1):
        self.clickIndex[index].press(x,y)

class screen:
    pass





'''

[     147.083927] /dev/input/event4: 0003 002f 00000000
[     147.083927] /dev/input/event4: 0003 0039 0000000e
[     147.083927] /dev/input/event4: 0001 014a 00000001
[     147.083927] /dev/input/event4: 0003 0035 00001e62
[     147.083927] /dev/input/event4: 0003 0036 00001a02
[     147.083927] /dev/input/event4: 0000 0000 00000000
[     147.983737] /dev/input/event4: 0003 002f 00000001
[     147.983737] /dev/input/event4: 0003 0039 0000000f
[     147.983737] /dev/input/event4: 0003 0035 000025d6
[     147.983737] /dev/input/event4: 0003 0036 00001a2e
[     147.983737] /dev/input/event4: 0000 0000 00000000
[     151.152794] /dev/input/event4: 0003 002f 00000000
[     151.152794] /dev/input/event4: 0003 0039 ffffffff
[     151.152794] /dev/input/event4: 0000 0000 00000000
[     154.657181] /dev/input/event4: 0003 002f 00000001
[     154.657181] /dev/input/event4: 0003 0039 ffffffff
[     154.657181] /dev/input/event4: 0001 014a 00000000
[     154.657181] /dev/input/event4: 0000 0000 00000000

'''