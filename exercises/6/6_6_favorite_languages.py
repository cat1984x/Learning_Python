favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people=(
	'jen',
	'sarah',
	'chen',
	'edward',
	)

for man in people:
	if man.lower() in favorite_languages.keys():
		print(man.title()+',Thanks for your voting.')
	else:
		print(man.title()+',Please vote!')

