#!/bin/python
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics import renderPDF
from sys import argv
import string

def getLp(reportDict,init_num,height):
	lp = LinePlot()
	lp.x = 100
	lp.y = height-(200*(init_num+1))
	lp.height = 125
	lp.width = 600
	lp.data = []
	lp.lines[0].strokeColor = colors.blue
	lst=[]
	infile=reportDict[0]
	with open(infile,'r') as f:
		for line in f.readlines():
			line_lst=line.split('\t')
			lst_time=int(line_lst[0])
			lst_data=int(line_lst[1])
			lst.append((lst_time,lst_data))
		lp.data.append(lst)
	return lp

def drawReport(reportDict):
    length = len(reportDict)
    height = 250*length
    drawing = Drawing(700,height)
    for init_num in range(0,length):
        data=reportDict.popitem()
        drawing.add(getLp(data,init_num,height))
        drawing.add(String(230, 1270-200*init_num, data[0], fontSize=14, fillColor=colors.black))
        renderPDF.drawToFile(drawing, 'NvidiaInfo.pdf')

if __name__ == "__main__":
    dictreport={}
    for num in (range(1,len(argv))):
        dictreport[argv[num]]=argv[num]
    drawReport(dictreport)

