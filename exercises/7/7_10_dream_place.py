dream_places={}

active=True
while active:
	name=input("What's your name? ")
	place=input("If you could visit one place in the world,"+
		"where would you go? ")
	dream_places[name]=place
	repeat=input("Would you like to let another person respond?(yes/no) ")
	if repeat=='no':
		active=False

for name,place in dream_places.items():
	print(name+" would like to vist "+place+".")
