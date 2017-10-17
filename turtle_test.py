#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '蟒蛇绘制程序'
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

import turtle

def drawSnake(rad,angle,len,neckrad):
	'''range生成0-4，五个数的列表，循环5次'''
	for i in range(len):
		'''笔迹按照原型爬行，rad控制轨迹半径位置40，angle为弧度值80'''
		turtle.circle(rad,angle)
		turtle.circle(-rad,angle)
	turtle.circle(rad,angle/2)
	'''向前直线爬行'''
	turtle.fd(rad)
	'''粗细降低一半，转180度'''
	turtle.circle(neckrad+1,180)
	'''直线前行'''
	turtle.fd(rad*2/3)

def main():
	'''启动窗口的宽度和高度,窗口左上角在屏幕中的坐标位置（width，height，startx，starty）'''
	turtle.setup(1300,800,10,0)
	'''笔迹的宽度'''
	pythonsize=30
	turtle.pensize(pythonsize)
	'''笔迹颜色'''
	turtle.pencolor("blue")
	'''控制笔迹的初始方向，东南向40度'''
	turtle.seth(-40)
	#turtle.circle(40, 40)
	'''传参数'''
	drawSnake(40,80,5,pythonsize/2)
main()
