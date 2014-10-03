import os
import glob
import subprocess
import re
from decimal import *

fh = glob.glob("/home/vnwala/TextFiles/*.txt")
for line in fh:
	url=line
	url=url.replace('\n','')
	proc = subprocess.Popen(["wc -w " + url], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
	index = out.find(" ")
	index = out[:index]
	proc = subprocess.Popen(["grep -c 'football' " + url], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
	number = out
	number=number.replace('\n','')
	if (number > "0" and index > "0"):
		
		TF =(float(number)/int(index))
    		k = str(TF) + '\t' + url
		print k
    		saveFile = open('tpCal.txt','a')
        	saveFile.write(k)
		saveFile.write('\n')
		saveFile.close()
            
    
    








