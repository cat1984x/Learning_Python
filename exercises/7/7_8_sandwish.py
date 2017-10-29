active=True
while(active):
	age=input("请输入观众年龄： ")
	if(age=='quit'):
		#active=False
		break
	else:
		age=int(age)
		if(age<3):
			print(str(age)+"岁观众免费")
		elif(age>=3 and age<=12):
			print(str(age)+"岁观众10美元")
		else:
			print(str(age)+"岁观众15美元")
