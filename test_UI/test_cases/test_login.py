#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from test_UI.pages_object.login_page import LoginPage
from test_UI.pages_object.home_page import HomePage
from test_UI.datas import Comm_Datas as cd
from test_UI.datas import login_datas as ld
from selenium import webdriver
import unittest
from time import sleep
from ddt import ddt , data , unpack
import pytest

import pytest_html


# @pytest.mark.login
class TestLogin():
    pytestmark=pytest.mark.log
    # 正常场景

    @pytest.mark.success
    def test_login_success(self,login_url):
        LoginPage(login_url).login(ld.success_data["user"], ld.success_data["passwd"])
        assert HomePage(login_url).check_nick_name_exists()
        # sleep(1)
        assert login_url.current_url == ld.success_data["check"]

    # 密码为空/用户名为空/用户名格式不正确
    @pytest.mark.parametrize('data',ld.wrong_datas)
    def test_login_wrong_datas(self,data,login_url):
        LoginPage(login_url).login(data['user'],data['passwd'])
        res = LoginPage(login_url).get_error_msg_from_loginForm()
        assert data["check"] == res

    # 用户名未注册 /密码错误
    @pytest.mark.parametrize('data',ld.fail_datas)
    def test_login_faile_datas(self,data,login_url):
        LoginPage(login_url).login(data["user"], data["passwd"])
        res = LoginPage(login_url).get_error_msg_from_pageCenter()
        assert data["check"] == res

if __name__ == '__main__':
    # pytest.main(['-m','log'])
    os.system("pytest -m log -s --html=reports.aaa.html")