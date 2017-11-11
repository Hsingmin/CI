
# generatefeedvector.py

import feedparser
import re

# get a dict including RSS title and word counts
def getwordcounts(url):
	d = feedparser.parse(url)
	wc = {}

	# traverse all items
	for e in d.entries:
		if 'summary' in e:
			summary = e.summary
		else:
			summary = e.description

	words = getwords(e.title + ' ' + summary)
	for word in words:
		wc.setdefault(word, 0)
		wc[word] += 1
	
	return d.feed.title, wc

# dispatch clean word from summary
def getwords(html):
	# delete html label
	txt = re.compile(r'<[^>]+>').sub('', html)

	# split word
	words = re.compile(r'[^A-Z^a-z]+').split(txt)

	return [word.lower() for word in words if word != '']

# traverse RSS to generate dataset

apcount = {}
wordcounts = {}
feedlist = [line in file('feedlist.txt')]
for feedurl in feedlist:
	title, wc = getwordcouts(feedurl)
	wordcounts[title] = wc
	for word, count in wc.items():
		apcount.setdefault(word, 0)
		if count > 1:
			apcount[word] += 1

			









































