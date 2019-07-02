#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Name: main
# Author: 简
# Time: 2019/6/20
import os
import sys
# aa=sys.path.append('./')

# #python test_UI\test_cases\main.py

import pytest
os.system("pytest -v -s --html=reports.aaa.html --alluredir=/reports/allure_report -m login")
# pytest.main(['-m', 'smoke'])
# pytest.main(['-m','invest'])
# pytest.main(['-m', 'login'])