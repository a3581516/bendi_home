#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
#输入金额
input_amount_loc = (By.XPATH,'//input [@class="form-control invest-unit-investinput"]')
#输入框 属性名
input_amount_attr_loc = 'placeholder'
#投标按钮
invest_button_loc = (By.XPATH,'//button[@class="btn btn-special height_style"]')
#错误提示框 文本
alter_wrong_text_loc = (By.XPATH, '//div[@class="text-center"]')
#错误提示框 确认按钮
wrong_sure_loc = (By.XPATH, '//a[@class="layui-layer-btn0"]')

#可投标金额的 数字
left_money_num = (By.XPATH, '//div[@class="left fs-16 money_overplus"]/div[2]/span[2]')
#可投标金额的 单位
left_money_unit = (By.XPATH, '//div[@class="left fs-16 money_overplus"]/div[2]/span[3]')
#投标成功后， 点击查看并激活
success_sure_loc = (By.XPATH, '//div[@class="layui-layer-content"]//button [text()="查看并激活"]')
#投标成功后，提示框文本
alter_success_text_loc = (By.XPATH,'//div[@class="layui-layer-content"]//div [@class="capital_font1 note"]')
