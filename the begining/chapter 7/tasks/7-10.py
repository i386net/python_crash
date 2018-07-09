vacation = {}

while True:
	name = input('What is your name? ')
	place = input('What place would you like to visit? ')
	vacation[name] = place
	exit = input('Continue? (yes\\no): ').lower()
	if exit == 'no':
		break
for name, place in vacation.items():
	print(name.title() + "'d like to visit " + place.title())

