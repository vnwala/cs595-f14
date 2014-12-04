import requests
import urlparse

def getUniqueBlogs(countOfBlogsToRetrieve):

	listOfBlogs = []
	if( countOfBlogsToRetrieve>0 ):

		try:
			outputFile = open('blogs.txt', 'w')
			outputFile.write('http://f-measure.blogspot.com/\n')
			outputFile.write('http://ws-dl.blogspot.com/\n')
		except:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(fname, exc_tb.tb_lineno, sys.exc_info() )

		while len(listOfBlogs) != countOfBlogsToRetrieve:

			print 'retrieved: ', len(listOfBlogs)
			
			blogUrl = 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117'
			response = ''
			try:
				response = requests.head(blogUrl, allow_redirects=True)
				response = response.url
			except:
				response = ''


			if len(response) > 0:
				if response not in listOfBlogs:

					response = response.lower()
					
					parsedUrl = urlparse.urlparse(response)
					parsedUrl = parsedUrl.scheme + '://' + parsedUrl.netloc + '/'

					listOfBlogs.append(parsedUrl)
					outputFile.write(parsedUrl + '\n')

		outputFile.close()

getUniqueBlogs(98)
