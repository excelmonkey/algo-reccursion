# split a list into two halves recursively using every second element

from __future__ import division

def splitList(a, topList, bottomList):
	try:
		temp = a.pop(0)
		if len(topList) == len(bottomList):
			topList.append(temp)
		elif len(topList) > len(bottomList):
			bottomList.append(temp)
		splitList(a, topList, bottomList) 
	except IndexError:
		print a
		print topList
		print bottomList
		return
	
a = [0,15,45,88888,96,6513,648251,77]
topList = []
bottomList = []

#splitList(a, topList, bottomList)


######
# split a list into two halves recursively

def splitListAgain(a, topList, bottomList, index):
	try:
		temp = a.pop(0)
		if len(topList) < index // 2: # Note: the floor division operator here '//'
			topList.append(temp)
		else:
			bottomList.append(temp)
		splitListAgain(a, topList, bottomList, index) 
	except IndexError:
		print a
		print topList
		print bottomList
		return
	
#a = [0,15,45,88888,96,6513,648251,77]
a = ["sfd", "sdf", "awed", "afdf", "sgfg", "sgsdg", "kgv", "asdhjkb"]
topList = []
bottomList = []
index = len(a)

splitListAgain(a, topList, bottomList, index)
