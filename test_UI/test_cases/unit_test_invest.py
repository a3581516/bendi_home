#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pytest
import pytest_html
from test_UI.pages_object.login_page import LoginPage
from test_UI.pages_object.home_page import HomePage
from test_UI.pages_object.bid_page import BidPage
from test_UI.pages_object.user_page import UserPage
from test_UI.datas import Comm_Datas as cd
from test_UI.datas import login_datas as ld
from test_UI.datas import bid_datas as bd
from test_UI.common.my_log import MyLog
from selenium import webdriver
import unittest
from time import sleep
from ddt import ddt , data , unpack




"""
用例1：正常投资，投资金额：1000
异常用例:
# 1）投资为10   提示  要为100的整数倍           弹框 ：投标金额必须为100的倍数
# 2）投资为12   提示   要为10的整数倍           没弹框 ：  请输入10的整数倍
# 3）投资为非数字 要为1-的整数倍  特殊字符：    没弹框 ：  请输入10的整数倍
# 4）投资为0/负数/含空格/空   提示              -100    全空格 中间空格  为000        请正确填写投标金额

# 5）投资数 > 标总可投额  提示   购买标的金额不能大于标剩余金额
#    # 充值10万，创建一个借款9万块的标
#
# 6）投资数 > 你可用余额 且 标可投 > 投资数  提示   你投的钱 > 你能投的钱
#   你只有10万，你要投20万，标的可投为200万
#   # 另外一个帐号，永远都是10万。创建一个标为200万   你去投20万
"""
# 前置(准备工作-)、步骤(用户页面操作)、断言(页面操作)
# 前置 - 通过代码来创建前置 - 尽量少的依赖环境数据
"""
1、投资帐号登陆；
2、要有可投的标 - 有可投余额。没有就加标？--- 接口
3、用户余额充足 - 充值5000块线 - 接口实现
- 钱 > 投资金额  - 不充。不大了呢，一口气充2000000
- 充个2000万 ()

"""
# 步骤
"""
1、首页 - 选一个标，进入标页面
2、投资页面 - 输入金额，进行投资
"""
# 断言
"""
1、个人页面 - 个人余额少的部分 == 投资前的金额 - 投资后的金额
2、投资记录
3、标的可投金额  - 投资金额 = 投资之后的金额 
"""

import unittest

@ddt
class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://120.78.128.25:8765/Index/login.html")
        cls.driver.implicitly_wait(30)
        cls.lp = LoginPage(cls.driver)
        cls.hp = HomePage(cls.driver)
        cls.bd = BidPage(cls.driver)
        cls.up = UserPage(cls.driver)
        sleep(1)
        # 登录
        cls.lp.login(bd.success_data["user"], bd.success_data["passwd"])
        # 首页 - 选标投资
        cls.hp.click_invest_button()

    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
       cls.driver.quit()

    # def test_invest_success(self):
    #     #登录
    #     self.lp.login(bd.success_data["user"], bd.success_data["passwd"])
    #     # 首页当前标的可投金额
    #     print('投资前，主页标的可投金额：', self.hp.get_bid_money())
    #     # 获取 个人页面余额
    #     self.hp.click_user_center()
    #     print('投资前，个人页面余额：',self.up.get_user_left_money())
    #
    #     #返回首页 - 选标投资
    #     self.hp.click_home_back()
    #     self.hp.click_invest_button()
    #
    #     # 标页面 - 获取用户余额、获取标的可投金额
    #     before_bid_money = self.bd.get_bid_money()
    #     print('投资前，标页面可投标金额：',before_bid_money)
    #     before_left_money = self.bd.get_user_left_money()
    #     print('投资前，标页面可用余额：',before_left_money)
    #
    #     #标页面 - 投资操作 300
    #     self.bd.invest(bd.success_data["money"])
    #
    #     # 标页面 - 获取弹出框文本
    #     alter_suc_text =self.bd.alter_text()
    #     sleep(1)
    #
    #     #标页面 - 点击查看详情 -》进入个人页面
    #     self.bd.click_SeeAndActive()
    #
    #     #个人页面 - 获取投资后的用户可用余额
    #
    #     print('投资后，个人页面余额：',self.up.get_user_left_money())
    #     print('交易记录：',self.up.get_business_amount_note())
    #     print('项目记录：',self.up.get_intvest_amount_note())
    #     sleep(1)
    #     #主页 - 点击首页
    #     self.hp.click_home_back()
    #     # sleep(10)
    #     print('投资后，主页标的可投金额：', self.hp.get_bid_money())
    #     # 回到标页面看看
    #     self.hp.click_invest_button()
    #
    #     after_bid_money = self.bd.get_bid_money()
    #     print('投资后，标页面可投金额：', after_bid_money)
    #     after_left_money = self.bd.get_user_left_money()
    #     print('投资后，标页面可用余额：', after_left_money)
    #     # 断言
    #     try:
    #         print('开始断言.........')
    #         self.assertEqual(alter_suc_text,bd.success_data["check"])
    #         # 投资金额  = 投资前的钱 - 投资后的钱
    #         self.assertEqual(before_bid_money-after_bid_money, bd.success_data["money"])
    #         self.assertEqual(before_left_money-bd.success_data["money"], after_left_money)
    #     except Exception as e:
    #         raise e
    #     finally:
    #         print('结束断言........')
    # 个人页面 - 获取投资后的用户可用余额
    @data(*bd.wrong_datas)
    def test_invest_failed_wrong_format(self,wrong_data):
        print(bd.wrong_datas)


        # 标页面 - 获取用户余额、获取标的可投金额
        before_bid_money = self.bd.get_bid_left_money()
        print('投资前，标页面可投标金额：', before_bid_money)
        before_left_money = self.bd.get_user_left_money()
        print('投资前，标页面可用余额：', before_left_money)

        # 标页面 - 投资操作
        #eval（参数+1）   然后再转换会str写入 str(eval(wrong_data["money"]))
        if 'before_bid_money+1' in wrong_data["money"]:
            wrong_data["money"] = str(eval(wrong_data["money"]))

        result = self.bd.invest(wrong_data["money"])
        #不能点击 没有弹框 就返回 输入框文本
        if  result is not None:
            res =  result
        # 否则 出现弹框1 返回错误弹框文本
        elif  self.bd.alter_wrong_text():
            res =  self.bd.alter_wrong_text()
        # 否则 出现弹框2 返回成功 弹框文本
        else:
            print('错误格式，既然成功了...',self.bd.alter_success_text())
            res = False

        after_bid_moneyt = self.bd.get_bid_left_money()
        # 提示信息对不对？？
        print('断言开始...')
        self.assertEqual(wrong_data["check"],res)
        assert after_bid_moneyt == before_bid_money
        print('断言结束...')






# 首页 - 选标投资
# 获取 个人余额、获取 当前标的可投金额
# 标页面 - 获取用户余额、获取标的可投金额
# 标页面 - 投资操作 10/-1/0/$%%%/空
# 断言
# 提示信息对不对？？
# 个人的钱有没有少？？

if __name__ == '__main__':
    unittest.main()
