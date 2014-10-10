from bs4 import BeautifulSoup
import urllib2
import re
import sys, traceback
import hashlib
fh = open("altUrl.txt",'r')

for line in fh:
	url=line
	url=url.replace('\n','')
	try:
		html_page = urllib2.urlopen(url)
		soup = BeautifulSoup(html_page)
		def computeMD5hash(message):
			m = hashlib.md5()
			m.update(message)
			return m.hexdigest()
		hashMessage = computeMD5hash(url)
		saveFile = open("/home/vnwala/URLs/"+hashMessage+".txt",'a')
		saveFile.write('site')
		saveFile.write('\n')
		saveFile.write(url)
		saveFile.write('\n')
		saveFile.write('links')
		saveFile.write('\n')
		saveFile.close()
		for link in soup.findAll('a'):
			i = link.get('href')
			try:
				if i.find('http') == 0:
					print 'abc'
					saveFile = open("/home/vnwala/URLs/"+hashMessage+".txt",'a')
					saveFile.write(str(i))
					saveFile.write('\n')
					saveFile.close()
			except:
				print sys.exc_type, sys.exc_value , sys.exc_traceback
	except:
		print sys.exc_type, sys.exc_value , sys.exc_traceback

