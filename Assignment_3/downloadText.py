import hashlib
from hashlib import md5
import os

fh = open("UniqueURLS.txt",'r')

for line in fh:
	url=line
	url=url.replace('\n','')




	def computeMD5hash(message):
		m = hashlib.md5()
		m.update(message)
		return m.hexdigest()


	hashMessage = computeMD5hash(url)
	print hashMessage

	os.system("lynx -dump -force_html " + url+ "  > /home/vnwala/TextFiles/" + hashMessage  +".processed"+ ".txt ")






























