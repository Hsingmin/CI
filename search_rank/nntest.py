
# nntest.py

import nn

mynet = nn.searchnet('nn.db')
mynet.maketables()
wWorld,wRiver,wBank = 101,102,103
uWorldBank,uRiver,uEarth = 201,202,203
mynet.generatehiddennode([wWorld,wBank],[uWorldBank,uRiver,uEarth])

print('wordhidden layer0 : ')
for c in mynet.con.execute('select * from wordhidden'):
	print(c)

print('hiddenurl layer1 : ')
for c in mynet.con.execute('select * from hiddenurl'):
	print(c)

print('before trainning -- get weights of searching word : ')
print(mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth]))

print('train net -- get weights of searching word : ')
mynet.trainquery([wWorld,wBank],[uWorldBank,uRiver,uEarth],uWorldBank)
print(mynet.getresult([wWorld,wBank],[uWorldBank,uRiver,uEarth]))

print('multi-tries to train the network : ')
allurls = [uWorldBank, uRiver, uEarth]
for i in range(30):
	mynet.trainquery([wWorld,wBank], allurls, uWorldBank)
	mynet.trainquery([wRiver,wBank], allurls, uRiver)
	mynet.trainquery([wWorld], allurls, uEarth)

print('get result of [wWorld,wBank], allurls')
print(mynet.getresult([wWorld,wBank], allurls))

print('get result of [wRiver,wBank], allurls')
print(mynet.getresult([wRiver,wBank], allurls))

print('get result of [wBank], allurls')
print(mynet.getresult([wBank], allurls))



























