#! usr/bin/python
# -*- coding:utf-8 -*-
from appium import webdriver

class Singleton(object):
    driver = None

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            config = {
                'platformName': 'Android',
                'platformVersion': '7.1.1',
                'deviceName' : '127.0.0.1:5554',
                #'appPackage': 'com.bilibili.princonne',
                #'appActivity': 'com.bilibili.princonne.permission.PermissionActivity',
                'noReset': 'true'
            }
            cls._instance = orig.__new__(cls, *args, **kw)
            cls._instance.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config)
        return cls._instance

class DriverClient(Singleton):
    def getDriver(self):
        return self.driver