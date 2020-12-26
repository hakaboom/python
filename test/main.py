import uiautomator2 as u2


_DEVICE_ID = "emulator-5562"
driver = u2.connect(_DEVICE_ID)

driver.touch.down(100,100)
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

system = system()
