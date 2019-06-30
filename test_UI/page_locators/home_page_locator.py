#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

# 用户名输入框
class HomePageLocator:
    # // a[text() = "关于我们"]
    About_US_loc =  (By.XPATH,'// a[text() = "关于我们"]')
    #投标按钮
    invest_button_loc = (By.XPATH, '//div[2]//span[@class="fs-22"]')
    #个人中心
    user_center_loc = (By.XPATH, '//div [@class="right fs-12"]/span[3]/a')
    #首页
    home_page_loc = (By.XPATH,'//div [@class="navlist clearfix fs-18"]//a[text()="首页"]')
    #可投标金额
    bid_money_loc = (By.XPATH, '//div[@class="surplus_much"]')
