gDebugLevel = 2

DEBUG=2
ERROR=1


def dPrint (level,line, *args):
	global gDebugLevel 
	if gDebugLevel >= 2:
		if level == DEBUG:
			print ("DEBUG:>> Processing Line Num>>%d %s" %(line,args)) 
	if level ==1 :
		print ("ERROR:>> Processing Line Num>>%d %s" %(line,args)) 

if __name__ == "__main__":
	import fileReader
	FileLineReader = fileReader.FileLineReader
	gFileHndl = FileLineReader("sample1.txt") 
	while 1:
 		str = gFileHndl.readContentLine()
		curLineNum = gFileHndl.getLineNum() 
		dPrint (DEBUG,curLineNum , str)
	
