# 7-4

ask = True
toppings = []
while topping != 'quit':
    topping = input('Please enter a pizza topping: ')
    if topping != 'quiit':
        print('Your topping ' + topping + ' was added.')
        toppings.append(topping)
print(*toppings)