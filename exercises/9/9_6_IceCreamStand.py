class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	
	def describe_restaurant(self):
		print("\nThe restaurant's name is "+self.restaurant_name.title())
		print("The cuisine type is "+self.cuisine_type)
	
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is opening.")
		
		
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type):
		super().__init__(restaurant_name,cuisine_type)
		self.flavors=['origin','vanilla','chocolate']
		
	def show_flavors(self):
		print("We have these flavors:")
		for flavor in self.flavors:
			print(flavor)

ics=IceCreamStand('DQ','USA')
ics.show_flavors()
