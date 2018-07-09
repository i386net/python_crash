#7-8

sandwich_orders = ['bigmac', 'hamburger', 'cheesburger']
finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich.title())
	finished_sandwiches.append(sandwich)

print('Ready sandwiches: ')
for sandwich in finished_sandwiches:
	print('\t• ' + sandwich.title())

