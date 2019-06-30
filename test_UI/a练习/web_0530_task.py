#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time,re,random
from time import sleep
from selenium import webdriver
from test_UI.Common.upload import upload
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
print(time.ctime())            #current time
#输出格式化当前日期时间  strftime：string format time
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# 1、进入你所在的班级，随机选择一个已提交的作业(带有"查看成绩"的作业)，查看你的成绩是多少
# 2、获取1中作业下，作业被分享的同学名称。
# 3、在1中，切换到作业讨论，并发表你的评论。
# 4、点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。
# 5、在4的【同学】当中，使用右上角搜索功能。输入任意一个学生id，搜索学生信息。
# 【进阶思考：设计一条测试用例，来确认你的搜索结果与期望的匹配。使用unittest哦！！】
# ps：代码连接运行5次都通过的情况下，才算比较稳定。提交上来的代码，一定要是自己运行通过的。

# 1、完成课堂派 - 作业上传操作。
#
# ps：练手的课程派班级：邀请码：4SX4VK
#
# 2、完成腾讯课堂 - qq帐号登陆操作。 -- 涉及iframe，要小心哦。
#
# 3、完成12306查询票的操作  --  利用js去设置日期。
class KTP:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)

    def is_element_visibility(self,path):
        '''
        判断元素是否存在并可见，
        :param path: 参数为 Xpath 路径
        :return: 返回 找到这个元素的 对象，便利后续操作 使用
       '''
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator=(By.XPATH, path)))
        except Exception as e:
            raise e
        else:
            return self.driver.find_element(By.XPATH, path)
    def is_elements_visibility(self,path):
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_all_elements_located(locator=(By.XPATH, path)))
        except Exception as e:
            raise e
        else:
            return self.driver.find_elements(By.XPATH, path)
    def login(self):
        self.driver.get('https://w.ketangpai.com/')

        #选择电脑版
        sleep(1)
        self.is_element_visibility('//div [@class="banner"]//a[@class="pc-btn fs28"]').click()
        #登录
        self.is_element_visibility('//div[@id="indextop"]//a[text()="登录"]').click()
        #选择 账号登录 方式
        self.is_element_visibility('//a[text()="账号登录"]').click()
        #输入账号 密码  点登录
        self.is_element_visibility('//input[@name="account"]').clear()
        self.is_element_visibility('//input[@name="account"]').send_keys('13850600551')
        self.driver.find_element(By.XPATH, '//input[@type="password"]').clear()
        self.driver.find_element(By.XPATH, '//input[@type="password"]').send_keys('a123456')

        self.driver.find_element(By.XPATH,'//a[@class="btn-btn" and text()="登录"]').click()
        #关闭提醒
        self.is_element_visibility('//a[@class="close"]').click()
        sleep(1)
        print(self.driver.title)
        return self.driver.title
    def class_in(self):
        #进入班级
        self.is_element_visibility('//div[@class="empty-box hide"]/parent::div/div/following-sibling::div//strong/a[contains(text(),"第15期")]').click()
    def my_score(self):
        #查看所有 成绩单
        score_reports = self.is_elements_visibility('//a[@class="view-score"]')
        #随机选取一个 进入成绩单
        # score_reports[random.randint(0,len(score_reports)-1)].click()
        a=random.choice(score_reports)
        print(a)
        a.click()

        #查看我的成绩
        score = self.is_element_visibility('//p[@class="score fr"]/span').text
        print('我的成绩是：',score)
    def shared_names(self):
        #获取被分享作业的 同学名称
        classmate_names = '、'.join(i.text for i in self.is_elements_visibility('//p[@class="share-name"]'))
        print('作业被分享的同学名称:',classmate_names)

    def insert_comment(self):
        #切换到作业讨论
        self.is_element_visibility('//div[@id="third-nav"]//a[text()="作业讨论"]').click()
        #点击添加评论
        self.is_element_visibility('//div[@id="viewer-discuss"]//div[@class="img"]/following-sibling::p[text()="添加评论"]').click()
        #输入评论
        self.is_element_visibility('//textarea[@placeholder="添加评论"]').send_keys('hello word!')
        #提交点击确认
        self.is_element_visibility('//div[@class="opt-btn fr"]//a[text()="确定"]').click()
    def del_comment(self):
        #删除评论
        sleep(2)
        eles = self.is_elements_visibility('//ul[@class="comment-list"]//span[text()="深圳一灰灰"]/ancestor::div//p[text()="hello word!"]/parent::div//a[@title="删除"]')

        for ele in eles:
            #滚动到 可视区域
            sleep(1)
            self.driver.execute_script("arguments[0].scrollIntoView();",ele)
            sleep(1)
            ee = self.is_element_visibility('//ul[@class="comment-list"]//span[text()="深圳一灰灰"]/ancestor::div//p[text()="hello word!"]')
            ActionChains(self.driver).move_to_element(ee).perform()
            # 点击删除
            ele.click()
            #确认 删除
            self.is_element_visibility('//div[@id="layui-layer1"]//div//a[@class="layui-layer-btn0 active"]').click()
    def send_msg(self):
        self.is_element_visibility('//a [text()="同学"]').click()
        self.is_element_visibility('//li[@class="all" and contains(text(),"全部学生")]').click()
        ele = self.is_element_visibility('//li [@datas-id="MDAwMDAwMDAwMLOcy5mGudGvhLVyoQ"]')
        #滚下去看看
        sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView(false);",ele)
        #鼠标也移过去瞧瞧
        sleep(1)
        ActionChains(self.driver).move_to_element(ele).perform()
        #定位成功
        self.is_element_visibility('//li [@datas-id="MDAwMDAwMDAwMLOcy5mGudGvhLVyoQ"]//a[@class="call"]').click()

        #输入内容 发送
        self.is_element_visibility('//*[@class="ps-container"]').send_keys('sss',Keys.CONTROL+Keys.ENTER)
        #关闭
        self.is_element_visibility('//a [@class="layui-layer-ico layui-layer-close layui-layer-close2"]').click()

    def search(self):
        self.is_element_visibility('//input [@placeholder="姓名、学号"]').send_keys(1565,Keys.ENTER)

    def upload_files(self):
        #进入练习
        self.is_element_visibility('//h3[@class="work-title "]//a[@title="练习练习"]').click()
        sleep(2)
        if self.is_element_present('//a[@class="new-tj1"]'):#如果 更新提交存在
            #点击更新
            self.is_element_visibility('//a[@class="new-tj1"]').click()
            sleep(2)
            #点击确定
            self.is_element_visibility('//a [text()="确定"]/ancestor::div[@id="update-pop"]//a [text()="确定"]').click()

        #点击上传 按钮
        self.is_element_visibility('//a [@class="sc-btn webuploader-container"]').click()
        sleep(2)
        #调用函数 执行上传操作
        upload(r'F:\test_task.rar')
        sleep(2)
        #点击留言框### 第二次进来 出问题了***
        # self.is_element_visibility('//div[@id="mess1"]//span [contains(text(),"添加留言")]').click()
        #输入留言
        self.is_element_visibility('//textarea[@id="comment"]').clear()
        self.is_element_visibility('//textarea[@id="comment"]').send_keys('到此一游')
        if self.is_element_present('//div[@datas-teachername="小简"]//a[text()="更新提交"]/following-sibling::a'):
            self.is_element_visibility('//div[@datas-teachername="小简"]//a[text()="更新提交"]/following-sibling::a').click()
        # 完成后点击 提交
        else:
            self.is_element_visibility('//a [@class="tj-btn active"]').click()
        #点知道了  #这里也不点弹框....
        sleep(2)
        print(self.is_alter_present())
        self.is_element_visibility('//a [@class="weui_btn_dialog primary"]').click()

    def is_element_present(self,path):  # 是否存在
        try:
            self.driver.find_element(by=By.XPATH, value=path)
        except EC.NoSuchElementException as e:
            return False
        return True

    def is_alter_present(self):
        try:
            self.driver.switch_to.alert
        except EC.NoAlertPresentException as e:
            return False
        return True

    def login_12306(self):
        self.driver.get('https://www.12306.cn')
        self.driver.maximize_window()
        self.is_element_visibility('//input[@id="toStationText"]')
        # 设置起始城市
        js_pha = 'document.getElementById("fromStationText").value="深圳北";' \
                 'document.getElementById("fromStation").value="SZQ";'
        self.driver.execute_script(js_pha)

        # 设置终点城市
        js_pha = 'document.getElementById("toStationText").value="龙岩";' \
                 'document.getElementById("toStation").value="LYS";'
        self.driver.execute_script(js_pha)

        # 设置日期
        js_pha = 'var a = document.getElementById("train_date");a.readOnly = false;' \
                 'a.value = "2019-06-15";'

        self.driver.execute_script(js_pha)

        #点击查询
        js_pha = 'document.getElementById("search_one").click();'
        self.driver.execute_script(js_pha)
    def txkt_login(self):
        self.driver.get('https://ke.qq.com/')
        self.is_element_visibility('//a[@id="js_login"]').click()
        sleep(1)

        print('...')
        sleep(1)
        self.driver.find_element_by_xpath('//*[@class="icon-font i-qq"]').click()
        sleep(1)
        self.driver.switch_to.frame("login_frame_qq")
        sleep(2)
        self.is_element_visibility('//span[@id="img_out_360090343"]').click()
        self.is_element_visibility('//a[text()="下次再选"]').click()

if __name__ == '__main__':
    a =KTP()

    # a.login()
    # a.class_in()
    # a.upload_files()

    # a.login_12306()

    # a.txkt_login()







    a.login()
    a.class_in()
    a.my_score()
    # a.shared_names()
    # a.insert_comment()
    # a.del_comment()

    # a.login()
    # a.class_in()
    # a.send_msg()
    # a.search()





























