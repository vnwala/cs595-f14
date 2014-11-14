def aggregateMovieAndUserData(path='/home/vnwala/ml-100k/'):

    try:

        movies = {}
        aggregateMovieData = []
        for line in open(path + 'u.item'):
            (id, title) = line.split('|')[0:2]
            movies[id] = (title, [], -1)

        users = {}
        #populate user and movie data

        for line in open(path + 'u.data'):
            (user, movieid, rating, ts) = line.split('\t')

            user = user.strip()
            movieid = movieid.strip()
            rating = rating.strip()
            ts = ts.strip()

            users.setdefault(user, {})
            #movie title: movies[movieid][0]
            users[user][movieid] = float(rating)#key is movie title

            '''
            if( user in users ):
                users[user][movies[movieid][0]] = float(rating)
            else:
                users[user] = {}
            '''

            
            #movies[movieid]: (title, [ArrayOfRatings])
            #movies[movieid][0]: title
            #movies[movieid][1]: array of ratings
            movies[movieid][1].append(float(rating))



        #process movie data
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




def getHighestRatedMoviesByMenOrWomenUnderAge(aggregateUsersFemaleOrMale, count, ageLimit, movies):

    if( count > 0 and count < len(aggregateUsersFemaleOrMale) and ageLimit > 0 and len(movies) > 0 ):
        tupleOfMovieRatingDictionary = {}
        movieAverageRatingArrayOfTuples = []
        for user in aggregateUsersFemaleOrMale:
            if( int(user[2]) < ageLimit ):
                
                for movie, rating in user[3].items():
                    
                    if( movie in tupleOfMovieRatingDictionary ):
                        tupleOfMovieRatingDictionary[movie].append(rating)
                    else:
                        tupleOfMovieRatingDictionary[movie] = []
                        tupleOfMovieRatingDictionary[movie].append(rating)

        for movie, ratingsArray in tupleOfMovieRatingDictionary.items():
            averageRating = sum(ratingsArray) / float(len(ratingsArray))

            movieRatingTuple = (movie, averageRating)
            movieAverageRatingArrayOfTuples.append(movieRatingTuple)


        movieAverageRatingArrayOfTuples = sorted(movieAverageRatingArrayOfTuples, key=lambda tup: tup[1], reverse=True)

        i = 1
        for movieData in movieAverageRatingArrayOfTuples:
            print movies[movieData[0]][0], movieData[1]

            if( i == count ):
                break
            i = i + 1

#input:
    #aggregateUsers: [ (user id, gender, Age, {'movie_title': movie rating}) ]







def getHighestRatedMoviesByMenOrWomenOverAge(aggregateUsersFemaleOrMale, count, ageLimit, movies):

    if( count > 0 and count < len(aggregateUsersFemaleOrMale) and ageLimit > 0 and len(movies) > 0 ):
        tupleOfMovieRatingDictionary = {}
        movieAverageRatingArrayOfTuples = []

        for user in aggregateUsersFemaleOrMale:

            if( int(user[2]) > ageLimit ):
                for movie, rating in user[3].items():
                    
                    if( movie in tupleOfMovieRatingDictionary ):
                        tupleOfMovieRatingDictionary[movie].append(rating)
                    else:
                        tupleOfMovieRatingDictionary[movie] = []
                        tupleOfMovieRatingDictionary[movie].append(rating)


        #average ratings
        for movie, ratingsArray in tupleOfMovieRatingDictionary.items():
            averageRating = sum(ratingsArray) / float(len(ratingsArray))

            movieRatingTuple = (movie, averageRating)
            movieAverageRatingArrayOfTuples.append(movieRatingTuple)

        #sort
        movieAverageRatingArrayOfTuples = sorted(movieAverageRatingArrayOfTuples, key=lambda tup: tup[1], reverse=True)

        i = 1
        for movieData in movieAverageRatingArrayOfTuples:
            print movies[movieData[0]][0], movieData[1]

            if( i == count ):
                break
            i = i + 1

aggregateMovies, aggregateUsers, movies = aggregateMovieAndUserData()

aggregateUsersFemale, aggregateUsersMale = getFemaleAndMaleData(aggregateUsers)

getHighestRatedMoviesByMenOrWomenOverAge(aggregateUsersMale, 5, 40, movies)
print ''
getHighestRatedMoviesByMenOrWomenUnderAge(aggregateUsersMale, 5, 40, movies)
