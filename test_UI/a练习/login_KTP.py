#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#EC.presence_of_element_located    #元素存在
#EC.visibility_of_element_located  #元素可见
#EC.element_to_be_clickable  #元素可点击
#EC.element_to_be_selected  #下拉框

class LoginKTP:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        
    def login(self):

        self.driver.get('https://www.ketangpai.com/')
        #点击右上角登录
        self.driver.find_element_by_xpath('//div[@id="indextop"]//div[@class="log-reg fr"]//a[@class="login"]').click()
        #选择账号登录
        self.driver.find_element_by_xpath('//div[@id="login"]//div[@class="title items"]//a[@class="active"and contains(text(),"账号登录")]').click()
        
        #输入
        self.driver.find_element_by_xpath('//div[@id="login"]//div[@class="title items"]/following-sibling::div//div//input[@name="account"]').send_keys('xxx')
        self.driver.find_element_by_xpath('//div[@id="login"]//div[@class="title items"]/following-sibling::div//div//input[@name="pass"]').send_keys('xxx')
        self.driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]//a[text()="登录"]').click()
        #关闭弹窗
        self.driver.find_element_by_xpath('//*[@id="notice-pop"]/div[1]/a').click()
        
        sleep(1)
        #title15期
        self.driver.find_element_by_xpath('//div[@class="empty-box hide"]/parent::div/div/following-sibling::div//strong/a[contains(text(),"15期")]').click()
        #点击评论第一个 进入
        self.driver.find_element_by_xpath('//div[@class="announce-cont clearfix"]/following-sibling::div//a').click()
        #添加评论
        self.driver.find_element_by_xpath('//div[@id="viewer-discuss"]//div[@class="img"]/following-sibling::p[text()="添加评论"]').click()
        #输入评论
        self.driver.find_element_by_xpath('//div[@id="viewer-discuss"]//div[@class="add-comment"]//div[@class="input fr"]//textarea[@class="comment-txt"]').send_keys('hello word!')
        #点击确定
        self.driver.find_element_by_xpath('//div[@class="sc-box fl"]/ancestor::div[@class="opt-cont"]//div[@class="opt-btn fr"]//a[text()="确定"]').click()
        
        #移动到我的评论
        # weizhi = self.driver.find_element_by_xpath('//ul[@class="comment-list"]//span[text()="深圳一灰灰"]/ancestor::div//p[text()="hello word!"]')
        # ActionChains(self.driver).move_to_element(weizhi).perform()

        if self.is_element_visibility('//ul[@class="comment-list"]//span[text()="深圳一灰灰"]/ancestor::div//p[text()="hello word!"]/parent::div//a[@title="删除"]'):
        
            #点击删除
            self.driver.find_element_by_xpath('//ul[@class="comment-list"]//span[text()="深圳一灰灰"]/ancestor::div//p[text()="hello word!"]/parent::div//a[@title="删除"]').click()
        sleep(5)
        # self.driver.switch_to_alert().accept()
        # self.driver.switch_to_frame()

        if self.is_element_present('id','//div[@id="layui-layer1"]//div//a[@class="layui-layer-btn0 active"]'):
            self.driver.find_element_by_id('//div[@id="layui-layer1"]//div//a[@class="layui-layer-btn0 active"]').click()
        ##弹框点击确认
        # self.driver.find_element_by_xpath('//div[@class="layui-layer-btn"]//a[@class="layui-layer-btn0 active"]').click()


    def is_element_visibility(self,path):

         return  WebDriverWait(self.driver,30,2).until(EC.visibility_of_element_located(locator=(By.XPATH,path)))
    
    def is_element_present(self,by,value):#是否存在
        try:
            self.driver.find_element(by=by,value=value)
        except EC.NoSuchElementException as e:
            return False
        return True

    def is_alter_present(self):
        try:
            self.driver.switch_to.alert
        except EC.NoAlertPresentException as e:
            return False
        return True

if __name__ == '__main__':
    a =  LoginKTP()
    a.login()