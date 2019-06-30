#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from test_UI.common.base_page import BasePage
from test_UI.page_locators import user_page_locator as loc
import re

class UserPage(BasePage):

    #查看余额
    def get_user_left_money(self):
        self.wait_eleVisble(loc.left_money,'个人页面获取余额')

        left_money =  self.get_element_text(loc.left_money,'个人页面获取余额')
        num = re.search("\d+\.?\d*", left_money)
        return float(num.group(0))

    #查看交易记录
    def get_business_amount_note(self):
        self.wait_eleVisble(loc.business_note,'个人页面交易记录')

        self.click_element(loc.business_note,'个人页面点击交易记录')
        #默认就取第一条
        time = self.get_element_text(loc.business_note_time,'个人页面交易记录时间')
        amount = self.get_element_text(loc.business_note_amount,'个人页面交易记录金额')
        return time , amount

    def get_intvest_amount_note(self):
        self.wait_eleVisble(loc.invest_note,'个人页面 投资项目分页')

        self.click_element(loc.invest_note,'个人页面 投资项目分页')
        intvest_amount = self.get_element_text(loc.intvest_amount,'个人页面 投资项目金额')
        intvest_name = self.get_element_text(loc.intvest_name,'个人页面 投资项目名称')
        # 返回 投资的项目名称  和 投资金额
        return intvest_name, intvest_amount
if __name__ == '__main__':
    pass

