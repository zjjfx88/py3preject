#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2017/12/7'
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
#!/bin/python
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF
import time

drawing = Drawing(500,500)


lp = LinePlot()
lp.x = 100
lp.y = 200
lp.height = 125
lp.width = 300

lp.data = []
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.yellow
lst=[]
with open('test_out','r') as f:
        for line in f.readlines():
                line_lst=line.strip().split('\t')
                lst.append((line_lst[0],line_lst[1].split('MiB')[0]))
        lp.data.append(lst)
drawing.add(lp)
print(lp.data)
drawing.add(String(250, 150, 'Sunspots',fontSize=14, fillColor=colors.red))
renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')