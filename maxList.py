# Max of a list of numbers recurrsively


def sumlist(a,b):
	try:
		temp = a.pop(0)
		b = max(b, temp)
		print b
		sumlist(a,b) 
	except IndexError:
		return b
	
a = [15,45,88888,96,6513,648251,77]
b = 0
sumlist(a,b)