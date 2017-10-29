file_name='learning_python.txt'

'''读取整个文件'''
with open(file_name) as file_object:
    contents=file_object.read()
    print(contents)

'''遍历文件对象'''    
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())

print('')


'''存储在列表中，with外打印'''
with open(file_name) as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line.rstrip())
