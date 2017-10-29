'''
import car_function	
car={}
car=car_function.make_car('subaru','outback',color='blue',tow_package=True)
print(car)
'''

'''
from car_function import make_car
car={}
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
'''

'''
from car_function import make_car as mc
car={}
car=mc('subaru','outback',color='blue',tow_package=True)
print(car)
'''

'''
import car_function	as cf
car={}
car=cf.make_car('subaru','outback',color='blue',tow_package=True)
print(car)
'''

from car_function import *
car={}
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
