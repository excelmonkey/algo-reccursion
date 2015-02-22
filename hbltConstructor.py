## Three different constructors for HBLTs

# 1
# Naive Approach that applies merge method to each and builds the tree from there

def naiveHBLTContruct(A):
	x = len(A)
	# create empty list for our HBLT
	hblt = []
	hblt.append(A[0])
	
	if len(A) > 0:
		for node to x:
			merge(hblt, A[node+1])


def merge(hblt, node):
	if len(hblt) == 0:
		hblt.append(node)
		return hblt
	else:
		i = hblt(0)
		if i > node:
			hblt.append(node)
			return hblt
		

# 2 
# Greedy Recursive Algo Example

def greedyHBLTConstructor(A, hblt):
	minValue = min(A)
	A.remove(minValue)
	merge(hblt, minValue)
	greedyHBLTConstructor(A, hblt)






