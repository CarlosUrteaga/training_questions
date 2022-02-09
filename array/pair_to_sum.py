def pair_to_sum(nums, val):
	len = N
	my_dict = {}
	for i in range(0, N):
		res = val-nums[i]
		if res in my_dict.keys():
			return nums[res], i
		else:
			my_dict[nums[i]] = i
	print(my_dict)
	return -1
tmp = [0, 9, 3, 7, 1, 2]
pair_to_sum(tmp, 2) 
