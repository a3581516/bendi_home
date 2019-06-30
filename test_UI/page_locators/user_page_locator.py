#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
#余额
left_money = (By.XPATH,'//li[@class="color_sub"]')
#交易记录 页面按钮
business_note = (By.XPATH,'//div[text()="交易记录"]')
#交易记录 时间
business_note_time = (By.XPATH, '//div[@class="deal_tab_font2"]')
#交易记录 金额
business_note_amount = (By.XPATH,'//td [@width="175"]//div[@class="deal_tab_font1"]')

#投资项目 页面按钮
invest_note = (By.XPATH, '//div[text()="投资项目"]')
##投资项目 金额
intvest_amount = (By.XPATH, '//div[@ms-html="item.money"]')
##投资项目 名称
intvest_name = (By.XPATH,'//div[@ms-html="item.title"]')