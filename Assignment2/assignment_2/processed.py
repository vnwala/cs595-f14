def isInside(arrayOfItems, entry):
	for line in arrayOfItems:
		if( line == entry ):
	        	return True
	return False

inputFileForDuplicates = open("OKAYUrl.txt","r")
inputFileArray = inputFileForDuplicates.readlines()


outputFileForNonDuplicates = open('NonDup.txt','w')
outputFileArray = []



for line in inputFileArray:

	line = line.strip()#remove spaces at the end
	line = line.lower()#convert to lowercase
	#print line

	if( isInside(outputFileArray, line) == False ):
		outputFileArray.append(line)
	print outputFileArray
	

outputFileForNonDuplicates.write('\n'.join(str(line) for line in outputFileArray))
