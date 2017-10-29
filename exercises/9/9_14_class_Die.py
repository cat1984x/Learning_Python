from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides=sides
        
    def roll_die(self):
        print(randint(1,self.sides))
        
my_10die=Die(10)
my_20die=Die(20)

for time in range(1,11):
        my_10die.roll_die()
print('')
        
for time in range(1,11):
        my_20die.roll_die()        
    
