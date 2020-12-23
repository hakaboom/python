from selenium import webdriver
from base.behavior_Tree import Sequence
from base.behavior_Tree import Blackboard
import time


Main = Blackboard()
Main.setValueBath({
    'count' : 0,
})
start = Sequence()
start.setLoop(True,-1,-1,1)
start_err = Main.createScene()
start_suc = Main.createScene()
start.addScene(start_suc)
start.addScene(start_err)
def suc(_):
    global Main
    count = Main.getValue('count') + 1
    print(count)
    Main.setValue('count',count)
    if count >=5:
        print('suc')
        return True
def err(_):
    pass
start_suc.getStartTrigger().setRule(suc)
start_err.getStartTrigger().setRule(err)



suc_login = Sequence()
suc_login.setLoop(True,3,-1,1)
start_suc.addSequence(suc_login) '''向start_suc增加情景,满足star_suc后会运行suc_login里'''
suc_login_suc = Main.createScene()
suc_login_err = Main.createScene()
suc_login.addScene(suc_login_suc)
suc_login.addScene(suc_login_err)
def suc_login(blackboard):
    print('uc_login')
def err_login(blackboard):
    print('err_login')
suc_login_suc.getStartTrigger().setRule(suc_login)
suc_login_err.getStartTrigger().setRule(err_login)


start.run()