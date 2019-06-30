#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 正常场景
success_data = {"user":"13760246701","passwd":"python","money":300,"check":"投标成功！恭喜获得抢先投标奖励+1%奖励！"}
                # {"user":"13760246701","passwd":"python","money":  300  ,"check":"投标成功！"}
                # {"user":"13760246701","passwd":"python","money":00300,"check":"投标成功！"}
                #


# 1）投资为10   提示  要为100的整数倍           弹框 ：投标金额必须为100的倍数
# 2）投资为12   提示   要为10的整数倍           没弹框 ：  请输入10的整数倍
# 3）投资为非数字 要为1-的整数倍  含空格 特殊字符：    没弹框 ：  请输入10的整数倍
# 4）投资为0/负数//空   提示  -100    全空格 中间空格  为000  弹框：      请正确填写投标金额
wrong_datas = [
    {"user":"13760246701","passwd":"python","money":"10","check":"投标金额必须为100的倍数"},
    {"user":"13760246701","passwd":"python","money":"12","check":"请输入10的整数倍"},
    {"user":"13760246701","passwd":"python","money":"aa~!@#$","check":"请输入10的整数倍"},
    {"user":"13760246701","passwd":"python","money":"100 123","check":"请输入10的整数倍"},
    {"user":"13760246701","passwd":"python","money":"-100","check":"请正确填写投标金额"},
    {"user":"13760246701","passwd":"python","money":"    ","check":"请正确填写投标金额"},
    {"user":"13760246701","passwd":"python","money":"0000","check":"请正确填写投标金额"},
    {"user":"13760246701","passwd":"python","money":"before_bid_money+100","check":"投标失败，该标的每个用户限投50,000元! 您已投资900.00元，还可投资49100.00元"}
]
#
# # 用户名未注册 /密码错误
# fail_datas = [
# ]

