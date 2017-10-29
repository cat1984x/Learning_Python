magicians =['chen','zhou','david']
great_magicians=[]


def show_magicians(magicians):
	for magician in magicians:
		print(magician)
'''
def make_great(magicians):
	for index in range(0,len(magicians)):
		great_magicians.append('the Great '+magicians[index])
	return great_magicians
'''
def make_great(magicians):
	greats=[]
	for magician in magicians:
		greats.append('the Great '+magician)
	return greats


great_magicians=make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
