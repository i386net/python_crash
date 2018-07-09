# 7-6

active = True
toppings = []
while active:
    topping = input('Please enter a pizza topping: ')
    if topping != 'quit':
        print('• Your topping ' + topping + ' was added.\n')
        toppings.append(topping)
    else:
     	break
     
print("\nYou've ordered the following toppings: ")
for topping in toppings:
	print('\t• ' + topping.title())
