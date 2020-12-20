#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from base.time_meter import runtime
import time

def isElementExist(self,type,name):
    """'type ['id','name','xpath','link_text','link_text','tag_name','class_name','css_selector']'"""
    try:
        getattr(self,'find_element_by_'+type)(name)
        return True
    except:
        return False
class JDBUY:

    def __init__(self,buy_time):
        self.runTime = runtime()
        self.runTime.setcheckTime(2)
        self.buy_time=int(time.mktime(time.strptime(buy_time,"%Y-%m-%d %H:%M:%S")))
        self.driver = webdriver.Chrome()

    def login_jd(self):
        while True:
            '''检测登录'''
            if isElementExist(self.driver,'class_name','link-login'):
                print('未登录')
            else:
                if isElementExist(self.driver,'class_name','nickname'):
                   print('已登录')
                   return True
                else:
                    print('未知错误')
            time.sleep(3)

    def toCart(self):
        self.driver.get("https://cart.jd.com/cart_index/")

    def inCart(self):
        return self.driver.current_url == 'https://cart.jd.com/cart_index/#none'

    def inTrade(self):
       return self.driver.current_url == 'https://trade.jd.com/shopping/order/getOrderInfo.action'

    def selectAllCart(self):
        time.sleep(1)
        if isElementExist(self.driver,'name','select-all'):
            checkbox = self.driver.find_element_by_name('select-all')
            '''
                'pageclick|keycount|Shopcart_CheckAll|0'    --没全选
                'pageclick|keycount|Shopcart_CheckAll|1'    --已全选
            '''
            if checkbox.get_attribute('clstag')=='pageclick|keycount|Shopcart_CheckAll|1':
                print('购物车已全选')
                self.subimit_with_retry()
                return True
            else:
                print('购物车未全选')
                checkbox.click()
        if self.inTrade():
            print('已进入提交页面')
            self.buying()

    def subimit_with_retry(self):
        '''去结算'''
        if isElementExist(self.driver,'class_name','btn-area'):
            subimitBtn = self.driver.find_element_by_class_name('btn-area')
            subimitBtn.click()

    def checkSubimit(self):
        '''
            页面里如果存在'请至少选中一件商品！' 说明抢购未开始
            如果跳转到结算页面'https://trade.jd.com/shopping/order/getOrderInfo.action'说明提交成功
        '''
        print('checkSubimit')
        if isElementExist(self.driver,'link-text','请至少选中一件商品！'):
            self.driver.find_element_by_class_name('dialog-close dialog-close-notitle').click()
            print('抢购未开始')
        if self.inTrade():
            print('已进入提交页面')
            self.buying()

    def buying(self):
        self.driver.find_element_by_id('order-submit').click()

    def wait(self):
        print('wait')
        while True:
            nowTime = time.time()
            if time.time()+60<=self.buy_time:
                self.driver.refresh()
                print('刷新页面,防止登录超时')
                time.sleep(10)
            else:
                '''即将开始抢购'''
                self.selectAllCart()

'''
    下次需要重新写,checkSubimit主要判断页面是否在结算或购物车,wait里判断购物车
'''

jd = JDBUY('2020-12-17 23:17:00')
jd.toCart()
jd.login_jd()
jd.toCart()
while True:
    jd.checkSubimit()
    jd.wait()

