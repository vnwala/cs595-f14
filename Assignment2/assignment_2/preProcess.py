import requests
import urllib2
from urlparse import urlparse
fh = open("Freshurls.txt",'r')
saveFile = open("OKAYUrl.txt",'a')
for line in fh:
	url=line
	#url=url.lower()

	try:
		def get_redirected_url(url):

		    opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
		    request = opener.open(url)
		    return request.url
		k =get_redirected_url(url)
		#i = urlparse(k)
		#i =i.netloc
		#i="http://"+i
		

                
		print k
		saveFile.write(k)
		saveFile.write('\n')
		

	except BaseException, e:
		print e
saveFile.close()
fh.close()
