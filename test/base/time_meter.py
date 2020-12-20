#! usr/bin/python
# -*- coding:utf-8 -*-

import time

__all__ = ['runtime']


class runtime:  # 计时器
    startTime = 0

    def __init__(self):
        self.startTime = time.time()

    def resetTime(self, T=None):
        print('resetTime')
        self.startTime = T or time.time()

    def setcheckTime(self, T):  # T单位为秒
        self.Time = T

    def checkTime(self, bool=None):
        if self.startTime + self.Time < time.time():
            if bool:
                self.resetTime()
                return True
            return True
        else:
            return False

    def cmpTime(self):
        diff = time.time() - self.startTime
        print('Interval time:%.4f /s' % diff)
        return diff
