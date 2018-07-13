#8-1

def display_message():
	print('Python is great!')

for i in range(5):
	display_message()

#8-2

def favorite_book(title):
	print("One of my favorite books is " + title.title())
	
favorite_book(input('Type in your favorite book '))

#8-3

def make_shirt(size='L', text='I love Python'):
	print("T-shirt size: " + size)
	print("T-shirt print: " + text.upper())
	
make_shirt()

#8-4

make_shirt('S', 'I love C++')

#8-5


