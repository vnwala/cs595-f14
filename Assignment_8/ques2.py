from collections import Counter
from collections import defaultdict
from operator import itemgetter, attrgetter
from collections import OrderedDict

path='/home/vnwala/ml-100k'
def getMovieData():
	movie = {}
	for line in open(path + '/u.data'):
		(user, movieid, rating, ts) = line.split('\t')

		if( movieid in movie ):
			movie[movieid].append(float(rating))
		else:
			movie[movieid] = []
			movie[movieid].append(float(rating))

	return movie

movie = getMovieData()

sums2 = {}

for movieid in movie:	
	a = len(movie[movieid])
	if( movieid in movie ):
		sums2[movieid] = a
	else:
		sums2[movieid] = a
sums2 = sorted(sums2.items(), key=lambda x: x[1])
print sums2

