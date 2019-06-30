#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os

from test_UI.pages_object.login_page import LoginPage
from test_UI.pages_object.home_page import HomePage
from test_UI.pages_object.bid_page import BidPage
from test_UI.pages_object.user_page import UserPage
from test_UI.datas import Comm_Datas as cd
from test_UI.datas import login_datas as ld
from test_UI.datas import bid_datas as bd
from test_UI.common.my_log import MyLog
from selenium import webdriver
import pytest, pytest_html
from time import sleep
pytestmark=pytest.mark.demo

@pytest.mark.usefixtures('session_action')#
#标记
@pytest.mark.invest
#使用前置   #用例级别
@pytest.mark.usefixtures('open_home_page')
def test_invest_success(open_home_page ):
    lp = LoginPage(open_home_page)
    hp = HomePage(open_home_page)
    bp = BidPage(open_home_page)
    up = UserPage(open_home_page)
    #首页当前标的可投金额
    print('投资前，主页标的可投金额：',hp.get_bid_left_money())
    # 获取 个人页面余额
    hp.click_user_center()
    print('投资前，个人页面余额：',up.get_user_left_money())

    #返回首页 - 选标投资
    hp.click_home_back()
    hp.click_invest_button()

    # 标页面 - 获取用户余额、获取标的可投金额
    before_bid_money = bp.get_bid_left_money()
    print('投资前，标页面可投标金额：', before_bid_money)
    before_left_money = bp.get_user_left_money()
    print('投资前，标页面可用余额：', before_left_money)

    # 标页面 - 投资操作 300
    bp.invest(bd.success_data["money"])

    # 标页面 - 获取弹出框文本
    print('成功弹窗文本:',bp.alter_success_text())
    sleep(1)

    # 标页面 - 点击查看详情 -》进入个人页面
    bp.click_SeeAndActive()

    # 个人页面 - 获取投资后的用户可用余额

    print('投资后，个人页面余额：', up.get_user_left_money())
    print('交易记录：', up.get_business_amount_note())
    print('项目记录：', up.get_intvest_amount_note())
    sleep(1)
    # 主页 - 点击首页
    hp.click_home_back()
    # sleep(10)
    print('投资后，主页标的可投金额：', hp.get_bid_left_money())
    # 回到标页面看看
    hp.click_invest_button()

    after_bid_money = bp.get_bid_left_money()
    print('投资后，标页面可投金额：', after_bid_money)
    after_left_money = bp.get_user_left_money()
    print('投资后，标页面可用余额：', after_left_money)
    # 断言
    try:
        print('开始断言.........')
        # 投资金额  = 投资前的钱 - 投资后的钱
        assert before_bid_money - after_bid_money == bd.success_data["money"]
        assert before_left_money - bd.success_data["money"] == after_left_money
    except Exception as e:
        raise e
    finally:
        print('结束断言........')




# @pytest.mark.usefixtures('in_invest_page')#class 级
@pytest.mark.usefixtures('refresh_page')# function级别
class TestInvestFail():

    @pytest.mark.smoke
    @pytest.mark.parametrize('wrong_data',bd.wrong_datas)
    def test_invest_failed_wrong_format(self,wrong_data,in_invest_page):
        print(bd.wrong_datas)

        bp = BidPage(in_invest_page)

        # 标页面 - 获取用户余额、获取标的可投金额
        before_bid_money = bp.get_bid_left_money()
        print('投资前，标页面可投标金额：', before_bid_money)
        before_left_money = bp.get_user_left_money()
        print('投资前，标页面可用余额：', before_left_money)

        # 标页面 - 投资操作
        #eval（参数+1）   然后再转换会str写入 str(eval(wrong_data["money"]))
        if 'before_bid_money+1' in wrong_data["money"]:
            wrong_data["money"] = str(eval(wrong_data["money"]))

        result = bp.invest(wrong_data["money"])
        #不能点击 没有弹框 就返回 输入框文本
        if  result is not None:
            res =  result
        # 否则 出现弹框1 返回错误弹框文本
        elif  bp.alter_wrong_text():
            res =  bp.alter_wrong_text()
        # 否则 出现弹框2 返回成功 弹框文本
        else:
            print('错误格式，既然成功了...',bp.alter_success_text())
            res = False

        after_bid_moneyt = bp.get_bid_left_money()
        # 提示信息对不对？？
        print('断言开始...')
        assert wrong_data["check"] == res
        assert after_bid_moneyt == before_bid_money
        print('断言结束...')


if __name__ == '__main__':
    # pytest.main(['-m','smoke'])
    os.system("pytest -m smoke -s --html=reports.aaa.html --alluredir=/reports/allure_report")
#os.system("alluredir serve /reports/allure_report")
