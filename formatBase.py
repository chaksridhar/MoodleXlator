import printQGroup
printQGroup = printQGroup.printQGroup
class FormatBase:
	formatTypeHandlerHash =  {}


	def __init__ (self, formatType, inputDesc):
		self.formatTypeHandlerHash[formatType.upper()] = self
		self.myFormat = formatType
		self.qBank = inputDesc


	def formatProlog(self):
		pass
	def formatpilog(self):
		pass
	def execFormatter(self):
		dNumber =0
		if self.qBank:
			self.formatProlog()
		for  qType in self.qBank:
			qGroupList = self.qBank[qType]	
			printQGroup ( qGroupList, qType)
			length = len(qGroupList)
			out = ""
			for   i in range (0, length):
				thisQGroup = qGroupList[i]
				thisQGroupDesc =  thisQGroup[0]
				numLinesInDesc = len(thisQGroupDesc)
				tupleList =thisQGroup[1]
				numTuples = len(tupleList)
				qNumber = 0
				dNumber = dNumber + 1
				for k in range (0, numTuples):
					qNumber = qNumber+1
					curQuestion = tupleList[k][0]
					curChoiceList = tupleList[k][1]
					curAns = tupleList[k][2]
					curFeedback = tupleList[k][3]
					curMarks = tupleList[k][4][0][1]
					qId = [dNumber, qNumber]
					out = self.beginUnit (qId, qType, thisQGroupDesc, curQuestion, out)  	
					out = self.formatQuestion (qId, qType, thisQGroupDesc, curQuestion, out)  	
					out = self.formatChoiceAndAnswer (qId, qType, thisQGroupDesc, curChoiceList, curAns, out)  	
					out = self.formatFeedback (qId, qType, thisQGroupDesc, curFeedback, out)
					out =  self.formatMarks (qId, qType, thisQGroupDesc, curMarks, out)  	
					self.endUnit (qId, qType, thisQGroupDesc, curQuestion, out)  	
		if self.qBank:
			self.formatEpilog () 

	def formatQuestion (self, qId, qType, thisGroupDesc, curQuestion, out): 
		pass

	def formatFeedback (self, qId,  qType, thisGroupDesc, curFeedback, out):  	
		pass

	def formatChoiceAndAnswer (self, qId, qType, thisGroupDesc, curChoice, 
					curAns, out):  	
		pass

	def formatMarks (self, qId, qType, thisGroupDesc, curmarks, out):  	
		pass

.*',self.curLine)
			skip =	 isItEmpty or isItComment
			if  not skip:
				 break 
		return self.curLine
				
		

	def getLineNum(self):
		return (self.curLineNum)
    


   
 
   
