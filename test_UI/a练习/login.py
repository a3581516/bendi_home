#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
print(time.ctime())            #current time
#输出格式化当前日期时间  strftime：string format time
print(time.strftime("%Y-%m-%d %H:%M:%S"))
#EC.presence_of_element_located    #元素存在
#EC.visibility_of_element_located  #元素可见
#EC.element_to_be_clickable  #元素可点击
#EC.element_to_be_selected  #下拉框
class Login:
    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get(url)

    def is_element_visibility(self,path):
        '''
        判断元素是否存在并可见，
        :param path: 参数为 Xpath 路径
        :return: 返回 找到这个元素的 对象，便利后续操作 使用
       '''
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator=(By.XPATH, path)))
        except Exception as e:
            raise e
        else:
            return self.driver.find_element(By.XPATH, path)
    def is_elements_visibility(self,path):
        '''
        判断元素是否存在并可见，
        :param path: 参数为 Xpath 路径
        :return: 返回 找到这个元素的 对象，便利后续操作 使用
       '''
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(locator=(By.XPATH, path)))
        except Exception as e:
            raise e
        else:
            return self.driver.find_elements(By.XPATH, path)