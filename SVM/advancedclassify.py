
# advancedclassify.py
from matplotlib import pyplot as plt
import numpy as np
import random

class matchrow:
	def __init__(self, row, allnum=False):
		if allnum:
			self.data = [float(row[i]) for i in range(len(row)-1)]
		else:
			self.data = row[0:len(row)-1]
		self.match = int(row[len(row)-1])

def loadmatch(f, allnum=False):
	rows = []
	for line in open(f):
		rows.append(matchrow(line.split(','), allnum))

	return rows

def plotagematches(rows):
	xdm, ydm = [r.data[0] for r in rows if r.match == 1],\
		   [r.data[1] for r in rows if r.match == 1]

	xdn, ydn = [r.data[0] for r in rows if r.match == 0],\
		   [r.data[1] for r in rows if r.match == 0]

	plt.plot(xdm, ydm, 'go')
	plt.plot(xdn, ydn, 'ro')

	plt.show()


def lineartrain(rows):
	averages = {}
	counts = {}
	
	'''
	print('input rows : ')
	print(rows)	
	'''

	for row in rows:
		c1 = row.match
		averages.setdefault(c1, [0.0]*(len(row.data)))
		counts.setdefault(c1, 0)

		for i in range(len(row.data)):
			averages[c1][i] += float(row.data[i])
		counts[c1] += 1

	for c1, avg in averages.items():
		for i in range(len(avg)):
			avg[i] /= counts[c1]
	
	'''
	print('-------------------------')
	print('averages : ')
	print(averages)
	print('-------------------------')
	print('counts : ')
	print(counts)
	'''

	return averages

def dotproduct(v1, v2):
	return sum([v1[i]*v2[i] for i in range(len(v1))])

def dpclassify(point, avgs):
	b = (dotproduct(avgs[1], avgs[1]) - dotproduct(avgs[0], avgs[0]))/2
	y = dotproduct(point, avgs[0])-dotproduct(point, avgs[1]) + b
	if y > 0:
		return 0
	else:
		return 1

def yesno(v):
	if v == 'yes':
		return 1
	elif v == 'no':
		return -1
	else:
		return 0

def matchcount(interest1, interest2):
	l1 = interest1.split(':')
	l2 = interest2.split(':')
	x = 0
	for v in l1:
		if v in l2:
			x += 1

	return x

# cannot get a Yahoo API Key
def milesdistance(a1, a2):
	return ((random.random())**2)*10


def loadnumerical():
	oldrows = loadmatch('matchmaker.csv')
	newrows = []
	for row in oldrows:
		d = row.data
		data = [float(d[0]), yesno(d[1]), yesno(d[2]),\
			float(d[5]), yesno(d[6]), yesno(d[7]),\
			matchcount(d[3], d[8]), milesdistance(d[4], d[9]),\
			row.match]
		newrows.append(matchrow(data))
	return newrows

def scaledata(rows):
	low = [999999999.0]*len(rows[0].data)
	high = [-999999999.0]*len(rows[0].data)

	for row in rows:
		d = row.data
		for i in range(len(d)):
			if d[i] < low[i]:
				low[i] = d[i]
			if d[i] > high[i]:
				high[i] = d[i]

	def scaleinput(d):
		return [(d[i]-low[i])/(high[i]-low[i]) for i in range(len(low))]

	newrows = [matchrow(scaleinput(row.data)+[row.match]) for row in rows]

	return newrows, scaleinput






























