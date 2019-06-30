#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from test_UI.common.base_page import BasePage
from test_UI.page_locators import bid_page_locator as loc
import re

class BidPage(BasePage):


    def invest(self,money):
        #金额输入框
        self.wait_eleVisble(loc.input_amount_loc,'标页面金额输入')
        self.input_text(loc.input_amount_loc,'标页面金额输入',money)
        #点击 投标按钮
        ele = self.get_element(loc.invest_button_loc,'标页面投标按钮')
        if ele.is_enabled():
            ele.click()
        else:
            return ele.text
    #购买标的金额不能大于标剩余金额
    #获取错误弹框文本内容
    def alter_wrong_text(self):
        self.wait_eleVisble(loc.alter_wrong_text_loc,'标页面输入错误弹框-文本')
        try:
            return self.get_element_text(loc.alter_wrong_text_loc,'标页面输入错误弹框-文本')
        except:
            return False

    #判断 点击弹框的确认按钮
    def alter_wrong_click_sure(self):
        self.wait_eleVisble(loc.wrong_sure_loc,'标页面输入错误弹框-确认按钮')
        try:
            self.click_element(loc.wrong_sure_loc,'标页面输入错误弹框-确认按钮')
            return True
        except Exception as e:
            return False

    #这里也可以查看 可用余额        ps：只需要取数字出来
    def get_user_left_money(self):
        self.wait_eleVisble(loc.input_amount_loc,'标页面金额输入框')
        left_money = self.get_element_attribute(loc.input_amount_loc,loc.input_amount_attr_loc,'标页面获取用户可用余额')
        return float(re.sub("\D", "", left_money)) # 去掉非数字

    #剩余可投 标的 金额           ps:注意单位
    def get_bid_left_money(self):
        self.wait_eleVisble(loc.left_money_num,'标页面剩余可投标金额')
        num = self.get_element_text(loc.left_money_num,'标页面剩余可投标金额-数量')
        unit = self.get_element_text(loc.left_money_unit,'标页面剩余可投标金额-单位')
        if unit == "万":
            return float(num)*10000
        else:
            return float(num)

    #投标成功后， 点击查看并激活，  ps：可以断言  是否弹框消失
    def click_SeeAndActive(self):
       self.wait_eleVisble(loc.success_sure_loc,'标页面查看并激活')
       self.click_element(loc.success_sure_loc,'标页面查看并激活')

    #投标成功后， 获取弹框文本内容
    def alter_success_text(self):
        self.wait_eleVisble(loc.alter_success_text_loc,'标页面获取投标成功弹框文本')
        try:
            res = self.get_element_text(loc.alter_success_text_loc,'标页面获取投标成功弹框文本')
        except:
            return False
        return res
if __name__ == '__main__':
    pass