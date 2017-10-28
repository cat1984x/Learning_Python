favor_nums={
	'chen':[3,4,8],
	'zhou':[7,1],
	'GG':[23],
	'v':[12,7],
	'MM':[8,0],
	}

for name, nums in favor_nums.items():
	print(name+':')
	for num in nums:
		print(str(num))
	print('')
