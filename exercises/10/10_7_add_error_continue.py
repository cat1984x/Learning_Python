print("Give me two numbers,I'll add them up.")
print("Enter a 'q' to quit.")
while True: 
    first_number=input("\nFirst number: ")
    if first_number=='q':
        break
    else:
        try:
            first_number=int(first_number)
        except ValueError:
            print("Please enter a number")
        else:
            break
            
while True:            
    second_number=input("\nSecond number: ")
    if second_number=='q':
        break
    else:
        try:
            second_number=int(second_number)
        except ValueError:
            print("Please enter a number")
        else:
            break            
            
try:        
    print(str(first_number)+" + "+str(second_number)+" = "+
        str(first_number+second_number))
except TypeError:
    print("Please enter two number")
