def make_sandwishes(*materials):
	print("\nMaking a sandwishes with following materials:")
	for material in materials:
		print('-'+material)
				
make_sandwishes('egg','ham')
make_sandwishes('ham')
make_sandwishes('fish','egg','chicken')
		
