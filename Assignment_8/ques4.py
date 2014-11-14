path='/home/vnwala/ml-100k'
user1 = {}
movie = {}
male_raters ={}

for line in open(path + '/u.user'):
	(userid , age, gender, occupation, zipcode) = line.split('|')
	if( gender ==  'M' ):
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
	male_raters[movieid] = len(movie[movieid])

male_raters = sorted(male_raters.items(), key=lambda x: x[1])

print male_raters

