# Implementation of Beat Your Neighbour using divide and conquer


def beatNeighbour(a):
	if len(a) <= 2:
		print a
		return

	leftBox 	= 	a[len(a)/2]
	print "leftBox", (len(a)/2), "value", a[len(a)/2] 

	rightBox 	= 	a[(len(a)/2 + 1)]
	print "rightBox", (len(a)/2 + 1), "value", a[(len(a)/2 + 1)] 

	#holding array
	b = []
	
	if leftBox >= rightBox:
		for item in a[0:(len(a)/2)]:
			b.append(item)
	else:
		for item in a[(len(a)/2):len(a)]:
			b.append(item)

	a = b
	print a
	beatNeighbour(a)
	return






# Note: We would also need to handle the following cases:
# the empty list
# list with 1 element
# list with 2 elements

a = [0,4,2,7,6,5,3,9,8,1]

beatNeighbour(a)