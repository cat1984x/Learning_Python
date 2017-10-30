import unittest
from city_function_11_2 import city_country

class CityTestCase(unittest.TestCase):
	'''测试城市国家函数'''
	
	def test_city_country(self):
		city_country_output=city_country('santiago','chile')
		self.assertEqual(city_country_output,'Santiago,Chile')
		
	def test_city_country_population(self):
		city_country_output=city_country('santiago','chile',\
			population=5000000)
		self.assertEqual(city_country_output,\
			'Santiago,Chile - population 5000000')
		
unittest.main()
