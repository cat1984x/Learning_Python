from collections import OrderedDict

keyword=OrderedDict()

'''
for word, meaning in keyword.items():
    print("keyword['"+word+"']='"+meaning+"'")
'''

for word, meaning in keyword.items():
    print(word+':'+meaning)

keyword['print']='print out'
keyword['for']='create a loop'
keyword['if']='decide is or not'
keyword['range']='a list num'
keyword['else']='otherwise'
keyword['def']='define a function'
keyword['while']='a loop will continue'
keyword['break']='break out the loop'
keyword['class']='define a class'
keyword['import']='import module'


for word, meaning in keyword.items():
    print(word+':'+meaning)
