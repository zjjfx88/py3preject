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
import urllib3
import requests
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = "http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt"
COMMENT_CHARS="#:"

drawing = Drawing(400,200)
data=[]

r=requests.get(URL)
c=r.text

cont= c.split("\n")
#print(cont)

for line in cont:
	if line.strip()!="" and (not line.isspace()) and not (line[0] in COMMENT_CHARS):
		data.append([float(n) for n in line.split()])

swo = [row[2] for row in data]
ri = [row[3] for row in data]
times = [row[0] + row[1] / 12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = []
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red

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
drawing.add(lp)

drawing.add(String(250, 150, 'Sunspots',fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')
