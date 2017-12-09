#coding=utf8
import requests
import urllib
import sys
import getopt
import time

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
	
	opts, args = getopt.getopt(sys.argv[1:],"i:o:m:")
	
	helpInfo = """
	#######################################
	#          SogouTranslate             #
	#######################################
	
	\t-i input file \n
	\t-o output file \n
	\t-m method (json|alltran_json|xml)\n
	"""
	
	if len(opts) < 3:
		print helpInfo
		return -1
	for op, value in opts:
		if op == "-i":
			infile = value
		elif op == "-o":
			outfile = value
		elif op == "-m":
			method = value
		else:
			print helpInfo
			return -2
	
	if not isDefine("infile") or not isDefine("outfile") or not isDefine("method"):
		print "[ERROR]: you must input infile, output file and method "
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
		"&amp;"  :"&",
		"&lt;"   :"<", 
		"&gt;"   :">", 
		"&nbsp;" :" ", 
		"&quot;" :"\"", 
		"&apos;" :"\'", 
		"&nbsp;" :" ",
		} # define desired replacements here

	@staticmethod
	def process(tmp):
		if tmp.find("&") != -1:
			while True:
				flag = False
				for o_str, n_str in procTransferTerm.rep.iteritems():
					if tmp.find(o_str) != -1:
						flag=True
						tmp = tmp.replace(o_str, n_str)
						break
				if not flag:
					break
		return tmp

def readQueryFile():
	global infile
	global outfile

	if (getOptions() == 0):
		print "[SUCCESS] get file options!"
	else:
		print "[FAILED] don't get file options!"
         	exit(0)
	
	with open(infile,'r') as fin, open(outfile,"w") as fout:
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
			getSogouTrans(line,fout,method)
#	print "lineno: "+str(lineno)
	
def getSogouTrans(query,fout,method):
	encoded = unicode(query,'utf-8').encode("utf8")
	headers = {'User-agent': 'Mozilla/5.0', "Content-type":"text/xml"}
	resp = requests.post("http://10.153.51.60:12800/"+method, headers=headers, data=encoded)
	resp_str = resp.text.encode('utf-8')
	fout.write(resp_str+'\n')
if __name__ == "__main__":
	readQueryFile()	
