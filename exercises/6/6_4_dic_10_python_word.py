keyword={
    'print':'print out',
    'for':'create a loop',
    'if':'decide is or not',
    'range':'a list num',
    'else':'otherwise',
    }



for word, meaning in keyword.items():
    print(word+':'+meaning)

print('')

keyword['def']='define a function'
keyword['while']='a loop will continue'
keyword['break']='break out the loop'
keyword['class']='define a class'
keyword['import']='import module'


for word, meaning in keyword.items():
    print(word+':'+meaning)
