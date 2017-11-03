#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = 'chouti自动点赞'
__author__ = 'zhangjingjun'
__mtime__ = '2017/10/27'
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
import requests
i1 = requests.get('http://dig.chouti.com/help/service')

i2 = requests.post(
	url='http://dig.chouti.com/login',
	data={
		'phone':'8615811240629',
		'password':'zjjfx123',
		'oneMonth':''},
	cookies = i1.cookies.get_dict()
)
print(i1.cookies.get_dict()['gpsd'])

gpsd = i1.cookies.get_dict()['gpsd']
i3 = requests.post(
	url="http://dig.chouti.com/link/vote?linksId=14912956",

	cookies={'gpsd':gpsd}
)
print(i3.text)
