class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0
	
	def describe_restaurant(self):
		print("\nThe restaurant's name is "+self.restaurant_name.title())
		print("The cuisine type is "+self.cuisine_type)
	
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is opening.")
		
	def read_number_served(self):
		print(str(self.number_served)+" people have been served.")
	
	def set_number_served(self,number_served):
		self.number_served=number_served
	
	def increment_number_served(self,number_served):
		self.number_served+=number_served

res=Restaurant('huangmen chicken','Chinese food')
res.read_number_served()

res.set_number_served(25)
res.read_number_served()

res.increment_number_served(8)
res.read_number_served()
