import json
file_name="favor_num.json"

def store_favor_num():
    favor_num=input("What's your favorite number? ")
    with open(file_name,'w') as f_obj:
        json.dump(favor_num,f_obj)

def read_favor_num():
    with open(file_name) as f_obj:
        favor_num=json.load(f_obj)
    print("I know your favorite number!It's "+favor_num+" .")

store_favor_num()
read_favor_num()
