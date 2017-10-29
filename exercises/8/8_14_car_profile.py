def make_car(manufacturer,model,**car_infos):
	profile={}
	profile['manufacturer']=manufacturer
	profile['model']=model
	for car_key,car_info in car_infos.items():
		profile[car_key]=car_info
	return profile
	
car={}
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
