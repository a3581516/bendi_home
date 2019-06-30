#!/usr/bin/env python
# -*- coding: utf-8 -*-

from page_objects import PageElement,PageObject
import time, re, random, os, datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from test_UI.common.my_log import MyLog
from test_UI.common.upload import upload
from test_UI.common.dir_config import *

logger = MyLog(__name__)

class BasePage(object):
    def __init__(self, driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
    #等待元素可见
    def wait_eleVisble(self, loc,img_doc, timeout=40, frequency=0.5):
        t1 = datetime.datetime.now()
        try:
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
            t2 = datetime.datetime.now()
            logger.info('等待结束。等待开始时间：{0}等待结束时间：{1}。等待时长为：{2}'.format(t1,t2,t2-t1))
        except Exception as  e:
            logger.error('等待元素可见失败：{0}'.format(loc))
            # 截图 - 哪一个页面哪一个操作导致的失败。+ 当前时间
            self.save_web_screenshot(img_doc)
            raise e
    #等待元素存在 
    def wait_eleExists(self, loc, img_doc, timeout=30, frequency=0.5):
        t1 = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.presence_of_element_located(loc))
            t2 = datetime.datetime.now()
            logger.info('等待结束。等待开始时间：{0}等待结束时间：{1}。等待时长为：{2}'.format(t1, t2, t2 - t1))
        except Exception as  e:
            logger.error('等待元素可见失败：{0}'.format(loc))
            # 截图 - 哪一个页面哪一个操作导致的失败。+ 当前时间
            self.save_web_screenshot(img_doc)
            raise e

    # 查找一个元素
    def get_element(self, loc, img_doc=""):
        """
        :param loc: 元素定位。以元组的形式。(定位类型、定位时间)
        :param img_doc: 截图的说明。例如：登陆页面_输入用户名
        :return: WebElement对象。
        """
        logger.info("查找 {} 中的元素 {} ".format(img_doc, loc))
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            # 日志
            logger.error("查找元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    #点击元素  ps: 等待放里面了 偷懒
    def click_element(self, loc, img_doc, timeout=30, frequency=0.5):
        """
        实现了，等待元素可见，找元素，然后再去点击元素。
        :param loc:
        :param img_doc:
        :return:
        # """
        # # 1、等待元素可见
        # self.wait_eleVisble(loc, img_doc, timeout, frequency)
        # # 2、找元素
        ele = self.get_element(loc, img_doc)
        # 3、再操作
        logger.info(" 点击元素 {}".format(loc))
        try:
            ele.click()
        except:
            # 日志
            logger.error("点击元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 文本输入     ps: 等待放里面了 偷懒
    def input_text(self, loc, img_doc, *args):
        # # 1、等待元素可见
        # self.wait_eleVisble(loc, img_doc)
        # 2、找元素
        ele = self.get_element(loc, img_doc)
        # 3、再操作
        logger.info(" 给元素 {} 输入文本内容:{}".format(loc, args))
        try:
            #ActionChains(self.driver).move_to_element(ele).perform()
            #滚动到输入的位置
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            ele.send_keys(*args)
        except:
            # 日志
            logger.error("元素输入操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的属性值
    def get_element_attribute(self, loc, attr_name, img_doc):
        ele = self.get_element(loc, img_doc)
        # 获取属性
        try:
            attr_value = ele.get_attribute(attr_name)
            logger.info("获取元素 {} 的属性 {} 值为:{}".format(loc, attr_name, attr_value))
        except:
            # 日志
            logger.error("获取元素属性失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise
        return attr_value

    # 获取元素的文本值。
    def get_element_text(self, loc, img_doc):
        ele = self.get_element(loc, img_doc)
        # 获取属性
        try:
            text = ele.text
            logger.info("获取元素 {} 的文本值为:{}".format(loc, text))
        except:
            # 日志
            logger.error("获取元素文本值失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise
        return text


    # 实现网页截图操作
    def save_web_screenshot(self, img_doc):
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_doc, now)
        try:
            self.driver.save_screenshot(screenshot_dir + "/" + filepath)
            logger.info("网页截图成功。图片存储在：{}".format(screenshot_dir + "/" + filepath))
        except:
            logger.error("网页截屏失败！")
            raise

    # windows切换

    # iframe切换

    # select下拉列表

    # 上传操作 - 

    # 等待 弹窗 并处理它e
    def alter_handler(self,img_doc, timeout, frequency,action= "accept"):
        t1 = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.alert_is_present())
            t2 = datetime.datetime.now()
            logger.info('等待弹窗结束。等待开始时间：{0}等待结束时间：{1}。等待时长为：{2}'.format(t1, t2, t2 - t1))
        except Exception as  e:
            logger.error('等待弹窗可见 失败：{0}')
            # 截图 - 哪一个页面哪一个操作导致的失败。+ 当前时间
            self.save_web_screenshot(img_doc)
            raise e
        #调用下面的 函数 关闭弹窗 并返回 文本
        return self.close_alert_and_get_its_text()
        # alert = self.driver.switch_to.alert
        # msg = alert.text
        #
        # if action == "accept":
        #     alert.accept()
        # else:
        #     alert.dismiss()
        # return msg


    # 关闭警告和对得到文本框的处理
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text

        finally:
            self.accept_next_alert = True

    # 判断是否存在
    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except EC.NoSuchElementException as e:
            return False
        return True
    #弹框是否存在
    def is_alter_present(self):
        try:
            self.driver.switch_to.alert
        except EC.NoAlertPresentException as e:
            return False
        return True







