#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '字符串使用实例'
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
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = input("请输入月份数：")
pos = (int(n)-1)*3
monthsAbbrev = months[pos:pos+3]
print("月份简写："+monthsAbbrev+".")