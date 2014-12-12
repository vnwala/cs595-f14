
'''
Reads from 2 sources entry1.txt and classifier2.txt and consolidates data
and writes into a new file mainSourceData.txt
'''

outputFile = open('mainSourceData.txt', 'w')

entry1File = open('entry1.txt', 'r')
classifier2File = open('classifier2.txt', 'r')

entry1Lines = entry1File.readlines()
classifier2Lines = classifier2File.readlines()

if( len(entry1Lines) == len(classifier2Lines) ):

	for i in range(0, len(entry1Lines) ):

		data = entry1Lines[i].split('-----')

		title = data[0].strip()
		summary = data[1].strip()
		classValue = classifier2Lines[i].strip()

		#print title, classValue
		outputFile.write(title + '<----->' + summary + '<----->' + classValue + '\n')


outputFile.close()
entry1File.close()
classifier2File.close()
		

