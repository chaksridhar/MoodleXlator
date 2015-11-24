mport parseFile
import fileReader
import sys, getopt

parseFile=parseFile.parseFile

class DynamicImporter:
    def __init__(self, module_name, class_name,desc, fWritePtr):
		module = __import__(module_name)
		my_class = getattr(module, class_name)
		instance = my_class(desc, fWritePtr)
		instance.execFormatter()

if __name__ == "__main__":
	inputFile = ''
   	outputFile = ''
	opts, args = getopt.getopt(sys.argv[1:],"i:o:f:")
	if not opts:
		print "ERROR: No input supplied"
		print 'USAGE: python moodleXmlGen -i <inputfile> -o <outputfile>'
		sys.exit()
	fmt = "XML"
	for opt, arg in opts:
		if opt == '-h':
			print 'python moodleXmlGen -i <inputfile> -o <outputfile>'
			sys.exit()
		elif opt  == '-i':
			inputFile = arg
		elif opt  == '-o':
		 	outputFile = arg
		elif opt  == '-f':
			print "in fmt"
			fmt = arg
		else:
			print "In correct usage"
			print "python moodleXmlGen -i <inputfile> -o <outputfile>"
	if fmt != "XML" :
		print "ABORT: Outputing in  <%s> format not supported. Only xml foarmat currently supported" %(fmt)
		sys.exit()

	FileLineReader = fileReader.FileLineReader
	lineReader = FileLineReader(inputFile) 
	if outputFile:
		fWritePtr =  open(outputFile, 'w')
		if not fWritePtr:
			print "ABORT: Unable to open %s for writing" %(outputFile)
			sys.exit()
	else:
		fWritePtr = sys.stdout

	qBank = parseFile(lineReader)
 	DynamicImporter("formatXml", "FormatXml", qBank, fWritePtr)
