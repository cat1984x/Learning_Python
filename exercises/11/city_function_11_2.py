def city_country(city,country,population=''):
	if population:
		'''使用\换行'''
		city_country=city.title()+","+country.title()\
			+" - population "+str(population)
	else:
		city_country=city.title()+","+country.title()
	return city_country


#print(city_country('santiago','chile'))#test
