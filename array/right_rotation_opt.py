# 12 reversal algorithm
def reversal_algorithm (ar, k):
	"""
	ar is array of ints
	k is and positve  int value
	"""
	n = len(ar)
	k = k % n
	temp = []
	final = []
	temp = ar + ar
	return temp[n-k:n+k]
	"""
	for i in range(0, n):
		if i < n-k:
			temp.append(ar[i])
		else:
			final.append(ar[i])
	for i in range(0, len(temp)):
		final.append(temp[i])
	return final
	"""
