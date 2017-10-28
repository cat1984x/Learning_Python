chen={
	'first_name':'chen',
	'last_name':'yu shen',
	'age':'27',
	'city':'nanjing',
	}
	
zhou={
	'first_name':'zhou',
	'last_name':'mi',
	'age':'23',
	'city':'nanjing',
	}
	
lun={
	'first_name':'lun',
	'last_name':'zi ge',
	'age':'28',
	'city':'beijing',
	}

people =[chen,zhou,lun]


for man in people:
	for key,value in man.items():
		print(key+':'+value)
	print('\n')
	
