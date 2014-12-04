import sys, os
import feedparser
import re
import math

def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']

def getwordcounts(url):
	
	'''
	Returns title and dictionary of word counts for an RSS feed
	'''
	# Parse the feed


	#url: http://blogName.blogspot.com/
	d = feedparser.parse(url)


	wc = {}

	# Loop over all the entries
	for e in d.entries:
		if 'summary' in e:
			summary = e.summary
		else:
			summary = e.description

		# Extract a list of words
		words = getwords(e.title + ' ' + summary)
		for word in words:
			wc.setdefault(word, 0)
			wc[word] += 1

	return (d.feed.title, wc)

def getFeedVector500Popular(blogsFilename):

	apcount = {}
	wordcounts = {}
	feedlist = [line for line in file(blogsFilename)]

	
	
	for feedurl in feedlist:
		
		feedurl = feedurl.strip()

		try:
			
			(title, wc) = getwordcounts(feedurl + 'feeds/posts/default?max-results=500')
			wordcounts[title] = wc
			for (word, count) in wc.items():
				apcount.setdefault(word, 0)
				if count > 1:
					apcount[word] += 1

		except:
			print 'Failed to parse feed %s' % feedurl
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(fname, exc_tb.tb_lineno, sys.exc_info() )



	wordlist = []
	listOfTermTermFrequencyTuple = []
	for (t, tF) in apcount.items():

		frac = float(tF) / len(feedlist)

		if frac > 0.1 and frac < 0.5:
			ttFTuple = (t, tF)
			listOfTermTermFrequencyTuple.append(ttFTuple)


	#frequent 500 terms
	listOfTermTermFrequencyTuple = sorted(listOfTermTermFrequencyTuple, key=lambda tuple: tuple[1], reverse=True)
	for ttF in  listOfTermTermFrequencyTuple:
		t = ttF[0]
		tF = ttF[1]

		if( len(wordlist) > 500 ):
			break
		else:
			wordlist.append(t)
	

	out = file('blogVectorResult.txt', 'w')
	out.write('Blog')

	for word in wordlist:
		word = word.encode('ascii', 'ignore')
		out.write('\t%s' % word)

	out.write('\n')
	for (blog, wc) in wordcounts.items():
		
		blog = blog.encode('ascii', 'ignore')
		#print blog
		out.write(blog)
		for word in wordlist:

			word = word.encode('ascii', 'ignore')
			if word in wc:
				out.write('\t%d' % wc[word])
			else:
				out.write('\t0')
		out.write('\n')

def getFeedVector500PopularTFIDF(blogsFilename):

	apcount = {}
	wordcounts = {}
	feedlist = [line for line in file(blogsFilename)]

	
	
	for feedurl in feedlist:
		
		feedurl = feedurl.strip()

		try:
			
			(title, wc) = getwordcounts(feedurl + 'feeds/posts/default?max-results=500')
			wordcounts[title] = wc
			for (word, count) in wc.items():
				apcount.setdefault(word, 0)
				if count > 1:
					apcount[word] += 1

		except:
			print 'Failed to parse feed %s' % feedurl
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(fname, exc_tb.tb_lineno, sys.exc_info() )



	wordlist = []
	listOfTermTermFrequencyTuple = []
	for (t, tF) in apcount.items():

		frac = float(tF) / len(feedlist)

		if frac > 0.1 and frac < 0.5:
			ttFTuple = (t, tF)
			listOfTermTermFrequencyTuple.append(ttFTuple)


	#frequent 500 terms
	listOfTermTermFrequencyTuple = sorted(listOfTermTermFrequencyTuple, key=lambda tuple: tuple[1], reverse=True)
	for ttF in  listOfTermTermFrequencyTuple:
		t = ttF[0]
		tF = ttF[1]

		if( len(wordlist) > 500 ):
			break
		else:
			wordlist.append(t)
	

	out = file('blogVectorResultTFIDF.txt', 'w')
	out.write('Blog')

	for word in wordlist:
		word = word.encode('ascii', 'ignore')
		out.write('\t%s' % word)

	out.write('\n')
	for (blog, wc) in wordcounts.items():
		
		blog = blog.encode('ascii', 'ignore')
		#print blog
		out.write(blog)
		for word in wordlist:

			word = word.encode('ascii', 'ignore')
			if word in wc:

				TF = wc[word]/float(len(wc))
				IDF = len(feedlist)/float(apcount[word])

				#log base 2:
				IDF = math.log(IDF) / float(math.log(2))
				TFIDF = TF*IDF

				out.write('\t%f' % TFIDF)
			else:
				out.write('\t0')
		out.write('\n')


#p1
#getFeedVector500Popular('blogs.txt')

#p5
getFeedVector500PopularTFIDF('blogs.txt')
