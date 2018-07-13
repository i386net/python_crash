# 7-4

ask = True
toppings = []
while ask:
    topping = input('Please enter a pizza topping: ')
    if topping != 'quit':
        print('• Your topping ' + topping + ' was added.\n')
        toppings.append(topping)
    else:
     	ask = False
     
print("You've ordered the following toppings: ")
for topping in toppings:
	print('\t• ' + topping.title())
