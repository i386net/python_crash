def countdown(start):
    n = int(start)
    def display():
        print('counter: %d' % n)
    while n > 0:
        display()
        n -= 1

countdown(input('Enter a number: '))