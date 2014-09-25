from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import re
import urllib2
import httplib

#Variables that contains the user credentials to access Twitter API 
access_token = "384946837-aPnqh9DAtOKljCShMepwPJVg27dROGGysYuy9xog"
access_token_secret = "ow458SMzbIcAVZ3RL2nypCGYuqmkaoHTNlbZCVBiHG6FC"
consumer_key = "c3SExFZ3K6Do6Yw2Kwi84Strl"
consumer_secret = "CXobLgtdn8feYInLs659BxsjnBTCgfpmD5eEyENi1Bu6ttbfau"

saveFile = open('Freshurls.txt','a')
class StdOutListener(StreamListener):

    def on_data(self, data):
	try:

		
		url = data.split(',"url":"')[1].split('"')[0]
		url = url.replace("\/","/")
		print url

		
		
		saveFile.write(url)
		saveFile.write('\n')
		time.sleep(15)
		return True
	except BaseException, e:
		print 'failed ondata,',str(e)
		

    def on_error(self, status):
        print status
	saveFile.close()

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, StdOutListener())
stream.filter(track=["football"])
saveFile.close()


	

