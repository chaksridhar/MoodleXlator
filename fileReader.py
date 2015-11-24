import os
import re
class FileLineReader:
	def __init__ (self,fileName):
		try:
			self.inputHandle = open (fileName)
			self.curLineNum =0
			
		except:
			print ("Error: Unable to open file \"%s\" exiting"  %(fileName))
			os._exit (1)

	def readline(self):
		self.curLineNum = self.curLineNum + 1
		return (self.inputHandle.readline())

	def readContentLine(self):
		while 1:
			self.curLineNum = self.curLineNum + 1
			self.curLine = self.inputHandle.readline()
			if not self.curLine:
				return self.curLine
 			isItEmpty = re.search('^\s*$',self.curLine)
 			isItComment = re.search('^\s*#.*',self.curLine)
			skip =	 isItEmpty or isItComment
			if  not skip:
				 break 
		return self.curLine
				
		
