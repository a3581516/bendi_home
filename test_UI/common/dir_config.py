#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #
print(base_dir)

screenshot_dir = os.path.join(base_dir,'pictures')

log_dir = os.path.join(base_dir, 'log')

case_dir = os.path.join(base_dir, 'test_cases')

report_dir = os.path.join(base_dir, 'reports')


