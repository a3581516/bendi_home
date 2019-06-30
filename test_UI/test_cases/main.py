#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main
# Author: 简
# Time: 2019/6/20
import os
import sys
aa=sys.path.append('./')
print(aa)
# #
import pytest
os.system("pytest -m smoke -s --html=reports.aaa.html --alluredir=/reports/allure_report")
pytest.main(['-m', 'smoke'])
pytest.main(['-m','invest'])

