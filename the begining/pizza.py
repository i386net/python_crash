# saving information about ordered pizza
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
# order description
print('Your order is: ' + pizza['crust'] + '-crust pizza with the following toppings:')

for topping in pizza['toppings']:
    print('\t•' + topping)