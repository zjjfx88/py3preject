#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2017/11/15'
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
import time
dt="201711/15 15:38:12"
if dt.count("/")==2:
	print("Yes")
else:
	print("No")
#get timestamp
dt="2017/11/15 15:38:12"

timeArray=time.strptime(dt,"%Y/%m/%d %H:%M:%S")

dt_stmp=time.mktime(timeArray)

print("dt_stmp"+str(int(dt_stmp)))

#timestamp to time

timelocal=time.localtime(dt_stmp)
print(timelocal)
dt_new=time.strftime("%Y-%m-%d %H:%M:%S",timelocal)

print("dt_new"+dt_new)