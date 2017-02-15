def iterateList(l, n):
	if len(l) == n:
		return l
	
	elif len(l) != n:
 		print l[n]
		n += 1
		iterateList(l, n)
	

