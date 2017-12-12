
# stockvolume.py

import nmf
import urllib
from numpy import *

tickers = ['YHOO', 'AVP', 'BIIB', 'BP', 'CL', 'CVX', \
	   'DNA', 'EXPE', 'GOOG', 'PG', 'XOM', 'AMGN']

shortest = 300
prices = {}
dates = None

for t in tickers:
	row = urllib.urlopen('http://ichart.finance.yahoo.com/table.csv?'+\
                       's=%s&d=11&e=26&f=2006&g=d&a=3&b=12&c=1996'%t +\
                       '&ignore=.csv').readlines()
	prices[t] = [float(r.split(',')[5]) for r in rows[1:] if r.strip() != '']
	if len(prices[t])<shortest:
		shortest = len(prices[t])

	if not dates:
		dates = [r.split(',')[0] for r in rows[1:] if r.strip() != '']

l1 = [[prices[tickers[i]][j] for i in range(len(tickers))] for j in range(shortest)]

w, h = nmf.factorize(matrix(l1), pc=5)

print(h)
print(w)

for i in range(shape(h)[0]):
	print('Feature %d' %i)
	o1 = [(h[i,j], tickers[j]) for j in range(shape(h)[1])]
	o1.sort()
	o1.reverse()
	for j in range(12):
		print(o1[j])
	print()

	porder = [(w[d,i], d) for d in range(300)]
	porder.sort()
	porder.reverse()
	print([(p[0], dates[p[1]]) for p in porder[0:3]])
	print()





























