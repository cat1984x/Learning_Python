from user import User
            
class Privileges():
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]   
    def show_privileges(self):
        print("You have these privileges:")
        for privilege in self.privileges:
            print(privilege)        

            
class Admin(User):
    def __init__(self,fist_name,last_name,**info):
        super().__init__(fist_name,last_name,**info)
        self.privileges=Privileges()

