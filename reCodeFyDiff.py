#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'zhangjingjun'
__mtime__ = '2017/11/28'
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
# coding=utf8
import requests
import urllib
import sys
import getopt
import time
import json

def isDefine(val_name):
	try:
		type(eval(val_name))
	except:
		return 0
	else:
		return 1


def getOptions():
	global infile
	global outfile
	global method

	opts, args = getopt.getopt(sys.argv[1:], "hi:o:m:")

	helpInfo = """
	#######################################
	#          SogouTranslate             #
	#######################################

	\t-i input file \n
	\t-o output file \n
	\t-m method (json|alltran_json|xml)\n
	"""

	if len(opts) < 3:
		print
		helpInfo
		return -1
	for op, value in opts:
		if op == "-i":
			infile = value
		elif op == "-o":
			outfile = value
		elif op == "-m":
			method = value
		else:
			print
			helpInfo
			return -2

	if not isDefine("infile") or not isDefine("outfile") or not isDefine("method"):
		print
		"[ERROR]: you must input infile, output file and method "
		return -3

	optsInfo = """
	#################################################################
	#                            Information                        #
	#################################################################

	input  file : """ + infile + """ \n
	output file : """ + outfile + """ \n
	method    : """ + str(method) + """ \n
	"""
	#	print optsInfo
	return 0


class procTransferTerm(object):
	rep = {
		"&amp;": "&",
		"&lt;": "<",
		"&gt;": ">",
		"&nbsp;": " ",
		"&quot;": "\"",
		"&apos;": "\'",
		"&nbsp;": " ",
	}  # define desired replacements here

	@staticmethod
	def process(tmp):
		if tmp.find("&") != -1:
			while True:
				flag = False
				for o_str, n_str in procTransferTerm.rep.iteritems():
					if tmp.find(o_str) != -1:
						flag = True
						tmp = tmp.replace(o_str, n_str)
						break
				if not flag:
					break
		return tmp


def readQueryFile():
	global infile
	global outfile

	if (getOptions() == 0):
		print
		"[SUCCESS] get file options!"
	else:
		print
		"[FAILED] don't get file options!"
		exit(0)

	with open(infile, 'r') as fin, open(outfile, "w") as fout:
		lineno = 0
		while True:
			line = fin.readline()
			if not line:
				break
			line = line.strip()
			lineno += 1
			sys.stdout.write("lineno: " + str(lineno) + "\r")
			sys.stdout.flush()
			time.sleep(0.1)
			getSogouTrans(line, fout, method)

query_xml='''<?xml version="1.0" encoding="UTF-8"?><soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:v2="http://api.microsofttranslator.com/V2"><soapenv:Header/><soapenv:Body><v2:Translate><v2:appId>Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzY29wZSI6Imh0dHBzOi8vYXBpLm1pY3Jvc29mdHRyYW5zbGF0b3IuY29tLyIsInN1YnNjcmlwdGlvbi1pZCI6IjY5NWI0OGIwMmZhOTQxMWRiZjhmOWNjZTQ5MGE3ZWFjIiwicHJvZHVjdC1pZCI6IlRleHRUcmFuc2xhdG9yLlMyIiwiY29nbml0aXZlLXNlcnZpY2VzLWVuZHBvaW50IjoiaHR0cHM6Ly9hcGkuY29nbml0aXZlLm1pY3Jvc29mdC5jb20vaW50ZXJuYWwvdjEuMC8iLCJhenVyZS1yZXNvdXJjZS1pZCI6Ii9zdWJzY3JpcHRpb25zLzkzOWUwNzZkLTUwOTUtNGIwYS1iYTIyLWNiNzRlNGEyMTllOC9yZXNvdXJjZUdyb3Vwcy9mYW55aS9wcm92aWRlcnMvTWljcm9zb2Z0LkNvZ25pdGl2ZVNlcnZpY2VzL2FjY291bnRzL2ZhbnlpIiwiaXNzIjoidXJuOm1zLmNvZ25pdGl2ZXNlcnZpY2VzIiwiYXVkIjoidXJuOm1zLm1pY3Jvc29mdHRyYW5zbGF0b3IiLCJleHAiOjE0OTc5MzY4NDF9.id_MzyMPW0Ic_76i_0ZSvkkj-LoGRJljAe3sKAzFO9A</v2:appId><v2:text>I wonder why,What happened?</v2:text><v2:from>en</v2:from><v2:to>zh-CHS</v2:to><v2:needQc>1</v2:needQc><v2:contentType>text/plain</v2:contentType><v2:category>general</v2:category><v2:suv>00E75AA0B6F2A1A8593F35D36AC95308</v2:suv><v2:uuid>ef7d395b-4838-46df-8398-8ef4267a07f7</v2:uuid></v2:Translate></soapenv:Body></soapenv:Envelope>'''
query_json='''{"translate_struct":{"chinese_query":"phan湿婆","english_query":"phanes shiva","docs":[{"title":"Ten intersex gods and goddesses | Lusmerlin's Blog","abstract":"   Ardhanarishvara is a god composed of half Shiva (god of destruction and ... Phanes (Greek).  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=https%3A%2F%2Flusmerlin.wordpress.com%2F2013%2F08%2F16%2Ften-intersex-gods-and-goddesses%2Famp%2F&query=phanes%20shiva&tabMode=2","id":"uigs_1","showurl":"https://lusmerlin.wordpress.com › ten-int...","imgsrc":""},{"title":"Phanes - God Pictures","abstract":"   God Phanes God Revanta Ji God Sophia Shultz God ... Rama Ji Lord Sai Baba Ji Lord Shiva Ji Lord Surya Ji ...  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Fwww.mygodpictures.com%2Fphanes%2F&query=phanes%20shiva&tabMode=2","id":"uigs_2","showurl":"www.mygodpictures.com/phanes/","imgsrc":""},{"title":"Amazon.com: Customer Reviews: Success Is Your Proof: One Hundred ...","abstract":"   Shiva X˚ is a witty, intelligent piece that speaks ... the life of Leila Waddell. Phanes X˚ and AiSh ...  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Fwww.amazon.com%2FSuccess-Is-Your-Proof-Hundred%2Fproduct-reviews%2F0986336521&query=phanes%20shiva&tabMode=2","id":"uigs_3","showurl":"www.amazon.com/Success-Is-Your-Proof-Hundred/product-reviews/0986336521","imgsrc":""},{"title":"Images of phanes shiva","abstract":"","link":"./uID=8mwoIar7V0LOwdZy/v=5/type=1/sp=1/ct=170620144044/keyword=phanes+shiva/id=04fc9dc2-4a55-486e-a00b-4c3347e9104a/sec=uiXuHutcwHDV9Aw1EG-OTA../vr=11009301/k=phanes%20shiva/tc?key=phanes+shiva&pno=1&g_ut=3&is_per=0&wml=1&clk=4&url=http%3A%2F%2Fwww.bing.com%2Fimages%2Fsearch%3Fq%3Dphanes%2Bshiva%26id%3DFC601E0E5F731BB629A94D6D2A769699F41DD1AD%26FORM%3DIQFRBA&vrid=11009301&linkid=title","id":"sogou_vr_11009301_4","showurl":"","imgsrc":""},{"title":"Prajapati: Facts, Discussion Forum, and Encyclopedia Article","abstract":"   Shiva Shiva is a major Hindu deity, and is the destroyer ... (also known as Phanēs Phanes (mythology) Phanes ..  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Fwww.absoluteastronomy.com%2Ftopics%2FPrajapati&query=phanes%20shiva&tabMode=2","id":"uigs_5","showurl":"www.absoluteastronomy.com/topics/Prajapati","imgsrc":""},{"title":"Success Is Your Proof: One Hundred Years of O.T.O. in North America: ...","abstract":"   Frater Shiva and ＂It was acceptable in the Eighties＂ ... the essays by Vere Chappell, Phanes Xth degree and ..  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Fwww.amazon.com%2FSuccess-Your-Proof-Hundred-T%2Fdp%2F0986336521%3Fie%3DUTF8%26dpID%3D41CSH-v-TTL%26dpSrc%3Dsims%26preST%3D_AC_UL160_SR111%252C160_&query=phanes%20shiva&tabMode=2","id":"uigs_6","showurl":"www.amazon.com/Success-Your-Proof-Hundred-T/dp/0986336521?ie=UTF8&dpID=41CSH-v-TTL&dpSrc=sims&preST=_AC_UL160_SR111%2C160_","imgsrc":""},{"title":"Ordo Templi Orientis (O.T.O.) News","abstract":"   Britain & Northern Ireland Fr. Phanes X°, R.S.S. Italia Fr. Sabazius X°, R.S.S. United States of America Fr. S..  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Foto.org%2Fnews1014.html&query=phanes%20shiva&tabMode=2","id":"uigs_7","showurl":"oto.org/news1014.html","imgsrc":""},{"title":"Phanes Light | FINAL FANTASY XIV, The Lodestone","abstract":"   Phanes Light; Character. Profile; Blog; Events; Character. Elite Cascadier. Phanes Light. Balmung. You have no connection with this character. Follower Requests ...  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Fna.finalfantasyxiv.com%2Flodestone%2Fcharacter%2F130769%2F&query=phanes%20shiva&tabMode=2","id":"uigs_8","showurl":"na.finalfantasyxiv.com/lodestone/character/130769","imgsrc":""},{"title":"Home | Ordo Templi Orientis | United Kingdom Grand Lodge","abstract":"   Frater Shiva X°. Most recently, on 17th May 2014e.v., ... under the leadership of Frater Phanes X°, bringing t..  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Foto-uk.org%2F&query=phanes%20shiva&tabMode=2","id":"uigs_9","showurl":"oto-uk.org/","imgsrc":""},{"title":"Greek Gods / Roman Gods","abstract":"   Hindu deities. Shiva is a godof complementary acti. ... son of Helios. Phanes: Greek, ＂light＂, first being b..  ","link":"http://snapshot.sogoucdn.com/fulltranslation?url=http%3A%2F%2Fwww.chromacity.net%2Fdivision%2Fgreek%2Fgreekgods.html&query=phanes%20shiva&tabMode=2","id":"uigs_10","showurl":"www.chromacity.net/division/greek/greekgods.html","imgsrc":""}]}}'''
resultFile=open("result",'w')
method='json'
# print "lineno: "+str(lineno)

def getSogouTrans(query, fout, method):
	encoded = unicode(query, 'utf-8').encode("utf8")
	headers = {'User-agent': 'Mozilla/5.0', "Content-type": "text/xml"}
	resp = requests.post("http://10.153.51.60:12800/" + method, headers=headers, data=encoded)
	resp_str = resp.text.encode('utf-8')
	resp_lst = resp_str.split('\n')
	print resp_lst
	fout.write(resp_str + '\n')
	s=json.loads(resp_str)
	print s['translate_result'].keys()
	# orig_text=''
	# TranslateResult=''
	# for i in resp_lst:
	# 	if "orig_text" in i:
	# 		orig_text = i.strip()
	# 	if "TranslateResult" in i:
	# 		TranslateResult = i.strip()
	# fout.write(orig_text + TranslateResult + '\n')




if __name__ == "__main__":
#	readQueryFile()
 	getSogouTrans(query_json, resultFile, method)

