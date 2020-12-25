from base.appium_config import DriverClient
from time import sleep
import os
import re

class sceen:
    def __init__(self):
        self.driver = DriverClient().getDriver()
        print(self.driver.current_activity)
    def getSize(self):
        return self.driver.get_window_size()

    def getDPI(self):
        return self.driver.get

class system:
    def __init__(self):
        self.driver = DriverClient().getDriver()
    def runApp(self,appName,appActivity):
        self.driver.start_activity(appName, appActivity)
b=sceen()
print(b.getSize())
b=system()
b.runApp('com.bilibili.priconne', 'com.bilibili.princonne.permission.PermissionActivity')