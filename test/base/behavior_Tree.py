#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from inspect import isfunction
import time

def none(_=None):
    pass

class Blackboard:

    def __init__(self):
        self._tag = 'Blackboard'
        self.con = {}

    def setValue(self, Member, Value):
        self.con[Member] = Value

    def getValue(self, Member, DefaultValue=None):
        return self.con.get(Member, DefaultValue)

    def setValueBath(self, Value):
        for k, v in Value.items():
            self.con[k] = v

    def getAllValue(self, Target=None):
        Target = Target or self
        return Target.con

    def createScene(self):
        return Scene(self)

    def createSequence(self):
        return Sequence(self)

class Behavior:

    def __init__(self, Parent):
        self._tag = 'Behavior'
        self.parent = Parent
        self.blackboard = Parent.blackboard
        self.triggerOnDelay = Trigger(Parent.blackboard)
        self.server=none

    def setTrigger(self):
        pass

    def setServer(self,serverFunction=None):
        if isfunction(serverFunction) or type(serverFunction).__name__ == 'method':
            self.server = serverFunction

    def run(self):
        self.setTrigger()
        self.server(None)

class Scene:
    # '''创建场景'''
    def __init__(self, Blackboard):
        self._tag = 'Scene'
        self.blackboard = Blackboard
        self.startTrigger = Trigger(Blackboard)
        self.endTrigger = Trigger(Blackboard)
        self.startingBehavior = Behavior(self)
        self.doingBehavior = Behavior(self)
        self.endingBehavior = Behavior(self)

    def getStartingBehavior(self):
        return self.startingBehavior

    def getEndingBehavior(self):
        return self.endingBehavior

    def getDoingBehavior(self):
        return self.doingBehavior

    def getStartTrigger(self):
        return self.startTrigger

    def getendTrigger(self):
        return self.endTrigger

    def addSequence(self,Sequence):
        if hasattr(Sequence,'_tag') and Sequence._tag == 'Sequence':
            self.child = Sequence

    def run(self):
        if self.startTrigger.check():
            self.startingBehavior.run()
            if not self.endTrigger.check():
                self.doingBehavior.run()
            self.endingBehavior.run()
            if hasattr(self,'child') and self.child._tag == 'Sequence':
                self.child.run()
            return True
        return False

class Trigger:
    # '''触发器'''
    def __init__(self, Blackboard=None):
        self._tag = 'Trigger'
        self.blackboard = Blackboard
        self.rule = none

    def setRule(self, RuleFunction):
        if isfunction(RuleFunction) or type(RuleFunction).__name__ == 'method':
            self.rule = RuleFunction

    def check(self):
        if hasattr(self,'blackboard'):
            return self.rule(self.blackboard)
        return self.rule(None)

class Sequence:

    def __init__(self,Blackboard=None):
        self._tag = 'Sequence'
        self.scenes = []
        self.isLoop = False
        self.maxCount = -1
        self.maxTime = -1
        self.loopIntervalTime = 0
        self.LoopEndTrigger = Trigger(Blackboard)

    def addScene(self, Scene):
        if hasattr(Scene,'_tag') and Scene._tag == 'Scene':
            self.scenes.append(Scene)

    def run(self):
        flag = False
        loopTime = time.time()
        loopCount = 1
        while True:
            if flag:
                loopTime = time.time()
                loopCount = 0
            for v in self.scenes:
                flag = v.run()
                if flag:
                    break
            if self.LoopEndTrigger.check():
                break
            loopCount = loopCount + 1
            if self.loopIntervalTime > 0:
                time.sleep(self.loopIntervalTime)
            if (not flag and not self.isLoop) or ((self.isLoop and not flag) and (not self.maxTime==-1 and (loopTime + self.maxTime < time.time()) or False) or (not self.maxCount == -1 and (loopCount > self.maxCount) or False)):
                return

    def getLoopEndTrigger(self):
        return self.LoopEndTrigger

    def setLoop(self, isLoop, LoopCount=-1, LoopTime=-1, IntervalTime=0):
        '''
            设置场景检测的循环方式
            参数:	isLoop		Bool型,是否循环
                    LoopCount 	循环次数
                    LoopTime 	循环最长时间
                    IntervalTime每次循环的间隔(毫秒)
        '''
        self.isLoop = isLoop
        self.maxCount = LoopCount
        self.maxTime = LoopTime
        self.loopIntervalTime = IntervalTime

#测试例子
'''
from selenium import webdriver
from base.behavior_Tree import Sequence
from base.behavior_Tree import Blackboard
import time
Driver = webdriver.Chrome()

Main = Blackboard()
Main.setValueBath({
    '当前流程' : '登陆系统',
    'driver' : Driver,
})
start_up = Sequence()
start_up.setLoop(True,-1,-1,1)
start_up_suc = Main.createScene()
start_up_err = Main.createScene()
start_up.addScene(start_up_err)
start_up.addScene(start_up_suc)
class c_start_up:
    global Main
    url = 'https://www.jd.com/'
    driver = Main.getValue('driver')
    def checkURL_err(self,_):
        if self.driver.current_url != self.url:
            return True
        return False

    def checkURL_suc(self,_):
        if self.driver.current_url == self.url:
            return True
        return False

    def getURL(self,blackboard):
        self.driver.get(self.url)

    def suc(self,blackboard):
        print('suc')
start_up_rule = c_start_up()
start_up_suc.getStartTrigger().setRule(start_up_rule.checkURL_suc)
start_up_err.getStartTrigger().setRule(start_up_rule.checkURL_err)
start_up_suc.getDoingBehavior().setServer(start_up_rule.suc)
start_up_err.getDoingBehavior().setServer(start_up_rule.getURL)

start_up.run()
'''