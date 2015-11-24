import os
import re
import fileReader
import dPrint

DEBUG = dPrint.DEBUG
ERROR = dPrint.ERROR

dPrintFxn = dPrint.dPrint

def getDescription (fileHndl, curLineDesc):
	curDesc = []
	dPrintFxn ( DEBUG,curLineDesc[0], "Entering Description Funciton")
	isItD = re.search('^\s*Desc\s*>>\s*(.*)',curLineDesc[1])
	if not isItD:
		return curDesc
	desc = isItD.group(1)
	while isItD:	
		dPrintFxn ( DEBUG, curLineDesc[0], " Processing DescrLines %s" %(curLineDesc[1]))
		curDesc.append((curLineDesc[0], desc))
		curLineDesc[1] = fileHndl.readContentLine()
		if not curLineDesc[1]:
			return curDesc
		curLineDesc[0] = fileHndl.getLineNum() 
		isItQ = re.search('^\s*Q\s*>>\s*(.*)',curLineDesc[1])
		isItD =  not isItQ
		desc = curLineDesc[1]
	dPrintFxn ( DEBUG,curLineDesc[0], "Exiting Description Funciton")
	return curDesc


def getQuestion (fileHndl, curLineDesc, exitPattern) :
	
	dPrintFxn ( DEBUG,curLineDesc[0], "Entering geQuestion Funciton")
	isItQ = re.search('^\s*Q\s*>>\s*(.*)',curLineDesc[1])
	curQuestion = [] ;
	if  not isItQ:
		dPrintFxn ( ERROR,curLineDesc[0], "Did not obtain Questinn Cntext. EXITING")
		os._exit(2)
	question = isItQ.group(1)
	while isItQ:	
		dPrintFxn ( DEBUG, curLineDesc[0], " Processing Question %s" %(curLineDesc[1]))
		curQuestion.append((curLineDesc[0], question))
		curLineDesc[1] = fileHndl.readContentLine()
		curLineDesc[0] = fileHndl.getLineNum() 
		if not curLineDesc[1]:
			return curQuestion
		isItExit = re.search( exitPattern,curLineDesc[1])
		isItQ = not isItExit
		question  = curLineDesc[1]

	dPrintFxn ( DEBUG,curLineDesc[0], "Exiting geQuestion Funciton it maches exit Pattern %s" %(exitPattern))
	return (curQuestion)


def  getChoice(fileHndl, curLineDesc, qType): 
	dPrintFxn ( DEBUG,curLineDesc[0], "Entering Get Choice Funciton")
	isItC = re.search('^\s*C\s*>>\s*(.*)',curLineDesc[1])
	choiceList = [] ;
	if  not isItC:
		if (qType == "truefalse"):
			thisChoiceArray = []
			dPrintFxn ( DEBUG,curLineDesc[0], "Adding True/False option to the   choices") 
			curChoice = "true"	
			thisChoiceArray.append ((curLineDesc[0], curChoice))
			choiceList.append (thisChoiceArray)
			thisChoiceArray = []
			curChoice = "false"	
			thisChoiceArray.append ((curLineDesc[0], curChoice))
			choiceList.append (thisChoiceArray)
			return choiceList
	thisChoice = isItC.group(1)
	thisChoiceArray = []

	while (1):
		while isItC: 
			dPrintFxn ( DEBUG, curLineDesc[0], " Processing Choice %s" %(thisChoice))
			thisChoiceArray.append (( curLineDesc[0], thisChoice))	
			curLineDesc[1] = fileHndl.readContentLine()
			curLineDesc[0] = fileHndl.getLineNum() 
			if not curLineDesc[1]:
				return curChoice
			isItNextC = re.search('^\s*C\s*>>\s*(.*)',curLineDesc[1])
			isItNextA = re.search('^\s*A\s*>>\s*(.*)',curLineDesc[1])
			isItC = not (isItNextA or isItNextC)
			thisChoice =curLineDesc[1]
		choiceList.append ( thisChoiceArray)	
		if isItNextA:
			dPrintFxn ( DEBUG,curLineDesc[0], "Detected Answer hence breaking out of loop")
			break ;
		else:
			isItC =isItNextC
			dPrintFxn ( DEBUG,curLineDesc[0], "Detected New Choice Specificaiton and hence continuing with the loop")
			thisChoice = isItC.group(1)
			thisChoiceArray = []
			
		dPrintFxn ( DEBUG,curLineDesc[0], "Exiting getChoice Funciton")
	return (choiceList)


def  getAnswer(fileHndl, curLineDesc): 
	dPrintFxn ( DEBUG,curLineDesc[0], "Entering getAnswer Funciton")
	isItA = re.search('^\s*A\s*>>\s*(.*)',curLineDesc[1])
	curAns = [] ;
	if  not isItA:
		dPrintFxn ( ERROR,curLineDesc[0], "EROOR: Did not obtain Answer Cntext. EXITING")
		os._exit(2)
		
	answer = isItA.group(1)
	while isItA: 
		dPrintFxn ( DEBUG, curLineDesc[0], " Processing Answer %s" %(answer))
		curAns.append((curLineDesc[0], answer))
		curLineDesc[1] = fileHndl.readContentLine()
		curLineDesc[0] = fileHndl.getLineNum() 
		if not curLineDesc[1]:
			return curAns
		isItFQDesc = re.search('^\s*(F|Q|Desc|Marks)\s*>>\s*(.*)',curLineDesc[1])
		string1 = '^\s*<(\/)\s*(truefalse|shortanswer|essay|multichoice)\s*>'
		isItBlkEnd = re.search(string1, curLineDesc[1])
		isItA = not (isItFQDesc or isItBlkEnd)
		answer =curLineDesc[1]

	dPrintFxn ( DEBUG,curLineDesc[0], "Exiting getAnswer Funciton")
	return (curAns)


def  getFeedback(fileHndl, curLineDesc): 
	dPrintFxn ( DEBUG,curLineDesc[0], "Entering getFeeback Funciton")
	isItF = re.search('^\s*F\s*>>\s*(.*)',curLineDesc[1])
	curFeedback = [] ;
	if not isItF:
		return curFeedback

	feedback = isItF.group(1)
	while isItF: 
		dPrintFxn ( DEBUG, curLineDesc[0], " Processing Feedback %s" %(feedback))
		curFeedback.append((curLineDesc[0], feedback))
		curLineDesc[1] = fileHndl.readContentLine()
		curLineDesc[0] = fileHndl.getLineNum() 
		if not curLineDesc[1]:
			return curFeedback
		isItQDMarksDesc = re.search('^\s*(Q|Desc|Marks)\s*>>\s*(.*)',curLineDesc[1])
		string1 = '^\s*<(\/)\s*(truefalse|shortanswer|essay|multichoice)\s*>'
		isItBlkEnd = re.search(string1, curLineDesc[1])
		isItF = not (isItQDMarksDesc or isItBlkEnd)
		feedback =curLineDesc[1]

	dPrintFxn ( DEBUG,curLineDesc[0], "Exiting getFeedback Funciton")
	return (curFeedback)

def  getMarks(fileHndl, marks, curLineDesc): 
	dPrintFxn ( DEBUG,curLineDesc[0], "Entering getMarks Funciton")
	isItMarks = re.search('^\s*Marks\s*>>\s*(.*)',curLineDesc[1])
	curMarks =  []
	if not isItMarks:
		curMarks.append ((curLineDesc[0], marks))
		return  curMarks
	marks = isItMarks.group(1)
	while isItMarks: 
		dPrintFxn ( DEBUG, curLineDesc[0], " Processing Marks %s" %(marks))
		curMarks.append((curLineDesc[0], int(marks)))
		curLineDesc[1] = fileHndl.readContentLine()
		curLineDesc[0] = fileHndl.getLineNum() 
		if not curLineDesc[1]:
			return curMarks
		isItQDDesc = re.search('^\s*(Q|Desc|F)\s*>>\s*(.*)',curLineDesc[1])
		string1 = '^\s*<(\/)\s*(truefalse|shortanswer|essay|multichoice)\s*>'
		isItBlkEnd = re.search(string1, curLineDesc[1])
		isItMarks = not (isItQDDesc or isItBlkEnd)
		marks =curLineDesc[1]

	dPrintFxn ( DEBUG,curLineDesc[0], "Exiting getMarks Funciton")
	return (curMarks)
