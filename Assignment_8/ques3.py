path='/home/vnwala/ml-100k'
user1 = {}
movie = {}
female_raters ={}

for line in open(path + '/u.user'):
	(userid , age, gender, occupation, zipcode) = line.split('|')
	if( gender ==  'F' ):
		user1[userid] = (age, gender, occupation, zipcode)
		
		
		
		for line in open(path + '/u.data'):
			(user, movieid, rating, ts) = line.split('\t')
			if (user == userid):
				if( movieid in movie ):
					movie[movieid].append(userid)
				else:
					movie[movieid] = []
					movie[movieid].append(userid)
for movieid in movie:
	female_raters[movieid] = len(movie[movieid])

female_raters = sorted(female_raters.items(), key=lambda x: x[1])

print female_raters

