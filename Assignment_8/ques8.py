from math import sqrt
import os, sys




def loadMovieLens(path='/home/vnwala/ml-100k/'):
  # Get movie titles
    movies = {}
    for line in open(path + 'u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id] = title
  # Load data
    prefs = {}
    for line in open(path + 'u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        #prefs[user][movies[movieid]] = float(rating)
        prefs[user][movieid] = float(rating)
    return prefs, movies

prefs, movies = loadMovieLens()



def sim_pearson(prefs,p1,p2):
    # Get the list of mutually rated shared_items
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1

    # Find the number of elements
    n=len(si)

    # if they have no ratings in common, return 0
    if n==0: return 0

    # Add up all the preferences
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    # Sum up the products
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

    # Calculate Pearson score
    num=pSum-(sum1*sum2/n)
    den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0

    r=num/den

    return r









def topMatches(prefs,person,n=5,similarity=sim_pearson, reverseSimilarityFlag=True):
    scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]

    # Sort the list so the highest scores appear at the top
    scores.sort()

    if( reverseSimilarityFlag ):
        scores.reverse()

    return scores[0:n]






def calculateSimilarItems(prefs, similarityMetric, n=10, reverseSimilarityFlag=True, transformMatrixFlag=True):
    '''
    Create a dictionary of items showing which other items they are
    most similar to.
    '''

    result = {}
    # Invert the preference matrix to be item-centric

    if( transformMatrixFlag ):
        #with transform: movie top similarity
        itemPrefs = transformPrefs(prefs)
    else:
        #without transform: user top similarity
        itemPrefs = prefs

    #c = 0
    for item in itemPrefs:

        scores = topMatches(itemPrefs, item, n=n, similarity=similarityMetric, reverseSimilarityFlag=reverseSimilarityFlag)
        
        result[item] = scores
    return result


def sim_distance(prefs,person1,person2):
    # Get the list of shared_items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    # if they have no ratins in common, return 0
    if len(si)==0: return 0

    # Add up the squares of all the differences
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in si])

    return 1/(1+sqrt(sum_of_squares))








#method 1: distance metric
userSimilarityMatrix = calculateSimilarItems(prefs=prefs, similarityMetric=sim_distance, n=5, reverseSimilarityFlag=True, transformMatrixFlag=False) #reverseSimilarityFlag=True: largest to smallest
#userSimilarityMatrix = calculateSimilarItems(prefs=prefs, n=5, reverseSimilarityFlag=True, transformMatrixFlag=False, similarity=sim_pearson)

#print len(userSimilarityMatrix)
userSimilarityArrayOfTuples = []
for userId, userAttr in userSimilarityMatrix.items():

    totalSimilarity = 0
    similarUsersArray = []
    for scoreAnduserId in userAttr:
        score = scoreAnduserId[0]
        userId = scoreAnduserId[1]

        similarUsersArray.append(userId)
        totalSimilarity = totalSimilarity + score

    userTupleData = (userId, similarUsersArray, totalSimilarity )
    userSimilarityArrayOfTuples.append(userTupleData)


count = 0
for userTuple in userSimilarityArrayOfTuples:

    userId = userTuple[0]
    userSimilarItems = userTuple[1]
    totalSim = userTuple[2]


    #any one of these qualifies
    #pick largest totalSim

    print userId, userSimilarItems, totalSim

print 'count: ', count

