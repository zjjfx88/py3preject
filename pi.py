#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'π值得计算'
__author__ = 'zhangjingjun'
__mtime__ = '2017/10/18'
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
from random import random
from math import sqrt
from time import clock
DARTS = 12000000
hits = 0
clock()
for i in range(1,DARTS):
	x,y = random(),random()
	dist = sqrt(x**2 + y**2)
	if dist <=1.0:
		hits = hits + 1
pi = 4 * (hits/DARTS)
print("pi得值是：%s" % pi)
print("程序运行时间是：%-5.5ss" % clock())