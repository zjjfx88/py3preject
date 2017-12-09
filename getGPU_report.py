#!/bin/python
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF
from sys import argv

def getLp(reportDict,init_num):
	lp = LinePlot()
	lp.x = 100
	lp.y = 100 + 200*init_num
	lp.height = 125
	lp.width = 300
	lp.data = []
	lp.lines[0].strokeColor = colors.blue
	lst=[]
	infile=reportDict[1]['filename']
	with open(infile,'r') as f:
		for line in f.readlines():
			line_lst=line.strip().split('\t')
			lst_time=int(line_lst[0])
			lst_data=int(line_lst[1])
			lst.append((lst_time,lst_data))
		lp.data.append(lst)
	return lp

def drawReport(reportDict):
	drawing = Drawing(500,900)
	length=len(reportDict)
	print(length)
	for init_num in range(0,length):
		data=reportDict.popitem()
		drawing.add(getLp(data,init_num))
		renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')

if __name__ == "__main__":
	mem={}
	mem['filename']=argv[1]
	mem['mode']='mode'
	mem['startx']=100
	mem['starty']=300
	used={}
	used['filename']=argv[2]
	used['mode']='mode'
	used['startx']=100
	used['starty']=50
	reportDict={}
	reportDict['mem']=mem
	reportDict['used']=used
	drawReport(reportDict)
