#example interface for priority queues

#Example implementation of compare
#Takes two elemets and returns an dict with their order
def compare(elem1, elem2):
	result = {}
	if elem1 > elem2:
		result = {"higherElement" : elem1, "lowerElem" : elem2}
	else:
		result = {"higherElement" : elem2, "lowerElem" : elem1}
	return result

def splitMin(heap):
	result = {}
	root = heap[0]
	# Using python list comprehension to remove the element
	newHeap = heap.remove(0)
	
	#call some method that reorders the heap 
	#following the removal of the smallest entity
	newHeap = reorderHeap(newHeap)
	result = {"root": root, "heap":newHeap}
	
	return result

# Some interface methods for Heaps
# From Chapter 6 of CLRS
# PG 154 (6.2)


def parent(i):
	return i/2

def left(i):
	return 2i

def right(i):
	return 21 +1

def minHeapReorder(A,i):
	l = left(i)
	r = right(i)

	if (l <= len(A)) and (A[l] > A[i]):
		largest = l
	else:
		largest = i

	if (r <= len(A)) and (A[r] > A[largest]):
		largest = r

	if largest != i:
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp

		minHeapReorder(A, largest)


