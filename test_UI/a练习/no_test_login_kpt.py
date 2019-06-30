#!/usr/bin/env python
# -*- coding: utf-8 -*-
from test_UI.a练习.web_0530_task import *
import unittest
##就写一条最最最简单用例

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Start Login!'.rjust(30))
        cls.ktp = KTP()
    def test_login(self):
        result = self.ktp.login()

        self.assertEqual(result,'课堂-简单好用的互动课堂管理工具')

        self.ktp.driver.quit()
    @classmethod


    def is_element_present(self,by,value):#是否存在
        try:
            self.ktp.driver.find_element(by=by,value=value)
        except EC.NoSuchElementException as e:
            return False
        return True

    def tearDownClass(cls):

        print('The end Login!'.rjust(30))
if __name__ == '__main__':
    unittest.main()

