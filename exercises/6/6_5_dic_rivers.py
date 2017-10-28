rivers={
	'nile':'egypt',
	'amazon':'brazil',
	'changjiang':'china',
	}

for river, country in rivers.items():
	print('The '+river.title()+' runs through '+country.title()+'.')
	
for river in rivers.keys():#打印河流名
	print(river.title())

for country in rivers.values():#打印河流名
	print(country.title())
