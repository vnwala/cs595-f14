from bs4 import BeautifulSoup
import urllib2
import re
import sys, traceback
import hashlib
from urlparse import urlparse
fh = open("altUrl.txt",'r')

for line in fh:
	url=line
	url=url.replace('\n','')
	try:
		html_page = urllib2.urlopen(url)
		soup = BeautifulSoup(html_page)
		saveFile = open("gephi_new.txt",'a')
		saveFile.close()
		for link in soup.findAll('a'):
			i = link.get('href')
			try:
				if i.find('http') == 0:
					
					saveFile = open("gephi_new.txt",'a')
					saveFile.write( '"'+str(i)+'"'+' '+"->"+' '+'"' + url+ '"'+ ';' )
					k = urlparse(i)
					saveFile.write('\n')
					saveFile.write( '"'+str(i)+'"'+' '+"[" + "label"+ "=" + k.netloc +  "]" + ';' )
					o = urlparse(url)
					saveFile.write('\n')
					saveFile.write( '"'+url+'"'+' '+"[" + "label"+ "=" + o.netloc +  "]" + ';' )
					saveFile.write('\n')
					saveFile.close()
			except:
				print sys.exc_type, sys.exc_value , sys.exc_traceback
	except:
		print sys.exc_type, sys.exc_value , sys.exc_traceback
