#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from test_UI.common.base_page import BasePage
from test_UI.page_locators.home_page_locator import HomePageLocator as loc
from time import sleep
import re
class HomePage(BasePage):

    def check_nick_name_exists(self):
        """
        :return: 存在返回True,不存在返回False
        """
        #// a[text() = "关于我们"]
        #1)先确定 1到了这个页面
        self.wait_eleVisble(loc.About_US_loc,'主页“关于我们”')
        sleep(0.5)
        #2）1.成立  再判断2. 是否存在
        return True

    # 点击投标按钮
    def click_invest_button(self):
        self.wait_eleVisble(loc.invest_button_loc,'首页点击投标')
        self.click_element(loc.invest_button_loc,'首页点击投标')

    #点击个人中心
    def click_user_center(self):
        self.wait_eleVisble(loc.user_center_loc,'首页点击个人中心')
        self.click_element(loc.user_center_loc,'首页点击个人中心')

    #点击首页
    def click_home_back(self):
        self.wait_eleVisble(loc.home_page_loc, '首页点击首页')
        self.click_element(loc.home_page_loc, '首页点击首页')

    #首页 剩余可投 标的 金额    ps:剩余：64.86万
    def get_bid_left_money(self):
        self.wait_eleVisble(loc.bid_money_loc,'首页获取可投标金额')
        bid_money = self.get_element_text(loc.bid_money_loc,'首页获取可投标金额')
        num =re.search("\d+\.?\d*",bid_money)
        if bid_money[-1] == "万":
            return float(num.group(0))*10000
        else:
            int(num.group(0))
if __name__ == '__main__':
   pass