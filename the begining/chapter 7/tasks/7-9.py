#7-9

sandwich_orders = ['bigmac', 'pastrami', 'hamburger', 'pastrami', 'cheesburger', 'pastrami']
finished_sandwiches = []

print('Pastrami is unavailable for order!')
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:	
	sandwich = sandwich_orders.pop()
	print('I made your ' + sandwich.title())
	finished_sandwiches.append(sandwich)

print('Ready sandwiches: ')
for sandwich in finished_sandwiches:
	print('\t• ' + sandwich.title())
