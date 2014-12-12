import docclass
import feedfilter
cl=docclass.fisherclassifier(docclass.getwords)
cl.setdb('politics_feed.db') # Only if you implemented SQLite
feedfilter.read('politics_search.xml',cl)
