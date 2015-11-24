import os
import re
import fileReader
import dPrint
import parseUnitHandlers

DEBUG=dPrint.DEBUG
ERROR=dPrint.ERROR

getDescription=parseUnitHandlers.getDescription
getQuestion=parseUnitHandlers.getQuestion
getAnswer=parseUnitHandlers.getAnswer
getFeedback=parseUnitHandlers.getFeedback
getChoice=parseUnitHandlers.getChoice
getMarks=parseUnitHandlers.getMarks

dPrintFxn = dPrint.dPrint

DESCRIPTION=0


def essayHandler (fileHndl, marks, curLineDesc , qGroupList):
	return questionAndAnswerHandler (fileHndl, marks,  curLineDesc , qGroupList, "essay")

def shortDescHandler (fileHndl, marks, curLineDesc , qGroupList):
	return questionAndAnswerHandler (fileHndl, marks,  curLineDesc , qGroupList, "shortanswer")
	
def multiChoiceHandler (fileHndl, marks, curLineDesc , qGroupList):
	return questionAndAnswerHandler (fileHndl, marks, curLineDesc , qGroupList, "multichoice")

def trueFalseHandler (fileHndl, marks, curLineDesc , qGroupList):
	qGroupList = questionAndAnswerHandler (fileHndl, marks, curLineDesc , qGroupList, "truefalse")
	return qGroupList
	
	

def questionAndAnswerHandler (fileHndl, marks, curLineDesc , qGroupList, qType):
	
	isAnsCtxtPresent = 1
	isChoiceCtxtPresent = 1

	if qType ==  "shortanswer":
		isChoiceCtxtPresent = 0	
		qUnitExitPattern="^\s*A\s*>>"
	elif qType == "essay":
		isChoiceCtxtPresent = 0	
		isAnsCtxtPresent=0
		qUnitExitPattern="(^\s*(F|Desc|Marks)\s*)|\s*(<\/essay>)"
	else:
		qUnitExitPattern="^\s*(A|C)\s*>>"
	
	dPrintFxn (DEBUG, curLineDesc[0], "Entering <%s>" %(qType))
	dPrintFxn (DEBUG, curLineDesc[0], "isChoicePresent=%d, exitPattern=%s" %(isChoiceCtxtPresent, qUnitExitPattern))
	while 1:
		qList = []
		curDesc = getDescription(fileHndl, curLineDesc) 
		isItDone = 0
		while not isItDone: 
			curQuestion =[]
			curChoice =[]
			curAns =[]
			curMark = []
			curFeedback  =[]
			dPrintFxn (DEBUG,  curLineDesc[0],"Detecting Question context")
			curQuestion = getQuestion (fileHndl, curLineDesc,
						 qUnitExitPattern) 
			if len(curQuestion) == 0:
				dPrintFxn (ERROR, curLineDesc[0],
					"Expecting Question Context, Exiting")
				os._exit(2)

			if 	isChoiceCtxtPresent == 1:	
				dPrintFxn (DEBUG,  curLineDesc[0],"Detecting Choice context")
				curChoice  = getChoice(fileHndl, curLineDesc, qType) 


			if isAnsCtxtPresent ==1:
				dPrintFxn (DEBUG,  curLineDesc[0],"Detecting Ans context")
				curAns  = getAnswer(fileHndl, curLineDesc) 
				if len(curAns) == 0:
					dPrintFxn (ABORT, curLineDesc[0],
						"Expecting Ansser Context, Exiting")
					os_exit(2)

			isItF = re.search('^\s*F\s*>>\s*(.*)',curLineDesc[1])
			isItMarks = re.search('^\s*Marks\s*>>\s*(.*)',curLineDesc[1])
			if  isItF:
				dPrintFxn (DEBUG,  curLineDesc[0],"Detecting Feeback  context")
				curFeedback  = getFeedback(fileHndl, curLineDesc) 
				dPrintFxn (DEBUG,  curLineDesc[0],"Detecting Marks  context")
				curMark  = getMarks(fileHndl, marks, curLineDesc ) 
				qList.append ((curQuestion, curChoice, curAns, curFeedback, curMark ))
			elif isItMarks:
				dPrintFxn (DEBUG,  curLineDesc[0],"Detecting Marks  context")
				curMark  = getMarks(fileHndl, marks, curLineDesc ) 
				dPrintFxn (DEBUG,  curLineDesc[0],"Detecting Feeback  context")
				curFeedback  = getFeedback(fileHndl, curLineDesc) 
				qList.append ((curQuestion, curChoice, curAns, curFeedback, curMark ))
			else:
				curMark.append ((curLineDesc[0], marks))
				qList.append ((curQuestion, curChoice, curAns, curFeedback, curMark ))

			isItQ = re.search('^\s*Q\s*>>\s*(.*)',curLineDesc[1])
			isItDone =  not isItQ
	
		qGroupList.append ((curDesc, qList))
		dPrintFxn (DEBUG, curLineDesc[0], "Looks like one Group  of Question is over. Checking for BlkEnd/Desc")
		blkEndString = '^\s*<(\/)\s*(truefalse|shortanswer|multichoice|essay)\s*>'
		isItBlkEnd = re.search(blkEndString, curLineDesc[1])
		if isItBlkEnd:
			dPrintFxn (DEBUG, curLineDesc[0], "Detected BLK end")
			dPrintFxn (DEBUG, curLineDesc[0], "Processed All Questiions in curretn Group")
			dPrintFxn (DEBUG, curLineDesc[0], "Exiting getGroup")
			return qGroupList
		dPrintFxn (DEBUG, curLineDesc[0], "Not a BlkEnd.  Entering the loop again checking out Description context")
	dPrintFxn (DEBUG, curLineDesc[0], "Exiting %s" %(qType))
