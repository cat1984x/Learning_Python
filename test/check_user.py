users=['Chen','John','rice','KNIGHT','King']
users_lower=[]
new_users=['zhou','JOHN','xiaomi','abb','GG']

for user in users:
	user_lower=user.lower
	users_lower.append(user_lower)
print(users_lower)

for new_user in new_users:
	if new_user.lower in users_lower:
		print(new_user+' Has exist.Please Take a another name\n')
	else:
		print(new_user+" don't exist.\n")
