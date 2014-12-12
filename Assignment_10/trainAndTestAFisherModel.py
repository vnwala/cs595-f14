import docclass
import feedfilter


def trainingModel(dictionaryOfTitleAndClass):
	cl=docclass.fisherclassifier(docclass.getwords)
	cl.setdb('politics_feed.db') # Only if you implemented SQLite
	feedfilter.readNonInteractive(dictionaryOfTitleAndClass,'politics_search.xml',cl)

def testingModel(dictionaryOfTitleAndClass):
	cl=docclass.fisherclassifier(docclass.getwords)
	cl.setdb('politics_feed.db') # Only if you implemented SQLite
	feedfilter.readNonInteractiveTesting(dictionaryOfTitleAndClass,'politics_search2.xml',cl)

def getInput(inputFileName):
	inputFile = open(inputFileName, 'r')
	mainSourceDataLines = inputFile.readlines()

	dictionaryOfTitleAndClass = {}
	#arrayOfTitles = []

	for line in mainSourceDataLines:

		data = line.split('<----->')
		title = data[0].strip()
		classValue = data[2].strip().lower()

		title = title.lower()
		dictionaryOfTitleAndClass[title] = classValue


		#arrayOfTitles.append(title)

	'''
	arrayOfTitles.sort()
	for l in arrayOfTitles:
		print l
	'''

	return dictionaryOfTitleAndClass


	


#dictionaryOfTitleAndClass = getInput('50FirstHalf.txt')
#print len(dictionaryOfTitleAndClass)
#trainingModel(dictionaryOfTitleAndClass)


dictionaryOfTitleAndClass = getInput('50SecondHalf.txt')
print len(dictionaryOfTitleAndClass)
testingModel(dictionaryOfTitleAndClass)
