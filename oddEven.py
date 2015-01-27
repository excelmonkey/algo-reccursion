# odd-even recursive spit

def oddEvenList(a, oddList, evenList):
	try:
		temp = a.pop(0)
		if temp%2 > 0:
			oddList.append(temp)
		else:
			evenList.append(temp)
		oddEvenList(a, oddList, evenList) 
	except IndexError:
		print a
		print oddList
		print evenList
		return
	
a = [0,15,45,88888,96,6513,648251,77]
oddList = []
evenList = []
oddEvenList(a, oddList, evenList)