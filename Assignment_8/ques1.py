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

sums = {}

for movieid in movie:	
	a = sum(movie[movieid])/len(movie[movieid])
	if( movieid in movie ):
		sums[movieid] = a
	else:
		sums[movieid] = a

sums = sorted(sums.items(), key=lambda x: x[1])
print sums
