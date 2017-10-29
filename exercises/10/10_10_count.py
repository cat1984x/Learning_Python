#file_name='Pride_and_Prejudice.txt'
file_name='alice.txt'

def count(file_name,word):
    try:
        with open(file_name,'r') as file_object: #rb 二进制模式
            #contents=file_object.read()
            lines=file_object.readlines()
    except FileNotFoundError:
        print(file_name+" is not found")
    else:
        #words=contents.split()
        #print("Have "+str(len(words))+" words")
        word_num=0
        #print(contents)
        for line in lines:
            #print(line)        
            word_num+=int(line.lower().count(word))
        print("Have "+str(word_num)+" 'the'.")
        

count(file_name,'the')
