file_name='reasons.txt'

while True: 
    reason=input("Why you like programming? ")
    with open(file_name,'a') as file_object:
        file_object.write(reason+"\n")
