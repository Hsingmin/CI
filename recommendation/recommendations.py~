
# recommendations.py

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}

from math import sqrt

# euclidean distance
def sim_distance(prefs, person1, person2):
	si = {}

	# check similarity between person1 and person2
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1

	if len(si) == 0:
		return 0

	# only common items considered
	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) \
				for item in prefs[person1] if item in prefs[person2]])

	return (1/(1+sqrt(sum_of_squares)))

# pearson distance
def sim_pearson(prefs, p1, p2):

	# store common items for p1 and p2
	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]:
			si[item] = 1

	n = len(si)

	if n == 0:
		return 0

	sum1 = sum([prefs[p1][it] for it in si])
	sum2 = sum([prefs[p2][it] for it in si])

	sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
	sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

	pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

	num = pSum - (sum1*sum2/n)
	den = sqrt((sum1Sq-pow(sum1, 2)/n) * (sum2Sq-pow(sum2, 2)/n))

	if den == 0:
		return 0

	r = num/den
	return r

# another pearson distance 
def sim_another_pearson(prefs, p1, p2):

	si = {}
	for item in prefs[p1]:
		if item in prefs[p2]:
			si[item] = 1

	n = len(si)
	if n == 0:
		return 0

	aver1 = sum([prefs[p1][it] for it in si])/n
	aver2 = sum([prefs[p2][it] for it in si])/n

	cov = sum([(prefs[p1][it]-aver1)*(prefs[p2][it]-aver2) for it in si])/(n-1)

	delt1 = sqrt(sum([pow(prefs[p1][it]-aver1, 2) for it in si])/(n-1))
	delt2 = sqrt(sum([pow(prefs[p2][it]-aver2, 2) for it in si])/(n-1))

	if not(delt1 and delt2):
		return 0

	corr = cov/(delt1*delt2)

	return corr

# topMatches
def topMatches(prefs, person, n = 5, similarity = sim_another_pearson):
	scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]

	scores.sort()
	scores.reverse()
	return scores[0:n]










