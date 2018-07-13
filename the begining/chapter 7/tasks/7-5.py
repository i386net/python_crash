# 7-5



while True:
	age = int(input('Enter your age: '))
	if age < 3:
		print('You may pass for free')
	elif 3 <= 3 < 12:
		print('Price is 10$')
	else:
		print('Price is 15$')
	print('Would you like to repeat?')
	if input().title() == 'No':
		break
print('Thank you for your order 🙋‍♂️')
