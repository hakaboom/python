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
