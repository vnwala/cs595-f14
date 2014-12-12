import feedparser
import re


def interestingwords(s):
  splitter = re.compile(r'\W*')
  return [s.lower() for s in splitter.split(s) if len(s) > 2 and len(s) < 20]


def entryfeatures(entry):
  f = {}

  # extract title
  titlewords = interestingwords(entry['title'])
  for w in titlewords: f['Title:' + w] = 1

  # extract summary
  summarywords = interestingwords(entry['summary'])

  # count uppercase words
  uc = 0
  for i in range(len(summarywords)):
    w = summarywords[i]
    f[w] = 1
    if w.isupper(): uc += 1

    # get word pairs in summary aas features
    if i < len(summarywords) - 1:
      twowords = ' '.join(summarywords[i:i+1])
      f[twowords] = 1

  # keep creator and publisher as a whole
  f['Publisher:' + entry['publisher']] = 1

  # Insert virtual keyword for uppercase words
  if float(uc) / len(summarywords) > 0.3: f['UPPERCASE'] = 1

  print f.keys()
  return f.keys()

def readNonInteractive(dictionaryOfTitleActualClassValues, feed, classifier):
  print '...training'
  f = feedparser.parse(feed)
  for entry in f['entries']:
    fulltext = '%s\n%s' % (entry['title'], entry['summary'])
    #print dictionaryOfTitleActualClassValues
    
    titleFromXML = entry['title'].strip().lower()
    titleFromXML1 = entry['summary'].strip().lower()
    if titleFromXML1 in dictionaryOfTitleActualClassValues:
      groundTruth = dictionaryOfTitleActualClassValues[titleFromXML1]

      print 'here'
      print titleFromXML, groundTruth
      classifier.train(fulltext, groundTruth)
      
  print '...done training'

def readNonInteractiveTesting(dictionaryOfTitleActualClassValues, feed, classifier):
  print '...testing'

  outputFile = open('myPredictionsFile.txt', 'w')
  
  f = feedparser.parse(feed)
  for entry in f['entries']:

    titleFromXML = entry['title'].strip().lower()
    titleFromXML1 = entry['summary'].strip().lower()
    fulltext = '%s\n%s' % (entry['title'], entry['summary'])
    
    if titleFromXML1 in dictionaryOfTitleActualClassValues:

      actualValue = dictionaryOfTitleActualClassValues[titleFromXML1]

      prediction = str(classifier.classify(fulltext))
      cprobValue = classifier.getCProb()

      print actualValue, prediction, cprobValue
      outputFile.write(titleFromXML + '&' + titleFromXML1[:20] + '&' + actualValue + '&' + prediction + '&' + str(cprobValue) + '\\' + '\n')

  outputFile.close()

      

  print '...done testing'
  



def read(feed, classifier):
 #out = open('mainSourceData.txt, 'w') 
  f = feedparser.parse(feed)
  for entry in f['entries']:
    print
    print '----'
    print 'Title:     ' + entry['title'].encode('utf-8')
    #print 'Publisher: ' + entry['publisher'].encode('utf-8')
    print
    print entry['summary'].encode('utf-8')
    #summary = entry['summary'].split.()
    #summary = entry['summary'].encode('ascii','ignore')
    #title = entry['title'].split.()
    #title = entry['title'].encode('ascii','ignore')
    fulltext = '%s\n%s' % (entry['title'], entry['summary'])
    #out.write(title + '<----->'+summary)
    #out.write('\n')
    #print 'Guess: ' + str(classifier.classify(fulltext))

    #cl = raw_input('Enter category: ')
    classifier.train(fulltext, cl)

    print 'Guess: ' + str(classifier.classify(fulltext))

    #cl = raw_input('Enter category: ')
    #classifier.train(entry, cl)
    classifier.train(fulltext, cl)
