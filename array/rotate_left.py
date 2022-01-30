def rotate_left(ar, d: int):
	"""
	ar array with elements
	d : point to rotate
	1 2 3 4 5 6
	result 
	5 6 1 2 3 4
	"""
	temp = []
	temp1 = []
	n = len (ar)
	for i in range (0, n):
		if  i <n-d: # 6 -2 = 4
			temp.append(ar[i])
		else:
			temp1.append(ar[i])
	for i in range (0, len(temp)):
		temp1.append(temp[i])

	return temp1



