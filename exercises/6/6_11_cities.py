cities={
	'beijing':{
		'country':'china',
		'population':'21710000',
		'fact':"china's captital",
		},
	'tokyo':{
		'country':'china',
		'population':'13500000',
		'fact':"japan's captital",
		},
	'nanjing':{
		'country':'china',
		'population':'8270000',
		'fact':"jiangsu provice",
		},

	}

for city_name,city_info in cities.items():
	print(city_name)
	for info_key,info in city_info.items():
		print(info_key+':'+info)
	print('')
