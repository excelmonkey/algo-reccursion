# Prof Bumsteads new sorting algo
# Taking the Java inplementation provided in assignment
# Re-written as Python

def sorter(a):
	x = sort(a,0,len(a))
	print x

def sort(a, l, r):
	print "Print Me!!"
	#print "top of sort Algo", "a=", a, "l=", l, "r=", r 
	size = r - l
	if (size <= 1):
		print "Print Me too!!"
		return a
	elif (size == 2):
		#print "check"
		print "elif entry point"
		#print "a[l]=",a[l],"a[l+1]=", a[l+1]
		if (a[l] > a[l+1]):
			#print "switch"
			tmp = a[l]
			a[l] = a[l+1]
			a[l+1] = tmp
			#print "elif exit point"
	else:
		i = size / 3
		#print "top of else:", a, i
		sort( a, l, (r - i))
		#print "post 1st recc:", a, i 
		
		sort( a, (l + i), r)
		#print "post 2nd recc:", a, i
		
		#print "pre 3rd recc", a, l, i, r
		sort( a, l, (r - i))
		#print "post 3nd recc:", a, i 	
		return a
		
#a = [4]
#a = [78,9]
#a = [5,3,6]
#a = [4,9,5,3]
#a = [4,9,5,3,6]
#a = [11,5,3,6,8,9]
#a = [11,5,3,6,8,9,18]
#a = [11,5,3,6,8,9,18,7]
#a = [11,5,3,6,8,9,18,7,10]
#a = [11,5,3,6,8,9,18,7,10,12]
#a = [4,9,5,3,2,45,7,8,45,3,23]
#a = [4,9,5,3,2,45,7,8,45,3,23,1]
#a = [4,9,5,3,2,45,7,8,45,3,23,1,18]
a = [4,9,5,3,2,45,7,8,45,3,23,1,18,25]

x = len(a)
print "Length of list A:", x
sorter(a)
