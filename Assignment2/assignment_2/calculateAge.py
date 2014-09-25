import time
import datetime
import calendar

fh = open("time.txt",'r')

for line in fh:
	date=line
	try:
		def getLowest(date):
	                date = date.split(" ")
			date[-1] = date[-1][:18]
			date = " ".join(date)
			epoch = int(calendar.timegm(time.strptime(date, '%Y-%m-%dT%H:%M:%S')))
			
			t2 = int(time.time())-epoch
			day = (t2/86400)
			return day
		k = getLowest(date) 
		print k
		saveFile = open("day.txt",'a')
		saveFile.write(str(k))
		saveFile.write('\n')
		saveFile.close()
	except BaseException, e:
		print e


fh.close()
