#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
# aa='''<JARQ>20220922-</JARQ>'''
#
# p =re.compile('<[^>]+>')
#
# a=p.sub('',aa)
# print(a)
# if aa.find(a)>-1:
#     name = 'jj'
#     b = aa.replace(a,name)
# print(b)
# aa='''<JARQ>202209h22-</JARQ>'''
# p= '<[^>]+>'
#
# res = re.findall(p,aa)
# print(res)
#
# a = re.sub(p,'',aa,2)
# print(a)
ss = '剩余：43.94万'
# num =re.search("\d+\.?\d*",str)
# print(num.group(0))
# print(float(num.group(0)))
# print(int(13776578.80))

num = re.search("\d+\.?\d*", ss)
print(num.group(0))


print(float(num.group(0)) * 10000)
#
# print(num.group(0))


