#!/usr/bin/env python
# -*- coding: utf-8 -*-
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


@pytest.fixture
def login_url():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.implicitly_wait(30)
    sleep(1)
    yield driver
    # 后置
    driver.quit()
@pytest.fixture
def open_home_page(login_url):
    # 登录
    LoginPage(login_url).login(bd.success_data["user"], bd.success_data["passwd"])
    yield login_url
    # 后置
    login_url.quit()

@pytest.fixture('class')
def in_invest_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://120.78.128.25:8765/Index/login.html")
    driver.implicitly_wait(30)
    # sleep(1)
    LoginPage(driver).login(bd.success_data["user"], bd.success_data["passwd"])

    HomePage(driver).click_invest_button()
    # sleep(1)
    #楚河汉界
    yield driver
    #后置
    driver.quit()

#定义一个用例级别的 后置  默认是scope="function"
@pytest.fixture
def refresh_page(in_invest_page):
    yield
    in_invest_page.refresh()

# session级别的   默认  autouse=False
#所以不需要调用，默认自动调用    会话级
@pytest.fixture(scope="session",autouse=True)
def session_action():
    print("===== 会话开始，测试用例开始执行=====")
    yield
    print("===== 会话结束，测试用例全部执行完成！=====")

