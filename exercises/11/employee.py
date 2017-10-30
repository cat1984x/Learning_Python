class Employee:
	
	def __init__(self,first_name,last_name,salary):
		self.fist_name=first_name
		self.last_name=last_name
		self.salary=salary
		
	def give_raise(self,salary=''):
		if salary:
			self.salary+=salary
		else:
			self.salary+=5000
