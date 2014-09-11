import time 
import sys
import urllib2
from bs4 import BeautifulSoup


def extractScores(school, seconds, url):
        count = 1
        while ( count > 0):
		seconds = float (seconds)
		soup = BeautifulSoup(urllib2.urlopen(url).read())
		for row in soup('table')[1].findAll('tr', {'class':'game  link'}):
			away = row.find('td', {'class':'away'})
			away = away.em.text

			awayScore = row.find('td', {'class':'score'}).findAll('span')
			awayScore = awayScore[0].text
		
			home = row.find('td', {'class':'home'})
			home =  home.em.text

	
			homeScore = row.find('td', {'class':'score'}).findAll('span')
			homeScore = homeScore[1].text
		
		        if (away.lower() == school.lower() or home.lower() == school.lower()):

		 		print away + " "+ awayScore + "," + home+ " " + homeScore
		        
		       		time.sleep(seconds)
		count = count + 1

if len(sys.argv) == 4:
	extractScores(sys.argv[1],sys.argv[2],sys.argv[3])
else:
	print "Error, wrong argument count, do this instead: ", sys.argv[0] + " schoolName, time and url"
	
    
