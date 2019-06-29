#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver


d=webdriver.Chrome(r'D:\360安全浏览器下载\Chrome6503325146\GoogleChrome_65.0.3325.146'
                   r'\ChromePortable\App\Google Chrome\chromedriver.exe')
d.get('https://www.baidu.com/')
print(d.title)
d.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
d.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()

d.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__userName"]').send_keys('a3581516')
d.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__password"]').click('a1986815')

d.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__submit"]').click()
print(d.title)