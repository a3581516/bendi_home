# -*- coding : utf-8 -*-
# @Time      :2019/4/15 23:06
# @Author    : py15期   lemon_huihui
# @File      : run_all.py
#气温气温气温不不v
import sys
aa=sys.path.append('./')
print(aa)
# #

from test_interface.common.my_test_suite import MyTestSuite
from test_interface.common.contants import html_file,case_dir

# E:\lemon_py\test_interface\run\run_all.py
suite = MyTestSuite()

suite.addPath_case(case_dir)
with open(html_file, 'wb') as fp:
    suite.run_html(stream=fp, title='前程贷项目接口测试报告',
                   description='用例范围：注册、登录、充值', tester='灰灰的')

