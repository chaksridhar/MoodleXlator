import os
import re
import fileReader
import dPrint
import parseCategoryHandlers
import sys, getopt

DEBUG = dPrint.DEBUG
ERROR = dPrint.ERROR
dPrintFxn  = dPrint.dPrint
shortDescHandler = parseCategoryHandlers.shortDescHandler
multiChoiceHandler = parseCategoryHandlers.multiChoiceHandler
trueFalseHandler = parseCategoryHandlers.trueFalseHandler
essayHandler = parseCategoryHandlers.essayHandler


categoryHandler = { 
		"shortanswer" : shortDescHandler ,
		"multichoice" : multiChoiceHandler,	
	  	"truefalse":  trueFalseHandler,
		"essay": essayHandler
		 }

def  parseFile (fileHndl):
		descList = []
		qList = []
		ansList = []
		feedbackList = []
		qGroupList = []
		masterList = {}
		masterList["shortanswer"] = []
		masterList["truefalse"] = []
		masterList["multichoice"] = []
		masterList["essay"] = []
		curLineDesc=[1,2]

		while 1:
			curLineDesc[1] = fileHndl.readContentLine()
			curLineDesc[0] = fileHndl.getLineNum() 
			if  not curLineDesc[1]:
				dPrintFxn ( DEBUG,   curLineDesc[0], "Detected EOF")
				return masterList
				break 
			dPrintFxn ( DEBUG, curLineDesc[0], "Checking for Questin Type TF/shortans/MC")
 			isItQ = re.search('\s*Q\s*[0-9]*\s*>>\s*(.*)',curLineDesc[1])
 			newQBlkStr = '\s*<\s*(truefalse|shortanswer|multichoice|essay)'
			markStr =  '(\s*Marks\s*=\s*(\d*))*\s*>'
			string3 = newQBlkStr +  markStr
			isItCategory = re.search(string3, curLineDesc[1] )
			if isItCategory:
				category= isItCategory.group(1)
				if (isItCategory.group(3)):
					marks=int(isItCategory.group(3))
				else:
					marks=1
				dPrintFxn ( DEBUG,   curLineDesc[0],"Detected <category>=%s(marks=<%d>)" %(category, marks))
				curLineDesc[1] = fileHndl.readContentLine()
				curLineDesc[0] = fileHndl.getLineNum() 
				masterList[category] =  categoryHandler[category](fileHndl,
							 marks, curLineDesc, masterList[category])	
			else: 
				dPrintFxn (urLineDesc[0],
                                      "ABORT: Unexpected syntax, cannot parse")
				dPrintFxn (curLineDesc[0], curLineDesc[1])
				sys.exit()


					
