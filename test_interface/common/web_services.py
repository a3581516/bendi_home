# -*- coding : utf-8 -*-
# @Time      :2019/4/29 0:26
# @Author    : py15期   lemon_huihui
# @File      : web_service.py
import suds
from suds.client import Client
from test_interface.common.read_config import config

class WebServices():
    def client(self, method, url, data):
        url=config.get_str('api','wsdl')+url#拼接url    read_config 已经选好环境切换  自动适配
        if type(data) == str:
            data = eval(data)

        client = Client(url)
        cln_str = 'client.service.'+method+'(datas)'#利用字符串拼接
        try:
            result = eval(cln_str)              #利用eval函数特点 执行
            res = result.retInfo
            print(result)
            print(res)
        except suds.WebFault as e:
            print(e)
            print(e.fault['faultstring'])


if __name__ == '__main__':
    w = WebServices()
    url ='/sms-service-war-1.0/ws/smsFacade.ws?wsdl'
    method = 'sendMCode'
    data = "{'client_ip': '192.168.1.1', 'mobile':'1385600551', 'tmpl_id': 1}"
    w.client(method,url,data)










    #
    # t={"channel_id":2,"ip":"129.45.6.7","mobile":"mobile" ,"pwd":"123456",
    #    "user_id" :"shabicu8","verify_code":"123456"}
    # result=client.service.userRegister(t)
    # # client这个对象 ，调用service这个方法，然后再调用userRegister这个接口函数，函数里面传递刚刚我们准备
    # # 好的得参数字典 t
    # print(result)#打印返回结果
    #http://www.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl
    #
    # client = Client('http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl')
    # print(client.service.getMobileCodeInfo('13850600551', ''))
    #
    # imp = Import('http://www.w3.org/2001/XMLSchema',
    # location='http://www.w3.org/2001/XMLSchema.xsd')
    # imp.filter.add('http://WebXml.com.cn/')
    # doctor = ImportDoctor(imp)
    # client = Client('http://www.webxml.com.cn/WebServices/WeatherWS.asmx?wsdl', doctor=doctor)
    # # print client
    # print (client.service.getWeatherbyCityName('上海'))