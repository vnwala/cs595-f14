import tweepy
import simplejson
from tweepy import OAuthHandler
import itertools
import time

access_token = "384946837-FuQQRJrNFNN8BXyOToG6D1opwRIX1ZQjnysTDjZo"
access_token_secret = "IY1O1Ck8QHZ9rt9XlkkWUhcbRpnfPAN9euOZ3ndc4Gznn"
consumer_key = "mRpX89WMtUSEZSDGi6jtxd5KU"
consumer_secret = "SZyHZiSwQfFMLq5fMwHJTxWqYgfqL9o3AQXdOTP6B4ocQloi9A"


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('phonedude_mln')
k = user.screen_name
i = user.friends_count
saveFile = open('friends.txt','a')
saveFile.write(k + ' ' + str(i) )
saveFile.write('\n')
for friend in user.friends(count=i):
	j = friend.screen_name
	print j
	user = api.get_user(j)
	k = user.screen_name
	i = user.friends_count
	saveFile.write(k + ' ' + str(i) )
	saveFile.write('\n')
	#time.sleep(15)
saveFile.close()


