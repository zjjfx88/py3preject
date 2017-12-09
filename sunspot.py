#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '太阳黑子活动折线图'
__author__ = 'zhangjingjun'
__mtime__ = '2017/11/3'
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
from reportlab.graphics.shapes import *
from reportlab.lib.colors import purple, PCMYKColor, black, pink, green, blue
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.legends import LineLegend
from reportlab.graphics import renderPDF

URL = "http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt"
COMMENT_CHARS="#:"
#画布大小
drawing = Drawing(500,500)
data=[]

r=requests.get(URL)
c=r.text

cont= c.split("\n")
#print(cont)

for line in cont:
	if line.strip()!="" and (not line.isspace()) and not (line[0] in COMMENT_CHARS):
		data.append([float(n) for n in line.split()])
print(data)
swo = [row[2] for row in data]
print(swo)
ri = [row[3] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]

lp = LinePlot()
#数据绘画的起点，距离画布的坐下角的相对位置
lp.x = 100
lp.y = 200
#x轴和y轴的长度
lp.height = 125
lp.width = 300
lp.data = []
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.yellow
#lp.lines[0].strokeColor = PCMYKColor(0,100,100,40,alpha=100)
#lp.lines[1].strokeColor = PCMYKColor(100,0,90,50,alpha=100)
#drawing.colorNamePairs = [(PCMYKColor(0,100,100,40,alpha=100), 'Bovis Homes'), (PCMYKColor(100,0,90,50,alpha=100), 'HSBC Holdings')]
swo_2=zip(times,swo)
ri_2=zip(times,ri)
l=[]
w=[]
for i in swo_2:
	l.append(i)
for j in ri_2:
	w.append(j)

lp.data.append(l)
lp.data.append(w)
print(lp.data)
drawing.add(lp)

try:
	# 图标文字的位置，图标名，字体大小，颜色
	drawing.add(String(250, 150, 'Sunspots',fontSize=14, fillColor=colors.red))

	renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')
except PermissionError:
	print("文件被打开，请关闭文件重新生成")
