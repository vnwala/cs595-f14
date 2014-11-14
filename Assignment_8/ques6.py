from math import sqrt
import os, sys


def loadMovieLens(path='/home/vnwala/ml-100k/'):
    movies = {}
    for line in open(path + 'u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title
    prefs = {}
    for line in open(path + 'u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movieid] = float(rating)
    return prefs, movies


def aggregateMovieAndUserData(path='/home/vnwala/ml-100k/'):

    try:

        movies = {}
        aggregateMovieData = []
        for line in open(path + 'u.item'):
            (id, title) = line.split('|')[0:2]
            movies[id] = (title, [], -1)

        users = {}

        for line in open(path + 'u.data'):
            (user, movieid, rating, ts) = line.split('\t')

            user = user.strip()
            movieid = movieid.strip()
            rating = rating.strip()
            ts = ts.strip()

            users.setdefault(user, {})
            users[user][movieid] = float(rating)

            movies[movieid][1].append(float(rating))

        for movieId, tupleData in movies.items():
            averageRating = sum(tupleData[1]) / float(len(tupleData[1]))

            movietuples = (movieId, tupleData[0], averageRating, len(tupleData[1]))
            aggregateMovieData.append(movietuples)


        aggregateUserData = []
        for line in open(path + 'u.user'):
            (userId, age, gender, occupation, zipCode) = line.split('|')
            userTuples = (userId, gender, age, users[userId])
            aggregateUserData.append(userTuples)
            

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(fname, exc_tb.tb_lineno, sys.exc_info() )
        return



    return aggregateMovieData, aggregateUserData, movies


def getHighestRatedMovies(movies, count):

    if( count > 0 and count < len(movies) ):
        movies = sorted(movies, key=lambda tup: tup[2], reverse=True)
        i = 1
        for movie in movies:
            print movie

            if( i == count ):
                break
            i = i + 1


def getFemaleAndMaleData(aggregateUsers):
    aggregateUsersFemale = []
    aggregateUsersMale = []
    if( len(aggregateUsers) > 0 ):

        for user in aggregateUsers:
            if( user[1] == 'F' ):
                aggregateUsersFemale.append(user)
            else:
                aggregateUsersMale.append(user)


    return aggregateUsersFemale, aggregateUsersMale



def getHighestMovieRaters(aggregateUsers, count):

    if( len(aggregateUsers) > 0 and count > 0 ):
        raterIDRatedMoviesCount = []

        for rater in aggregateUsers:

            #raterTuple: rater id, number of movies rated
            raterTuple = (rater[0], len(rater[3]))
            raterIDRatedMoviesCount.append(raterTuple)

        raterIDRatedMoviesCount = sorted(raterIDRatedMoviesCount, key=lambda tup: tup[1], reverse=True)

        i = 1
        for rater in raterIDRatedMoviesCount:
            print rater[0], rater[1]

            if( i == count ):
                break
            i = i + 1


aggregateMovies, aggregateUsers, movies = aggregateMovieAndUserData()

aggregateUsersFemale, aggregateUsersMale = getFemaleAndMaleData(aggregateUsers)

getHighestMovieRaters(aggregateUsers, 5)



