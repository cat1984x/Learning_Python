magicians =['chen','zhou','david']
great_magicians=[]


def show_magicians(magicians):
	for magician in magicians:
		print(magician)

def make_great(magicians):
	for index in range(0,len(magicians)):
		magicians[index]='the Great '+magicians[index]


make_great(magicians)
show_magicians(magicians)
