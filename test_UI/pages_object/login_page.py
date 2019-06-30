#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_UI.common.base_page import BasePage
from test_UI.page_locators.login_page_locator import LoginPageLocator as loc

class LoginPage(BasePage):

    def login(self,user, pwd):
        self.wait_eleVisble(loc.user_loc,'登录页面输入用户名')

        self.input_text(loc.user_loc,'登录页面输入用户名',user)
        self.input_text(loc.passwd_loc,'登录页面输入密码',pwd)
        self.click_element(loc.login_button_loc,'登录页面点击登录')

    ####哪个页面 就去哪里 断言 。就可以在每个PO 页面校验不同时 改变
    # 获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        self.wait_eleVisble(loc.error_notify_from_loginForm,"登录表单区域错误提示框")

        return self.get_element_text(loc.error_notify_from_loginForm,"登录表单区域错误提示框")

    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        self.wait_eleVisble(loc.error_notify_from_pageCenter,'登录中间区域提示框')
        return self.get_element_text(loc.error_notify_from_pageCenter,'登录中间区域提示框')


##用例步骤  = 页面对象 + 元素位置 + 测试数据
# 页面对象 （一个功能，一个页面做为一个对象） = 功能+ 元素位置 + 测试数据 ，断言所需步骤 + 元素位置
# 元素 和 数据 各自独立
#元素 按 页面对象一一对应 分开管理 。 只要元素变化  对应页面对象 调用 它 一致改变

#数据 同上 就更不用说了。ddt.datas(*[{},{},{}] )  测试数据 （如：账号密码） +  断言数据（check）   分离  管理
#字典不是很好用  有待改进...
if __name__ == '__main__':
    pass

