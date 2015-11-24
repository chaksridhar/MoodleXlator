import os
import re
import fileReader
import dPrint
import sys, getopt

DEBUG=dPrint.DEBUG
ERROR=dPrint.ERROR
gDebugLevel = dPrint.gDebugLevel


def printQGroup (qGroupList, qType):
	if gDebugLevel == 0:
		return
	
	print "*** Entering  printQGroup printing all %s****" %(qType)
	length = len(qGroupList)
	qNumber = 0
	for   i in range (0, length):
		thisQGroup = qGroupList[i]
		thisQGroupDesc =  thisQGroup[0]
		numLinesInDesc = len(thisQGroupDesc)
		tupleList =thisQGroup[1]
		curLineDesc = [1,2]
		numTuples = len(tupleList)
		if thisQGroupDesc:
			print ("<DESCRIPTION>  %s\n</DESCRIPTION>"   %(thisQGroupDesc))
		for k in range (0, numTuples):
			qNumber = qNumber+1
			curQuestion = tupleList[k][0]
			curChoiceList = tupleList[k][1]
			curAns = tupleList[k][2]
			curFeedback = tupleList[k][3]
			curMarks  = tupleList[k][4]

			for lineNumLineContentPair in curQuestion:
				print "Q %d>> %s" %(qNumber, lineNumLineContentPair[1])

			for  curChoice  in curChoiceList:
				for lineNumLineContentPair in curChoice:
					print "C>> %s" %(lineNumLineContentPair[1])

			for lineNumLineContentPair in curAns:
				print "A>> %s" %(lineNumLineContentPair[1])

			for lineNumLineContentPair in curFeedback:
				print "F>> %s" %(lineNumLineContentPair[1])

			for lineNumLineContentPair in curMarks:
				print "Marks>> %d" %(lineNumLineContentPair[1])

