class User():
	def __init__(self,fist_name,last_name,**info):
		self.infos={}
		self.infos['fist_name']=fist_name
		self.infos['last_name']=last_name
		for key,value in info.items():
			self.infos[key]=value
	
	def describe_user(self):
		for key,value in self.infos.items():
			print(key+":"+value)
		print('')
	
	def greet_user(self):
		print("Greeting,"+self.infos['fist_name'].title()+"\n")

user1=User('chen','yushen',age='27')
user2=User('zhou','mi',sex='female')
user3=User('xiao','mi',type='cat',color='white')

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
