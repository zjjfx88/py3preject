#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '温度转化程序'
__author__ = 'zhangjingjun'
__mtime__ = '2017/10/17'
# ----------Dragon be here!----------
              ┏━┓      ┏━┓
            ┏━┛ ┻━━━━━━┛ ┻━━┓
            ┃       ━       ┃
            ┃  ━┳━┛   ┗━┳━  ┃
            ┃       ┻       ┃
            ┗━━━┓      ┏━━━━┛
                ┃      ┃神兽保佑
                ┃      ┃永无BUG！
                ┃      ┗━━━━━━━━━┓
                ┃                ┣━┓
                ┃                ┏━┛
                ┗━━┓ ┓ ┏━━━┳━┓ ┏━┛
                   ┃ ┫ ┫   ┃ ┫ ┫
                   ┗━┻━┛   ┗━┻━┛
"""
val = input("亲输入带温度表示符号的温度值（例如：32C）:")
#-1取倒数第一个字符
if val[-1] in ['C','c']:
	#取第一个到倒数第一个之前的字符，不包括倒数第一个
	f = 1.8 * float(val[0:-1]) + 32
	print("转换后的温度为：%.2fF" %f)
elif val[-1] in ['F','f']:
	c = (float(val[0:-1]) - 32) / 1.8
	print("转换后的温度为：%.2fC" %c)
else:
	print("输入有误")