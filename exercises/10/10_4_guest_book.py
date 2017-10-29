file_name='guest_book.txt'

while True: 
    name=input("Please input your name. ")
    print("Hello "+name.title())
    with open(file_name,'a') as file_object:
        file_object.write(name+"\n")
