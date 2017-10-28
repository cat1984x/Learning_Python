rice={
	'type':'cat',
	'owner':'chen yu shen',
	}
	
pudding={
	'type':'dog',
	'owner':'zhou mi',
	}
	
pets =[rice,pudding]


for pet in pets:
	for type,owner in pet.items():
		print(type+':'+owner)
	print('\n')
	
