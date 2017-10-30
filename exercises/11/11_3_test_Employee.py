import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	'''测试emplyee类'''
	
	def setUp(self):
		self.my_employee=Employee('chen','yushen',5000)
		self.salary=[10000,13000]	
	
	def test_give_default_raise(self):
		self.my_employee.give_raise()
		self.assertEqual(self.salary[0],self.my_employee.salary)
		
	def test_give_custom_raise(self):
		self.my_employee.give_raise(8000)
		self.assertEqual(self.salary[1],self.my_employee.salary)	
		
unittest.main()
