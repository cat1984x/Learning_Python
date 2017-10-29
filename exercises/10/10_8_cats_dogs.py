file_cats='cats.txt'
file_dogs='dogs.txt'

def read(file_name):
    try:
        with open(file_name) as file_object:
            contents=file_object.read()
    except FileNotFoundError:
        print(file_name+" is not found")
    else:
        print(contents.rstrip())

read(file_cats)
read(file_dogs)
