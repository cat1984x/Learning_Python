sandwish_orders=['pastrami','tuna','ham','egg','pastrami','ham','pastrami',]
finished_sandwishes=[]

print("Pastrami sandwishes have been sold out.")

while 'pastrami' in sandwish_orders:
	sandwish_orders.remove('pastrami')


while sandwish_orders:
	current_sandwish=sandwish_orders.pop()
	finished_sandwishes.append(current_sandwish)
	print("I made your "+current_sandwish+"sandwish")
print("\nThese sandwishes have been made.")
for sandwish in finished_sandwishes:
	print(sandwish)
