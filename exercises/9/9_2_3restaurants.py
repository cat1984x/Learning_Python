class Restaurant():
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
	
	def describe_restaurant(self):
		print("\nThe restaurant's name is "+self.restaurant_name.title())
		print("The cuisine type is "+self.cuisine_type)
	
	def open_restaurant(self):
		print(self.restaurant_name.title()+" is opening.")

res1=Restaurant('huangmen chicken','Chinese food')
res2=Restaurant('sushi bar','Japan food')
res3=Restaurant('pizza hut','USA food')

res1.describe_restaurant()
res2.describe_restaurant()
res3.describe_restaurant()
